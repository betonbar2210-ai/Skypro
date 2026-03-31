import json
from unittest.mock import Mock, patch
from src.utils import transaction_withdrawal
from src.external_api import conversion

import pytest

from src.utils import read_json

def test_read_json_try(utils_json):
    glav = Mock(return_value=utils_json)
    json.load = glav
    assert read_json() == utils_json


def test_transaction_withdrawal_rub(utils_json):
    assert transaction_withdrawal(441945886) == '31957.58'
    assert transaction_withdrawal(445) == 'id не найден'


def test_read_json_except():
    with patch('json.load', side_effect = json.JSONDecodeError('', '', 0)):
           assert read_json() == []


