import requests
import json


BASE_URL = "http://127.0.0.1:8000/status/api/"


end_point = BASE_URL + str(1)
post_data = json.dumps({"content": "Here is some information."})

# r = requests.get(end_point)
# print(r.text)
#
# r2 = requests.get(end_point)
# print(r2.status_code)

post_headers = {
	'content-type': 'application/json'
}

r3 = requests.post(end_point, data=post_data, headers=post_headers)
print(r3.text)





