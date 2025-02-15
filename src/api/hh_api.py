import requests
from .base_api import BaseAPI

class HeadHunterAPI(BaseAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        self.__session = requests.Session()

    def connect(self):
        """Проверка подключения к API."""
        try:
            response = self.__session.get(self.BASE_URL)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Ошибка подключения: {e}")
            return False

    def get_vacancies(self, query: str) -> list:
        """Получение вакансий по ключевому слову."""
        params = {
            "text": query,
            "per_page": 100,
            "page": 0
        }
        response = self.__session.get(self.BASE_URL, params=params)
        if response.status_code == 200:
            return response.json().get("items", [])
        else:
            print(f"Ошибка при получении вакансий: {response.status_code}")
            return []