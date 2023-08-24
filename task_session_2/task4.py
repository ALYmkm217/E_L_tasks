# #pip install requests
# # you will need to use sudo for running this script

import requests

api_url = "https://ipinfo.io/198.16.66.123/geo"
response = requests.get(api_url).json()

print("IP Information:")
print(f"IP Address: {response.get('ip', 'N/A')}")
print(f"City: {response.get('city', 'N/A')}")
print(f"Region: {response.get('region', 'N/A')}")
print(f"Country: {response.get('country', 'N/A')}")
print(f"Location: {response.get('loc', 'N/A')}")

