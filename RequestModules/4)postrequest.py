import requests
r = requests.post('https://httpbin.org/post', data={'name': 'jalaj'})
print(r.text)