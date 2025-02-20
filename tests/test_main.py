from unittest.mock import patch

from main import user_interaction


@patch("builtins.input", side_effect=["Python", "1", "desc"])  # Добавлено значение для порядка сортировки
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

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "Java Dev" in captured.out  # При сортировке по убыванию Java Dev должна быть первой
    assert "120000-160000" in captured.out
