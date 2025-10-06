import requests

url = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6  /jobs"

headers = {
    'X-API-Key': 'jobboerse-jobsuche',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.115',
    'Copnnection': 'keep-alive'
}

for page in range (1,6):
    params = {
        'angebotsart' : '34',
        'was': 'Informatik',
        'wo': 'Leipzig',
        'umkreis': '10',
        'page': page
    }

response = requests.get (url, headers=headers, params=params)

print (response.status_code)

if response.status_code == 200:
    data = response.json()

    print (data)