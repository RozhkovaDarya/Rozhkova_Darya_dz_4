import requests
import json
import pprint
import datetime as dt


def currency_rates():
    URL = 'http://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(URL)
    
    dict = json.loads(response.text)
    

    pprint.pprint(dict['Valute']['USD'])
    pprint.pprint(dict['Valute']['EUR'])
    pprint.pprint(dict['Valute']['GBP'])

    start = dt.datetime.utcnow() + dt.timedelta(hours = 4)

    print(f"Курс USD на {start.strftime('%d %b')} равен {dict['Valute']['USD']['Value']}")
    print(f"Курс EUR на {start.strftime('%d %b')} равен {dict['Valute']['EUR']['Value']}")
    print(f"Курс GBP на {start.strftime('%d %b')} равен {dict['Valute']['GBP']['Value']}")

if __name__ == '__utils__':
    currency_rates