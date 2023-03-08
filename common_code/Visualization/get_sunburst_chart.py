# This code is to get sunburst chart for specific data set

import plotly.express as px
import plotly.graph_objects as go

'''
data = dict(
	character = ["Downloads", "Arcade", "Hypercasual", "HC - Puzzle","HC - Simulation","HC - Arcade","HC - Traversal", "HC - Action","HC - Sports",
	"Get the Girl","Brain Games","Hyper Jobs", "Toilet Games 3D","Date the Girl 3D","Draw Story","Pin Pull","Cooking Games 3D",
	"Get Married 3D", "Car Games 3D", "Drawing Games 3D", "6ix9ine Runner","Erase Her: Puzzle Story","Animal Games 3D","Granny vs Impostor",
	"Draw Story 3D","Food Games 3D","Rhythm Games","Care Bears","Goal Blitz","Mini Games Universe"],
	parent = ["", "Downloads", "Downloads", "Hypercasual", "Hypercasual", "Hypercasual", "Hypercasual", "Hypercasual", "Hypercasual",
	"HC - Puzzle","HC - Puzzle","HC - Simulation","HC - Arcade","HC - Puzzle","HC - Puzzle","HC - Puzzle","HC - Simulation",
	"HC - Puzzle", "HC - Puzzle","HC - Puzzle","HC - Traversal","HC - Puzzle","HC - Arcade","HC - Action","HC - Puzzle",
	"HC - Simulation","HC - Arcade","HC - Puzzle","HC - Sports","HC - Arcade"],
	value = [1,0.09,0.91,0.52,0.14,0.19,0.05,0.05,0.05,0.12,0.11,0.09,0.07,0.06,0.06,0.05,0.04,0.04,0.04,0.03,0.03,0.03,0.02,0.02,0.02,0.02,0.02,0.01,0.01,0.01]
)

print("size of character: %d" %(len(data['character'])))
print("size of parent: %d" %(len(data['parent'])))
print("size of value: %d" %(len(data['value'])))

fig =px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
		branchvalues="total",
)
fig.show()
'''

'''
colors=["white","yellow","green","lightgreen", "blue","darkblue","purple","grey","lightgrey"]

fig =go.Figure(go.Sunburst(
    labels=["Downloads", "Arcade", "Hypercasual", "HC - Puzzle","HC - Simulation","HC - Arcade","HC - Traversal", "HC - Action","HC - Sports",
		"Get the Girl","Brain Games","Hyper Jobs", "Toilet Games 3D","Date the Girl 3D","Draw Story","Pin Pull","Cooking Games 3D",
		"Get Married 3D", "Car Games 3D", "Drawing Games 3D", "6ix9ine Runner","Erase Her","Animal Games 3D","Granny vs Impostor",
		"Draw Story 3D","Food Games 3D","Rhythm Games","Care Bears","Goal Blitz","Mini Games Universe"],
    parents=["", "Downloads", "Downloads", "Hypercasual", "Hypercasual", "Hypercasual", "Hypercasual", "Hypercasual", "Hypercasual",
		"HC - Puzzle","HC - Puzzle","HC - Simulation","HC - Arcade","HC - Puzzle","HC - Puzzle","HC - Puzzle","HC - Simulation",
		"HC - Puzzle", "HC - Puzzle","HC - Puzzle","HC - Traversal","HC - Puzzle","HC - Arcade","HC - Action",
		"HC - Puzzle","HC - Simulation","HC - Arcade","HC - Puzzle","HC - Sports","HC - Arcade"],
    values=[1,0.1,0.9,0.57,0.15,0.12,0.03,0.02,0.01,
		0.12,0.11,0.09,0.07,0.06,0.06,0.05,0.04,
		0.04,0.04,0.03,0.03,0.03,0.02,0.02,
		0.02,0.02,0.02,0.01,0.01,0.01],
		marker = dict(colors=colors),
    branchvalues="total",
		insidetextorientation='radial',
		textinfo='label+percent entry'
))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
fig.update_layout(uniformtext=dict(minsize=10, mode='show'))
fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})

fig.show()
'''

