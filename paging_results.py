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

def csv_storing(name_repo, language_repo, filename='github_data.csv'):
    if os.path.exists(filename):
        return f"O arquivo '{filename}' já existe. Nenhum novo arquivo foi criado."

    data_obc = pd.DataFrame({'repos_name': name_repo, 'lang_name': language_repo})
    data_obc.to_csv(filename, index=False)

    return f"Arquivo '{filename}' criado com sucesso!"

print(csv_storing(name_repo=name_repos, language_repo=lang_repos))
