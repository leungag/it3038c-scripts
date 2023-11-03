import json
import requests

print('Please enter your zip code: ')
zip = input()


r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=3b12ad914d7f74ec0aaa1b29bb3618da' % zip)

data=r.json()
print(data['weather'][0]['description'])