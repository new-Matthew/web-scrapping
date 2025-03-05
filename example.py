import requests




headers = {'X-GitHub-Api-Version': '2022-11-28'}
base_api = 'https://api.github.com'
user = ''
url = f'{base_api}/users/{user}/repos'

response = requests.get(url, headers=headers)
print(response.status_code)
print(len(response.json()))
print(response.json())