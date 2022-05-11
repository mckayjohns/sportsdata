import requests

url = "https://v3.football.api-sports.io/{endpoint}"

payload={}
headers = {
  'x-rapidapi-key': '',
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)