import pandas as pd
import pytest


@pytest.fixture
def test_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.fixture
def sort_data():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def filter_state():
    return [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}]


@pytest.fixture
def utils_json():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        },
    ]


@pytest.fixture
def test_rub():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def test_usd():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


@pytest.fixture
def test_csv():
    return [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "RUB",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]


@pytest.fixture
def test_excel():
    return pd.DataFrame(
        {
            "Дата операции": [
                "2024-10-01",
                "2024-10-02",
                "2024-10-03",
                "2024-11-01",
                "2024-11-02",
                "2024-11-03",
                "2024-12-01",
                "2024-12-02",
                "2024-12-03",
            ],
            "Дата платежа": [
                "01.10.2024",
                "02.10.2024",
                "03.10.2024",
                "01.11.2024",
                "02.11.2024",
                "03.11.2024",
                "01.12.2024",
                "02.12.2024",
                "03.12.2024",
            ],
            "Сумма платежа": [-100, -200, -300, -400, -500, -600, -700, -800, -900],
            "Категория": [
                "Супермаркеты",
                "Супермаркеты",
                "Кафе",
                "Супермаркеты",
                "Кафе",
                "Супермаркеты",
                "Кафе",
                "Супермаркеты",
                "Супермаркеты",
            ],
            "Описание": [
                "Магнит",
                "Пятерочка",
                "Кофейня",
                "Перекресток",
                "Шоколадница",
                "Ашан",
                "Кофейня",
                "Metro",
                "FixPrice",
            ],
            "Номер карты": ["*5091", "*1111", "*2222", "*3333", "*4444", "*5555", "*6666", "*7777", "*8888"],
        }
    )
