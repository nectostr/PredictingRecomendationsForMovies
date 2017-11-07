import requests as re
import json


headers = {'content-type': 'application/json'}
url = 'https://cit-home1.herokuapp.com/api/rs_homework_1'

data = {"user": 18,"1":{"movie 11":2.318,"movie 21":3.8196,"movie 29":1.003},"2":{"movie 21": 3.8196}}

r = re.post(url, data=json.dumps(data), headers=headers)
print(r)
print(r.json())
