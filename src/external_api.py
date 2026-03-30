import os
import requests
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('API_KEY')

def conversion(code, amount):
    """Функция конвертации суммы покупки иностранной валюты в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"

    payload = {}
    headers = {
        "apikey": f"{api_key}"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    result = response.json()
    return result
