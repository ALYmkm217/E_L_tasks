import requests

api_url = "https://www.boredapi.com/api/activity"
response = requests.get(api_url).json()['activity']
print("Random activity suggestion:", response)
