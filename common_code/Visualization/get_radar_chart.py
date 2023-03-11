
# This code is to get radar chart with go.Scatterpolar

import plotly.graph_objects as go
import pandas as pd
import os
import sys


# get input parameters
n = len(sys.argv)
if n != 2:
	print("1 parameter needed: you should specify input csv file with header including: name, theta") # do not use values as it is a built-in function in dataframe object
	exit
else:
	input_filename = sys.argv[1]

df = pd.read_csv(input_filename)

# set title
chart_title="Demo Radar Chart"

# get number of name
name_count = df["name"].size
#print(name_count)

# get theta array
categories = list(df.columns)[1:]
#print(categories)

# add figure trace according to name

fig = go.Figure()

for i in range(name_count):
  fig.add_trace(go.Scatterpolar(
    r=df.iloc[i,1:],
    theta=categories,
    fill='toself',
    name=df.iloc[i,0]
  ))

# customize chart layout, optional
fig.update_layout(
  title=dict(text=chart_title,x=0.5),
  colorway=['#2ca02c','#d62728','#9467bd']
)

#customize chart traces, optional
fig.update_traces(
  line=dict(color='#000000',dash="dash"),
  selector=dict(type='scatterpolar')
)

fig.show()


