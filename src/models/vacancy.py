from typing import Optional

class Vacancy:
    __slots__ = ("title", "url", "salary_from", "salary_to", "description")

    def __init__(self, title: str, url: str, salary_from: Optional[int] = None, salary_to: Optional[int] = None, description: str = ""):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description
        self._validate_data()

    def _validate_data(self):
        """
        Приватный метод для валидации данных.
        Если оба поля salary_from и salary_to равны None, устанавливаем их в 0.
        """
        if not self.salary_from and not self.salary_to:
            self.salary_from = 0
            self.salary_to = 0

    def to_dict(self):
        """
        Возвращает словарь с данными объекта Vacancy.
        """
        return {
            "title": self.title,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description
        }

    def __str__(self):
        return f"{self.title} ({self.salary_from}-{self.salary_to})"

    def __eq__(self, other):
        """Сравнение вакансий по зарплате."""
        return self.salary_from == other.salary_from and self.salary_to == other.salary_to

    def __lt__(self, other):
        """Сравнение вакансий по зарплате (меньше)."""
        return (self.salary_from or 0) < (other.salary_from or 0)

    def __gt__(self, other):
        """Сравнение вакансий по зарплате (больше)."""
        return (self.salary_from or 0) > (other.salary_from or 0)