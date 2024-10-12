# This code uses wifi to communicate over to the arduino

import requests

address = "http://IP ADDRESS HERE"

response = requests.post(address, {"WWADDUP"})
response.close()
print(response.json())
