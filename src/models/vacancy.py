from dataclasses import dataclass
from typing import Optional

@dataclass
class Vacancy:
    title: str
    url: str
    salary_from: Optional[int] = None
    salary_to: Optional[int] = None
    description: str = ""

    def __post_init__(self):
        """Валидация данных."""
        if not self.salary_from and not self.salary_to:
            self.salary_from = 0
            self.salary_to = 0

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