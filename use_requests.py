import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    print(f'Sucess! {response}')
    print(f'Content {response.text}')
except Exception as e:
    print('There is an error', e)
print('Program ended')





