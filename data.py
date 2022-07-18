import requests


class Data:
    def __init__(self) -> None:
        parameters = {
            "amount": 10,
            "type": "boolean"}
        res = requests.get(url = "https://opentdb.com/api.php", params=parameters)
        self.question_data = res.json()['results']
        