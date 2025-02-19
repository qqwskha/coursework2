import json
from os.path import join
from typing import List
from ..models.vacancy import Vacancy

class JSONSaver:
    def __init__(self, filename: str = "vacancies.json"):
        self.__filename = join("data", filename)

    def add_vacancy(self, vacancy: Vacancy):
        """Добавление вакансии в файл."""
        vacancies = self.load_vacancies()
        vacancies.append(vacancy.__dict__)
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def load_vacancies(self) -> List[dict]:
        """Загрузка вакансий из файла."""
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def delete_vacancy(self, vacancy: Vacancy):
        """
        Удаление вакансии из файла по уникальному идентификатору (URL).
        """
        vacancies = self.load_vacancies()
        vacancies = [v for v in vacancies if v["url"] != vacancy.url]
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)