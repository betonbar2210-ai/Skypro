import json
import os
from unittest.mock import Mock, patch

from src.external_api import conversion
from src.utils import transaction_withdrawal
from config import ROOT_DIR


from src.utils import read_json


def test_read_json_try(utils_json):
    glav = Mock(return_value=utils_json)
    json.load = glav
    way_file = os.path.join(ROOT_DIR, "data", "operations.json")
    assert read_json(way_file) == utils_json


def test_transaction_withdrawal_rub(test_rub):
    assert transaction_withdrawal(test_rub) == '31957.58'


@patch('src.utils.conversion')
def test_transaction_withdrawal_usd(mock_usd, test_usd):
    mock_usd.return_value = {"conversion_result" : 56.21}
    assert transaction_withdrawal(test_usd) == 56.21





def test_read_json_except():
    with patch("json.load", side_effect=json.JSONDecodeError("", "", 0)):
        way_file = os.path.join(ROOT_DIR, "data", "operations.json")
        assert read_json(way_file) == []
