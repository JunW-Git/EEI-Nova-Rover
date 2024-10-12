# This code uses wifi to communicate over to the arduino

import requests

address = "http://192.168.68.51"

response = requests.post(address, {"WWADDUP"})
response.close()
print(response.json())