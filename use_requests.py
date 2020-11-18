import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    print(f'Sucess! {response}')
except Exception as e:
    print('There is an error', e)
print('Program ended')


