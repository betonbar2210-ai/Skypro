import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


load_dotenv()
api_key = os.getenv("API_KEY")


def conversion(code, amount):
    """Функция конвертации иностранной валюты в рубли через API https://app.exchangerate-api.com/dashboard/confirmed"""
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{code}/RUB/{amount}"
    response = requests.get(url)
    result = response.json()
    return result
