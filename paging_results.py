from dotenv import load_dotenv
import requests
import os
from collections import Counter
import pandas as pd
load_dotenv()

access_token = os.getenv("GITHUB_TOKEN")
headers = {
    'Authorization': 'Bearer ' +access_token,
    'X-GitHub-Api-Version': '2022-11-28'
}

base_api = 'https://api.github.com'
user = 'alyssonwolfpoet'
url = f'{base_api}/users/{user}/repos'
response = requests.get(url, headers=headers)

repos_list = []
page = 1

while True:
    url_page = f'{url}?page={page}&per_page=30'
    response = requests.get(url_page, headers=headers)

    if response.status_code != 200:
        print(f"Erro {response.status_code}: {response.json()}")
        break

    repos = response.json()

    if not repos:
        break

    repos_list.extend(repos)
    page += 1

print(f'Total de repositórios encontrados: {len(repos_list)}')
print(f'Última URL consultada: {url_page}')

name_repos = []

for repo in repos_list:
    name_repos.append(repo['name'])

lang_repos = []
for repo in repos_list:
    lang_repos.append(repo['language'])

print(Counter(lang_repos))
print(name_repos)

