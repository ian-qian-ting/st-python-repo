# This code is to get sunburst chart using graph_objects

import plotly.graph_objects as go
import pandas as pd
import os
import sys

# get input parameters
n = len(sys.argv)
if n != 2:
	print("1 parameter needed: you should specify input csv file with header including: ids(optional, each should be unique string), labels, parents(should be aligned with ids if ids provided), data_values") # do not use values as it is a built-in function in dataframe object
	exit
else:
	input_filename = sys.argv[1]

df = pd.read_csv(input_filename)

# set title
chart_title="Demo Sunburst Chart"

#check if ids provided in dataframe
if 'ids' in df.columns:
	print("the dataframe has ids")
	fig = go.Figure(go.Sunburst(
		ids = df.ids,
		labels = df.labels,
		parents = df.parents,
		values = df.data_values,
		branchvalues="total",
		insidetextorientation='radial',
		textinfo='label+percent entry'
	))
else:
	print("the dataframe doesn't have ids, use labels instead")
	fig = go.Figure(go.Sunburst(
		labels = df.labels,
		parents = df.parents,
		values = df.data_values,
		branchvalues="total",
		insidetextorientation='radial',
		textinfo='label+percent entry'
	))

#custimize chart layout, optional
fig.update_layout(title=dict(text=chart_title,x=0.5),
	margin=dict(t=80,l=80,r=80,b=80),
	uniformtext=dict(minsize=10, mode='show')
)

#custimize chart traces, optional


#show figures
fig.show()

