import requests
from typing import List, Dict
from .base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        self.__session = requests.Session()

    def _connect(self) -> bool:
        """
        Приватный метод для проверки подключения к API.
        Возвращает True, если подключение успешно, иначе False.
        """
        try:
            response = self.__session.get(self.BASE_URL)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Ошибка подключения: {e}")
            return False

    def connect(self) -> bool:
        """
        Публичный метод для подключения к API.
        Вызывает приватный метод _connect.
        """
        return self._connect()

    def get_vacancies(self, query: str) -> List[Dict]:
        """
        Получение вакансий по ключевому слову.
        Возвращает список словарей с данными о вакансиях.
        """
        if not self.connect():
            print("Не удалось подключиться к API.")
            return []

        params = {
            "text": query,
            "per_page": 100,
            "page": 0
        }
        response = self.__session.get(self.BASE_URL, params=params)

        try:
            data = response.json()
        except ValueError:
            print("Ошибка: получен невалидный JSON.")
            return []

        if response.status_code == 200:
            return data.get("items", [])
        else:
            print(f"Ошибка при получении вакансий: {response.status_code}")
            return []