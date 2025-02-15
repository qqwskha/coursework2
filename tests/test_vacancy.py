from src.models.vacancy import Vacancy


def test_vacancy_creation():
    """Тест создания вакансии."""
    vacancy = Vacancy(
        title="Python Developer",
        url="http://example.com",
        salary_from=100000,
        salary_to=150000,
        description="Опыт работы от 3 лет"
    )
    assert vacancy.title == "Python Developer"
    assert vacancy.url == "http://example.com"
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 150000
    assert vacancy.description == "Опыт работы от 3 лет"


def test_vacancy_comparison():
    """Тест сравнения вакансий."""
    v1 = Vacancy("Python Dev", "http://example.com", 100000, 150000)
    v2 = Vacancy("Java Dev", "http://example.com", 120000, 160000)
    assert v1 < v2
    assert v2 > v1
    assert v1 != v2


def test_vacancy_validation():
    """Тест валидации данных."""
    vacancy = Vacancy("Python Dev", "http://example.com")
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0