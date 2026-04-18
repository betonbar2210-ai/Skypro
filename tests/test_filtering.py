
from unittest.mock import patch


from src.filtering import read_file, filter_status, sort_date, sort_rub, filter_word



def test_read_file_json(utils_json):
    """Тест: пользователь выбирает JSON (пункт 1)"""
    with patch('src.filtering.read_json', return_value=utils_json):
        with patch('builtins.input', return_value="1"):
            result = read_file()
    assert result == utils_json

def test_read_file_csv(test_csv):
    """Тест: пользователь выбирает CSV (пункт 2)"""
    with patch('src.filtering.reader_csv', return_value=test_csv):
        with patch('builtins.input', return_value="2"):
            result = read_file()
    assert result == test_csv

def test_read_file_excel(test_excel):
    """Тест: пользователь выбирает Excel (пункт 3)"""
    with patch('src.filtering.reader_excel', return_value=test_excel):
        with patch('builtins.input', return_value="3"):
            result = read_file()
    assert result.to_dict(orient='records') == test_excel.to_dict(orient='records')


@patch('src.filtering.read_json')
def test_read_file_error(mock_read_json):
    """Тест: пользователь вводит неверный номер, затем выбирает JSON"""
    mock_read_json.return_value = [{"transaction": "test"}]
    with patch('builtins.input', side_effect=["4", "1"]):
        result = read_file()
    assert result == [{"transaction": "test"}]


@patch('src.processing.filter_by_state')
@patch('src.filtering.read_file')
def test_filter_status_executed(mock_read_main, mock_filter_by_state):
    """Тест: фильтрация по статусу EXECUTED"""
    mock_read_main.return_value = [{"state": "EXECUTED"}, {"state": "CANCELED"}, {"state": "PENDING"}]
    mock_filter_by_state.return_value = [{"state": "EXECUTED"}]
    with patch('builtins.input', return_value="EXECUTED"):
        result = filter_status()
    assert result == [{"state": "EXECUTED"}]


@patch('src.processing.filter_by_state')
@patch('src.filtering.read_file')
def test_filter_status_canceled(mock_read_main, mock_filter_by_state):
    """Тест: фильтрация по статусу CANCELED"""
    mock_read_main.return_value = [{"state": "EXECUTED"}, {"state": "CANCELED"}]
    mock_filter_by_state.return_value = [{"state": "CANCELED"}]
    with patch('builtins.input', return_value="CANCELED"):
        result = filter_status()
    assert result == [{"state": "CANCELED"}]


@patch('src.processing.filter_by_state')
@patch('src.filtering.read_file')
def test_filter_status_pending(mock_read_main, mock_filter_by_state):
    """Тест: фильтрация по статусу PENDING"""
    mock_read_main.return_value = [{"state": "EXECUTED"}, {"state": "PENDING"}]
    mock_filter_by_state.return_value = [{"state": "PENDING"}]
    with patch('builtins.input', return_value="PENDING"):
        result = filter_status()
    assert result == [{"state": "PENDING"}]


@patch('src.processing.filter_by_state')
@patch('src.filtering.read_file')
def test_filter_status_error(mock_read_main, mock_filter_by_state):
    """Тест: пользователь вводит неверный статус, затем правильный"""
    mock_read_main.return_value = [{"state": "EXECUTED"}, {"state": "PENDING"}]
    mock_filter_by_state.return_value = [{"state": "EXECUTED"}]
    with patch('builtins.input', side_effect=[" ", "EXECUTED"]):
        result = filter_status()
    assert result == [{"state": "EXECUTED"}]


def test_sort_date_no(sort_data):
    """Ответ нет"""
    with patch('src.filtering.filter_status', return_value=sort_data):
        with patch('builtins.input', side_effect="нет"):
            assert sort_date() == sort_data


def test_sort_date_yes_1(sort_data):
    """Ответ да по убыванию"""
    with patch('src.filtering.filter_status', return_value=sort_data):
        with patch('builtins.input', side_effect=["да", "по убыванию"] ):
            assert sort_date() == sort_data

def test_sort_date_yes_2(sort_data):
    """Ответ да по возрастанию"""
    with patch('src.filtering.filter_status', return_value=sort_data):
        with patch('builtins.input', side_effect=["да", "по возрастанию"]):
            expected_result = sorted(sort_data, key=lambda x: x['date'], reverse=False)
            assert sort_date() == expected_result

def test_sort_date_error(sort_data):
    """Ответ да с неверным ответом"""
    with patch('src.filtering.filter_status', return_value=sort_data):
        with patch('builtins.input', side_effect=["да","УБЫВАНИЕ", "по убыванию"]):
            assert sort_date() == sort_data


def test_sort_rub_yes(utils_json, test_csv):
    """Сортирует по рублям если надо"""
    with patch('src.filtering.sort_date', return_value=utils_json):
        with patch('builtins.input', return_value="да"):
            assert sort_rub() == [
                {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
                }
            ]

def test_sort_rub_no(utils_json):
    """Не сортируем по рублям"""
    with patch('src.filtering.sort_date', return_value=utils_json):
        with patch('builtins.input', return_value="нет"):
            assert sort_rub() == utils_json


def test_filter_word_no(utils_json):
    """Фильтрация по ключевым запросам если нет"""
    with patch('src.filtering.sort_rub', return_value=utils_json):
        with patch('builtins.input', return_value="нет"):
            assert filter_word() == utils_json

def test_filter_word_yes(utils_json):
    """Фильтрация по ключевым запросам если да"""
    with patch('src.filtering.sort_rub', return_value=utils_json):
        with patch('builtins.input', side_effect=["да", "перевод"]):
            assert filter_word() == [
                {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
                }
            ]

