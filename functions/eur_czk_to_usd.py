import requests
from bs4 import BeautifulSoup 
from datetime import datetime 

headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

url = 'https://www.fio.cz/akcie-investice/dalsi-sluzby-fio/devizove-konverze'
response = requests.get(url, headers)
soup = BeautifulSoup(response.text, 'lxml')

table = soup.find("table")
last_row = table("tr")[-1]
value = last_row.find_all('td')[4].text.strip()
# print(value)

value = value.replace(',','.')

# # сколько отдаю 
# input_czk = float(input('write czk: '))
# usd = float(input_czk / float(value))

# print(usd)


# # сколько получу 
# input_usd = float(input('write usd: '))
# czk = float(input_czk * float(value))

# print(czk)

"""
bank transfer IBAN bic swift 
visa/mastercard - credit card
2002416156 / 2010 - перевод в рамках Чехии - CZK
IBAN:CZ56 2010 0000 0020 0241 6156 - международный перевод 
BIC/SWIFT:FIOBCZPPXXX 


Сделать долар везде
брать курс из čnb и переводить
Сколько хочет получить 
пополнение в доларах 
обмен на евро и кроны 
"""

