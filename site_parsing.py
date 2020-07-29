import requests
import json
from bs4 import BeautifulSoup as bs


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

b_url = 'https://sinoptik.com.ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BE%D0%BC%D1%81%D0%BA'

def pars_weather():

    session = requests.Session()
    request = session.get(b_url, headers=headers)

    if request.status_code == 200:

        end_data = []
        soup = bs(request.content, "lxml")
        weather__content = soup.find('div', attrs={'class': 'weather__content_tabs'})
        days_info = weather__content.find_all('div', attrs={'class': 'weather__content_tab'})
        for day in days_info:

            data = {
                'dayofweek': day.p.text,
                'month': day.find('p', attrs={'class': 'weather__content_tab-month'}).text,
                'dayofmonth': day.find('p', attrs={'class': 'weather__content_tab-date'}).text,
                'weather': day.find('div', attrs={'class': 'weather__content_tab-icon'}).text,
                'temperature': day.find('div', attrs={'class': 'weather__content_tab-temperature'}).text,
            }
            end_data.append(data)
        return end_data


print(pars_weather())
with open('weather_file.json', 'w', encoding="utf-8") as write_file:
    json.dump(pars_weather(), write_file, ensure_ascii=False)