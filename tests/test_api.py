import pytest
from src.api.hh_api import HeadHunterAPI


@pytest.fixture
def hh_api():
    """Фикстура для создания экземпляра HeadHunterAPI."""
    return HeadHunterAPI()


def test_connect(hh_api):
    """Тест подключения к API."""
    assert hh_api.connect() is True


def test_get_vacancies(hh_api):
    """Тест получения вакансий."""
    vacancies = hh_api.get_vacancies("Python")
    assert isinstance(vacancies, list)
    if vacancies:
        vacancy = vacancies[0]
        assert "name" in vacancy
        assert "alternate_url" in vacancy
