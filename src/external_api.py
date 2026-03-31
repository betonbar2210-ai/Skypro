import os
import requests
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('API_KEY')

import os
import requests
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('API_KEY')

def conversion(code, amount):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{code}/RUB/{amount}"
    response = requests.get(url)
    result = response.json()
    return result
