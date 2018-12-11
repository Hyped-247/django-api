import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'

END_POINT = 'author/api'


def get_author_list():
	r = requests.get(BASE_URL + END_POINT)
	return r.json()


def create_new_author():
	data = {'name': 'Adam Lan'}
	data_dumps = json.dumps(data)
	r = requests.post(BASE_URL + END_POINT + '/', data=json.loads(data_dumps))
	return r.json()


def get_author_detail(pk):
	r = requests.get(BASE_URL + END_POINT + '/' + f'{pk}/')
	return r.json()


def update_existing_author(pk):
	data = {'name': 'Mo'}
	data_dumps = json.dumps(data)
	r = requests.put(BASE_URL + END_POINT + '/' + f'{pk}/', data=data_dumps)
	return r.json()


def delete_existing_author(pk):
	r = requests.delete(BASE_URL + END_POINT + '/' + f'{pk}/')
	return r.json()


print(get_author_detail(29))




