from abc import ABC, abstractmethod
from typing import List, Dict


class BaseAPI(ABC):
    @abstractmethod
    def connect(self) -> bool:
        """
        Метод для подключения к API.
        Возвращает True, если подключение успешно, иначе False.
        """
        pass

    @abstractmethod
    def get_vacancies(self, query: str) -> List[Dict]:
        """
        Метод для получения вакансий по запросу.
        Возвращает список словарей с данными о вакансиях.
        """
        pass