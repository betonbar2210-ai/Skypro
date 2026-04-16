import csv
import os
from unittest.mock import Mock, patch

from config import ROOT_DIR
from src.reader_csv_xlsl import reader_excel, reader_csv


def test_reader_csv(test_csv):
    way_csv = os.path.join(ROOT_DIR, "data", "transactions.csv")
    mock_csv = Mock(return_value=test_csv)
    csv.DictReader = mock_csv
    assert reader_csv(way_csv) == test_csv


@patch("pandas.read_excel")
def test_reader_excel(mock_excel, test_excel):
    mock_excel.return_value.to_dict.return_value = test_excel
    assert reader_excel('').to_dict() == test_excel.to_dict()
