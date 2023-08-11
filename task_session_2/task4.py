#pip install requests
# you will need to use sudo for running this script

import requests

api_url = "https://api.ipify.org/?format=json"
response = requests.get(api_url).json()['ip']
print("Your public IP address:", response)
