import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os
import sys

# get input parameters
n = len(sys.argv)
if n != 2:
	print("1 parameter needed: you should specify input csv file with header including: labels, metrics, parents") # do not use values as it is a built-in function in dataframe object
	exit
else:
	input_filename = sys.argv[1]

df = pd.read_csv(input_filename)
#print(df.labels)

fig = go.Figure()

fig.add_trace(go.Treemap(
    #ids = df.ids,
    labels = df.labels,
    parents = df.parents,
		values = df.metrics,
		branchvalues='total',
    maxdepth=3,
		textposition="middle center",
		textfont=dict(size=21),
    root_color="#007B76"
))

fig.update_layout(
	treemapcolorway = ["#4BA49A", "#6ACA98", "#72DBAA"],
	#width=1600,
	#height=1200,
	margin = dict(t=10, l=0, r=0, b=0)
)

fig.show()

