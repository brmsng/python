import requests

jeff = 'All teams will henceforth expose their data and functionality through service interfaces'
headers = {
    'X-Naver-Client-Id': 'RhZL4KGyFuAHjyqLKvOb',
    'X-Naver-Client-Secret': 'qjmeRPBkLr'
}
data = {
    'source': 'en',
    'target': 'ko',
    'text': jeff
}
res = requests.post('https://openapi.naver.com/v1/papago/n2mt',
              headers=headers, data=data)

from_server = res.json()
print(from_server['message']['result']['translatedText'])
