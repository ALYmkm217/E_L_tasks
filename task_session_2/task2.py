
import requests

url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

usd_rate_str = url.json() ['bpi']['USD']['rate']
usd_rate_float = float(usd_rate_str.replace(',', ''))  # Convert to float, remove commas

egp_value = (usd_rate_float * 35)

print('\n', url.json() ['bpi']['USD'])
print('\nBIT coin price in USA   : ', usd_rate_float, '  USD')
print("\nBIT coin price in Egypt : ", egp_value ,'EGP')
