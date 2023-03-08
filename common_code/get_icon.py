#import requests as req
import os
import urllib.request
import sys
import pandas

# Usage: python/python3 get_icon.py input.csv output_filename

# get input parameters
n = len(sys.argv)
if n != 3:
	print("2 parameters needed: you should specify input csv file and output relative directory")
	exit
else:
	input_filename = sys.argv[1]
	rel_dir = sys.argv[2]

data = 	pandas.read_csv(input_filename)

subdata = data[["unified_app_name","icon_url"]]
cwd = os.getcwd()
#print(cwd)
dir = os.path.join(cwd, rel_dir)
if not os.path.isdir(dir):
	os.mkdir(dir)

for ind in subdata.index:
	filename = subdata["unified_app_name"][ind].replace('/','_')
	#print(filename)
	icon_url = subdata["icon_url"][ind]
	#print(icon_url)
	urllib.request.urlretrieve(icon_url, os.path.join(dir, filename + ".png"))	

#test code

#link = "https://is1-ssl.mzstatic.com/image/thumb/Purple115/v4/94/ee/bd/94eebdf0-07b1-402c-707f-dff8e5c0c72b/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.png/150x150bb.png"
#link = "https://play-lh.googleusercontent.com/BoAvMI_6JGNRBp_3gFaVuLuqW_4J-rjtbR_giKFoJRvZmDiPtDlnLMur9cT7sTTfeos=s48-rw"
#filename = link.split('/')[-1]
#urllib.request.urlretrieve(link, filename)

