from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.json_saver import JSONSaver


def user_interaction():
    hh_api = HeadHunterAPI()
    json_saver = JSONSaver()
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    sort_order = input("Введите порядок сортировки (asc/desc): ").strip().lower()

    # Получение вакансий
    raw_vacancies = hh_api.get_vacancies(search_query)
    vacancies = [
        Vacancy(
            title=v["name"],
            url=v["alternate_url"],
            salary_from=v["salary"]["from"] if v.get("salary") else None,
            salary_to=v["salary"]["to"] if v.get("salary") else None,
            description=v.get("snippet", {}).get("requirement", "Описание отсутствует")
        )
        for v in raw_vacancies
    ]

    # Сохранение вакансий
    for vacancy in vacancies:
        json_saver.add_vacancy(vacancy)

    # Сортировка вакансий по зарплате
    reverse = sort_order == "desc"
    sorted_vacancies = sorted(
        vacancies,
        key=lambda x: x.salary_from or 0,
        reverse=reverse
    )

    # Вывод топ-N вакансий
    for vacancy in sorted_vacancies[:top_n]:
        print(vacancy)

if __name__ == "__main__":
    user_interaction()