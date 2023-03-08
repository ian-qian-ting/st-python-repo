#!/usr/bin/python3
# -*- coding: utf-8 -*-

from logging import root
import os
import sys
import requests
import json
import csv
import pandas as pd

# Introduce API KEY
ST_KEY = os.getenv('ST_API_KEY')
#ST_KEY = 's1CvtAv3zyKgLw-sRc-N'

# set url
root_url = 'https://api.sensortower-china.com'
version = 'v1'
os = 'android'
query = 'store_summary'
url_segment = (root_url, version, os, query)
#print(url_segment)
url = "/".join(url_segment)
#print(url)

# set parameters : categories, countries, date_granularity, start_date, end_date
parameters = {
	'categories': 'game', # string for android, number for ios
	'countries': 'WW', 
	'date_granularity': 'monthly', # suppport 'daily', 'weekly', 'monthly', 'quarterly', defaults to 'daily'
	'start_date': '2021-07-01',
	'end_date': '2021-07-31',
	'auth_token': ST_KEY
}

# set headers
headers = {
	'accept': '*/*'
}

# get url response
response = requests.get(url, params= parameters, headers= headers)
#print(response.status_code)
#print(response.text)
body = response.json()

flattened_body = pd.json_normalize(body)
#print(flattened_body)

#output_file = open("test.csv", "w")
#flattened_body.to_csv(output_file)

with open("test.csv", "w") as f:
	flattened_body.to_csv(f)	
