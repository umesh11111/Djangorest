import requests

import json

BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='bucketlists/'

r=requests.get(BASE_URL+ENDPOINT+'2/')

emp=r.json()

print("Employee id:",emp['id'])
print("Employee Name:",emp['name'])
print("Employee date created:",emp['date_created'])
print("Employee date modified:",emp['date_modified'])
