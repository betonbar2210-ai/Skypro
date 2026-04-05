import csv
import pandas as pd



def reader_csv(way_csv):
    """Функция чтения cvs файла вернуть список словарей"""
    with open(way_csv, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter= ';')
        data_csv = []
        for row in reader:
            data_csv.append(row)
        return data_csv


def reader_exel(way_excel):
    """Функция чтения EXCEL файла с помощью pandas"""
    data_excel = pd.read_excel(way_excel)
    return data_excel


