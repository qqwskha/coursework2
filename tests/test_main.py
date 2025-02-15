from unittest.mock import patch

from main import user_interaction


@patch("builtins.input", side_effect=["Python", "1"])  # Запрос топ-1 вакансии
@patch("src.api.hh_api.HeadHunterAPI.get_vacancies", return_value=[
    {
        "name": "Python Dev",
        "alternate_url": "http://example.com",
        "salary": {"from": 100000, "to": 150000},
        "snippet": {"requirement": "Опыт работы от 3 лет"}
    },
    {
        "name": "Java Dev",
        "alternate_url": "http://example.com",
        "salary": {"from": 120000, "to": 160000},
        "snippet": {"requirement": "Опыт работы от 5 лет"}
    }
])
def test_user_interaction(mock_get_vacancies, mock_input, capsys):
    """Тест взаимодействия с пользователем."""
    user_interaction()
    captured = capsys.readouterr()
    assert "Java Dev" in captured.out  # Ожидаем топ-1 вакансию с самой высокой зарплатой
    assert "Python Dev" not in captured.out  # Вторая вакансия не должна быть в выводе
