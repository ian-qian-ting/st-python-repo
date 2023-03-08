#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import requests
import json
import csv
import pandas as pd
import time
import numpy as np

# handle region code situation

region_country_dict = {}
# if retrieved country is None or WW use country list in region_country_dict['WW'] 
region_country_dict['WW'] = ['US','CN','DE','FR','JP','KR','TW','HK','SA','ID','BR']
region_country_dict['ASIA'] = ['AF', 'AM', 'AZ', 'BD', 'BT', 'BN', 'KH', 'CN', 'GE', 'HK', 'IN', 'ID', 'JP', 'KZ', 'KP', 'KR', 'KG', 'LA', 'MO', 'MY', 'MV', 'MN', 'MM', 'NP', 'PK', 'PH', 'SG', 'LK', 'TW', 'TJ', 'TH', 'TL', 'TM', 'UZ', 'VN']
region_country_dict['CARIB'] = ['AI', 'AG', 'AW', 'BS', 'BB', 'BQ', 'VG', 'VI', 'KY', 'CU', 'CW', 'DO', 'DM', 'GD', 'GP', 'HT', 'JM', 'MQ', 'MS', 'PR', 'BL', 'KN', 'LC', 'MF', 'TT', 'TC', 'VC', 'SX']
region_country_dict['CENTR_AM'] = ['BZ', 'CR', 'SV', 'GT', 'HN', 'NI', 'PA', 'MX']
region_country_dict['EUR_UN'] = ['AT', 'BE', 'BG', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE', 'GB']
region_country_dict['EUROPE'] = ['AL', 'AD', 'BY', 'BA', 'HR', 'FO', 'GI', 'GG', 'IS', 'JE', 'LI', 'MK', 'IM', 'MD', 'MC', 'ME', 'NO', 'RU', 'SM', 'RS', 'SJ', 'CH', 'TR', 'UA', 'VA', 'AT', 'BE', 'BG', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL', 'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE', 'GB']
region_country_dict['LATIN_AM'] = ['AR', 'BO', 'BR', 'CL', 'CO', 'CR', 'DO', 'EC', 'SV', 'GT', 'HN', 'MX', 'NI', 'PA', 'PY', 'PE', 'UY', 'VE']
region_country_dict['MID_EAST'] = ['BH', 'IQ', 'IR', 'IL', 'JO', 'KW', 'LB', 'OM', 'PS', 'QA', 'SA', 'SY', 'AE', 'YE']
region_country_dict['NORTH_AM'] = ['US', 'CA', 'GL', 'PM', 'BM']
region_country_dict['OCEANIA'] = ['AU', 'FJ', 'PF', 'GU', 'KI', 'MH', 'FM', 'NC', 'NZ', 'PG', 'WS', 'AS', 'SB', 'TO', 'VU']
region_country_dict['SOUTH_AM'] = ['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK', 'GF', 'GY', 'PY', 'PE', 'SR', 'UY', 'VE']
region_country_dict['SE_ASIA'] = ['ID', 'MY', 'PH', 'SG', 'TH', 'VN', 'KH']

# Introduce API KEY
ST_KEY = os.getenv('ST_API_KEY')
#print(ST_KEY)

# return a json object containing app metadata
def API_get_single_app_metadata(app_id, app_country, ST_KEY):
	if isinstance(app_id, (int, np.integer)):
		app_os = 'ios'
	elif isinstance(app_id, str):
		app_os = 'android'
	else:
		print("invalid app id")
		return None

	root_url = 'https://api.sensortower-china.com'
	version = 'v1'
	os = app_os # 'ios'/'android'
	query = 'apps'
	url_segment = (root_url, version, os, query)
	#print(url_segment)
	url = "/".join(url_segment)
	#print(url)

	# set parameters
	parameters = {
		'app_ids': app_id,
		'country': app_country,
		'auth_token': ST_KEY
	}

	# set headers
	headers = {
		'accept': 'application/json'
	}

	# get url response
	response = requests.get(url, params= parameters, headers= headers)
	body = response.json()	
	return body

# STEP 1: set url for custom_fields_filter_id
root_url1 = 'https://api.sensortower-china.com'
version1 = 'v1'
query1 = 'custom_fields_filter'
url_segment1 = (root_url1, version1, query1)
url1 = "/".join(url_segment1)

# set parameter
parameter1 = {
	'auth_token': ST_KEY
}

# add custom fields
# function to form custom fields - TBD
#def add_custom_fields_by_name_value(name, value):

data1 = {
  "custom_fields": [
    {
      "exclude": False, # choose if apps excluding below tags
      "global": True, # choose if tags are global or not
      "name": "Game Genre",
      "values": [
        "Action"
      ]
    }
#		{
#      "exclude": False, # choose if apps excluding below tags
#      "global": True, # choose if tags are global or not
#      "name": "Game Sub-genre",
#      "values": [
#        "Turn-based RPG"
#      ]			
#		}
#		{
#      "exclude": False, # choose if apps excluding below tags
#      "global": True, # choose if tags are global or not
#      "name": "Game Class",
#      "values": [
#        "Mid-core"
#				#"Casual"
#      ]			
#		}
  ]
}

# set headers
headers1 = {
	'accept': 'application/json',
	'Content-Type': 'application/json'
}

# get url response
response1 = requests.post(url1, params= parameter1, json = data1, headers = headers1)
if response1.status_code != 200:
	print("error: " + str(response1.status_code))
	sys.exit()

#print(response1.status_code)
body1 = response1.json()
#print(body1)
filter_id = body1['custom_fields_filter_id']
#print(filter_id)


# STEP 2: set url for comparison attributes
root_url2 = 'https://api.sensortower-china.com'
version2 = 'v1'
os2 = 'unified' # 'ios'/'android'/'unified'
query2 = 'sales_report_estimates_comparison_attributes'
url_segment2 = (root_url2, version2, os2, query2)
#print(url_segment2)
url2 = "/".join(url_segment2)
#print(url2)

# set parameters : categories, countries, date_granularity, start_date, end_date
parameters2 = {
	'comparison_attribute': 'absolute', # 'absolute'/'delta'/'transformed_delta'
	'time_range': 'month', # 'day'/'week'/'month'/'quarter'/'year'
	'measure': 'units', # 'units'/'revenue' revenue = net revenue in cents
	'device_type': 'total', # 'iphone','ipad' or 'total' for ios / '' for android / 'total' for unified
	'category': 6014, # number for ios or unified, string for android; reference: https://app.sensortower.com/api/docs/static/category_ids.json
	'country': 'JP', # reference: https://app.sensortower.com/api/docs/static/country_ids.json (country) https://app.sensortower.com/api/docs/static/region_ids.json (region)
	'limit': 100, # max: 2000
	'offset': 0,
	'date': '2022-01-01',
	'end_date': '2022-12-31',
	#'custom_fields_filter_id': filter_id,
	#'custom_tags_mode': 'include_unified_apps', # '--' / 'include_unified_apps' / 'exclude_unified_apps'
	'auth_token': ST_KEY
}

# set headers
headers2 = {
	'accept': '*/*'
}

# get url response
response2 = requests.get(url2, params= parameters2, headers= headers2)
if response2.status_code != 200:
	print("error: " + str(response2.status_code))
	sys.exit()
body2 = response2.json()

output_file = "input.csv"
if os.path.exists(output_file):
	os.remove(output_file)

with open(output_file, "w") as f:
	# create container to hold interesting data
	df = pd.DataFrame()
	for i in range(len(body2)):
		app_info = body2[i]
		app_entity_info = pd.json_normalize(app_info, record_path = ['entities'], meta=['app_id', 'units_absolute', 'units_delta', 'units_transformed_delta', 'revenue_absolute', 'revenue_delta', 'revenue_transformed_delta'], errors='ignore', max_level=1, meta_prefix='unified_', sep='_')

		# get the first app entity
		tmp_app_entity_id = app_entity_id = app_entity_info.at[0,'app_id']
		app_entity_country = app_entity_info.at[0,'country']
		#print(app_entity_country)
		if app_entity_country is None:
			for country in region_country_dict['WW']:
				app_entity_metadata = API_get_single_app_metadata(app_entity_id, country, ST_KEY)
				if app_entity_metadata != None:
					break
				time.sleep(0.001)
		elif app_entity_country in list(region_country_dict.keys()):
			for country in region_country_dict[app_entity_country]:
				app_entity_metadata = API_get_single_app_metadata(app_entity_id, country, ST_KEY)
				if app_entity_metadata != None:
					break
				time.sleep(0.001)	
		else:		
			app_entity_metadata = API_get_single_app_metadata(app_entity_id, app_entity_country, ST_KEY)	

		tmp_app_entity_country = None
		tmp_app_entity_metadata = None	

		for j in range(1,len(app_entity_info)):
			tmp_app_entity_id = app_entity_info.at[j,'app_id']
			#print(tmp_app_entity_id)
			if isinstance(tmp_app_entity_id, str) and app_entity_metadata != None:
				continue
			tmp_app_entity_country = app_entity_info.at[j,'country']
			#print(type(tmp_app_entity_country))
			if tmp_app_entity_country is None:
				for country in region_country_dict['WW']:
					tmp_app_entity_metadata = API_get_single_app_metadata(tmp_app_entity_id, country, ST_KEY)
					if tmp_app_entity_metadata != None:
						break
					time.sleep(0.001)
			elif tmp_app_entity_country in list(region_country_dict.keys()):
				for country in region_country_dict[tmp_app_entity_country]:
					tmp_app_entity_metadata = API_get_single_app_metadata(tmp_app_entity_id, country, ST_KEY)
					if tmp_app_entity_metadata != None:
						break
					time.sleep(0.001)				
			else:
				tmp_app_entity_metadata = API_get_single_app_metadata(tmp_app_entity_id, tmp_app_entity_country, ST_KEY)	

			if tmp_app_entity_metadata != None:
				app_entity_id = tmp_app_entity_id
				app_entity_country = tmp_app_entity_country
				app_entity_metadata = tmp_app_entity_metadata
				break

		#print(app_entity_metadata)
		if app_entity_metadata != None:
			app_entity_metadata_norm = pd.json_normalize(app_entity_metadata, record_path= ['apps'], max_level=1)
		else:
			app_entity_metadata_norm = pd.DataFrame({'humanized_name':'not found','publisher_name':'not found','publisher_country':'not found','icon_url':''},index=[0])
		tmp_df = pd.DataFrame([[\
			app_entity_info.at[0,'unified_app_id'],\
			app_entity_metadata_norm.at[0,'humanized_name'],\
			app_entity_info.at[0,'unified_units_absolute'],\
			app_entity_info.at[0,'unified_units_delta'],\
			app_entity_info.at[0,'unified_units_transformed_delta'],\
			app_entity_info.at[0,'unified_revenue_absolute'] / 100.0 / 0.7,\
			app_entity_info.at[0,'unified_revenue_delta'] / 100.0 / 0.7,\
			app_entity_info.at[0,'unified_revenue_transformed_delta'],\
			app_entity_metadata_norm.at[0,'publisher_name'],\
			app_entity_metadata_norm.at[0,'publisher_country'],\
			app_entity_metadata_norm.at[0,'icon_url'].replace('150x150','450x450') \
			]],columns=['unified_app_id','app_name','absolute_downloads','delta_downloads','transformed_delta_downloads',\
	'absolute_revenue','delta_revenue','transformed_delta_revenue','publisher_name','publisher_country','icon_url'])
		#print(tmp_df)
		df = df.append(tmp_df,ignore_index=True)
		#pd.concat([df,tmp_df])
		#print(df)
		time.sleep(0.01)
	df.to_csv(f)


