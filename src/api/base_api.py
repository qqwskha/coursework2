from abc import ABC, abstractmethod


class BaseAPI(ABC):
    @abstractmethod
    def connect(self):
        """Метод для подключения к API."""
        pass

    @abstractmethod
    def get_vacancies(self, query: str) -> list:
        """Метод для получения вакансий по запросу."""
        pass
