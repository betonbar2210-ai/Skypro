import os

from config import ROOT_DIR
from src.utils import read_json, transaction_withdrawal



if __name__ == "__main__":
    way_file = os.path.join(ROOT_DIR, "data", "operations.json")
    transactions = read_json(way_file)
    for transaction in transactions:
        print(transaction_withdrawal(transaction))
        break