'''
colors=["white","darkgreen","green","lightgreen"]
#colors=["#ffffff", "#51A89D", "#3273B5", "#BB77D9", 
#				"#51A89D", "#5bcfb0", "#78ccb6", "#78ccb6", "#5ebd60", "#8cbf8d", 
#				"#3285b5", "#1c9fe6", "#27c4e3"
#				]

fig=go.Figure(go.Sunburst(
#	labels = ["Downloads", "Casual", "Mid-core", "Sports & Racing", 
#						"Puzzle", "Lifestyle", "Hypercasual", "Simulation", "Tabletop", "Casual Others", 
#						"Strategy", "Shooter", "Mid-core Others"
#						],
#	parents = ["", "Downloads", "Downloads", "Downloads", 
#						"Casual", "Casual", "Casual", "Casual", "Casual", "Casual", 
#						"Mid-core", "Mid-core", "Mid-core"
#						],
#	value = [1, 0.62, 0.29, 0.9, 
#						0.12, 0.11, 0.07, 0.04, 0.04, 0.01, 
#						0.04, 0.03, 0.01
#						],
	labels = ["Downloads", "Casual", "Mid-core", "Sports & Racing"],
	parents = ["", "Downloads", "Downloads", "Downloads"],
	values = [1, 0.62, 0.29, 0.9],	
	marker = dict(colors=colors),
	branchvalues="total",
	insidetextorientation='radial',
	textinfo='label+percent entry'
))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
fig.update_layout(uniformtext=dict(minsize=10, mode='show'))
fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})

fig.show()
'''

'''
colors=["#ffffff", "#51A89D", "#3273B5", "#BB77D9", "#51A89D", "#22bda9", "#78ccb6", "#4ed99f", "#5ebd60", "#8cbf8d", "#398adb", "#1c9fe6", "#27c4e3"]

fig=go.Figure(go.Sunburst(
	labels = ["Downloads", "Casual", "Mid-core", "Sports & Racing", "Puzzle", "Lifestyle", "Hypercasual", "Simulation", "Tabletop", "Casual Others", "Strategy", "Shooter", "Mid-core Others"],
	parents = ["", "Downloads", "Downloads", "Downloads", "Casual", "Casual", "Casual", "Casual", "Casual", "Casual", "Mid-core", "Mid-core", "Mid-core"],	
	values = [1,0.63,0.28,0.09,0.19,0.17,0.11,0.07,0.06,0.03,0.13,0.12,0.03],	
	marker = dict(colors=colors),
	branchvalues="total",
	insidetextorientation='radial',
	textinfo='label+percent entry'
))

fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
fig.update_layout(uniformtext=dict(minsize=18, mode='show'))
fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})

fig.show()
'''

#'''
colors = ["#ffffff", "#3273B5", "#51A89D", "#FF9300", "#BB77D9", "#4981b8", "#398adb", "#1c9fe6", "#27c4e3", "#51A89D", "#22bda9", "#78ccb6", "#4ed99f"]

fig=go.Figure(go.Sunburst(
	labels = ["Revenue", "Mid-core", "Casual", "Casino", "Sports & Racing", "Strategy", "RPG", "Shooter", "Action", "Puzzle", "Lifestyle", "Tabletop", "Casual Others"],
	parents = ["", "Revenue", "Revenue", "Revenue", "Revenue", "Mid-core", "Mid-core", "Mid-core", "Mid-core", "Casual", "Casual", "Casual", "Casual"],	
	values = [1,0.86,0.10,0.03,0.01,0.40,0.20,0.15,0.11,0.04,0.03,0.02,0.01],	
	marker = dict(colors=colors),
	branchvalues="total",
	insidetextorientation='radial',
	textinfo='label+percent entry'
))

fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
fig.update_layout(uniformtext=dict(minsize=18, mode='show'))
fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})

fig.show()
#'''

'''
import plotly.graph_objects as go

fig =go.Figure(go.Sunburst(
    labels=[ "Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["",    "Eve",  "Eve",  "Seth", "Seth", "Eve",  "Eve",  "Awan",  "Eve" ],
    values=[  65,    14,     12,     10,     2,      6,      6,      4,       4],
    branchvalues="total",
))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig.show()
'''
