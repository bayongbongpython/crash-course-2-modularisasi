import requests

url = 'https://detik.com'
try:
    requests.get(url)
    print('Sucess!')
except Exception as e:
    print('There is an error', e)
print('Program ended')


