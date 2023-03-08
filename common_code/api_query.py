
import requests
import json
import csv
import pandas as pd

# Introduce API KEY
#ST_KEY = os.getenv('ST_API_KEY')
ST_KEY = 's1CvtAv3zyKgLw-sRc-N'

root_url = 'https://api.sensortower.com/v1/ios/search_entities'

parameters = {
	'os': 'ios',
	'entity_type': 'app',
	'term': 'Lyft',
	'limit': 10,
	'auth_token': ST_KEY
}

headers = {
	'accept': '*/*'
}

response = requests.get(url, params= parameters, headers= headers)
print(response.status_code)
#print(response.text)
body = response.json()

output_file = 'output.csv'
csv_data = open(output_file, 'w')
csv_writer = csv.writer(csv_data)

count = 0

for tmp in body:
	if count == 0:
		# Writing header
		header = tmp.keys()
		csv_writer.writerow(header)
		count += 1
	csv_writer.writerow(tmp.values())

csv_data.close()

