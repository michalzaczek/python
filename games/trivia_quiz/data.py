import requests

api_parameters = {
    'amount': 10,
    'type': 'boolean'
}

api_url = 'https://opentdb.com/api.php'

response = requests.get(url=api_url, params=api_parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']