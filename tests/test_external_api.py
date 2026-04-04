from src.external_api import conversion
from unittest.mock import patch


@patch("requests.get")
def test_conversion(mock_test, utils_json):
    mock_test.return_value.json.return_value = utils_json
    assert conversion("", "") == utils_json
