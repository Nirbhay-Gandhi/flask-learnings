import requests
import time

url1 = 'https://www.berkshirehathaway.com/' #'https://adamw.uk/'
url2 = 'https://adamw.uk/'
url3 = 'https://github.com/Nirbhay-Gandhi'
url4 = 'https://httpbin.org/get'
url5 = 'https://httpbin.org/post'

# payload = {'page' : 20, 'count' : 10, 'name': 'Nirbhay'}
# response = requests.get(url4, params=payload)
# response = requests.get(url4, params=payload, timeout=3)

# print(response.url)
# print(response.text)


payload = {'username': 'Nirbhay Gandhi', 'password': 'test'}
response = requests.post(url5, data=payload)
print(response.url)
print(response.text)
print(response.json())