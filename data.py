import requests

parameters = {
    "amount": 10,
    "type": "boolean"}
res = requests.get(url = "https://opentdb.com/api.php", params=parameters)
question_data = res.json()['results']