from bs4 import BeautifulSoup
import requests

response = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&cboWorkExp1=-1&txtLocation=')
print(response.status_code)

soup = BeautifulSoup(response.text, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    name_company = job.find('h3', class_='joblist-comp-name').text.strip().replace(' ', '')

    skill = job.find('span', class_='srp-skills').text.strip().replace(' ', '')

    pub_date = job.find('span', class_='sim-posted').span.text[7:]
    print(pub_date)