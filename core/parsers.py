import requests
from bs4 import BeautifulSoup

def parse_hh():
    url = "https://hh.ru/search/vacancy"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Парсинг данных, пример:
    jobs = []
    for item in soup.find_all('div', class_='vacancy-serp-item'):
        job_title = item.find('a', class_='bloko-link').text
        company = item.find('a', class_='bloko-link bloko-link_secondary').text
        jobs.append({'job_title': job_title, 'company': company})
    return jobs

