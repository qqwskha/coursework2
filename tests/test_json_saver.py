import os

import pytest

from src.storage.json_saver import JSONSaver
from src.models.vacancy import Vacancy


@pytest.fixture
def json_saver():
    """Фикстура для создания экземпляра JSONSaver."""
    return JSONSaver("test_vacancies.json")


def test_add_vacancy(json_saver):
    """Тест добавления вакансии."""
    vacancy = Vacancy("Python Dev", "http://example.com", 100000, 150000)
    json_saver.add_vacancy(vacancy)
    vacancies = json_saver.load_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0]["title"] == "Python Dev"


def test_delete_vacancy(json_saver):
    """Тест удаления вакансии."""
    vacancy = Vacancy("Python Dev", "http://example.com", 100000, 150000)
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)
    vacancies = json_saver.load_vacancies()
    assert len(vacancies) == 0


def test_load_vacancies(json_saver):
    """Тест загрузки вакансий."""
    vacancies = json_saver.load_vacancies()
    assert isinstance(vacancies, list)


def teardown_module():
    """Удаление тестового файла после завершения тестов."""
    if os.path.exists("data/test_vacancies.json"):
        os.remove("data/test_vacancies.json")
