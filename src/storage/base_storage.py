from abc import ABC, abstractmethod
from typing import List, Dict

class BaseStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Dict) -> None:
        """Добавляет вакансию в хранилище."""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Dict) -> None:
        """Удаляет вакансию из хранилища."""
        pass

    @abstractmethod
    def get_vacancies(self) -> List[Dict]:
        """Возвращает список всех вакансий."""
        pass