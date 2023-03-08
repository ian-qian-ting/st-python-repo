
# This code is to get radar chart with go.Scatterpolar

import plotly.graph_objects as go

# Game Class downloads
"""
categories = ['Casual', 'Mid-core', 'Sports & Racing', 'Casino']

fig = go.Figure()

# US
fig.add_trace(go.Scatterpolar(
      r=[0.82, 0.11, 0.04, 0.03],
      theta=categories,
      fill='toself',
      name='US'
))

# EUROPE
fig.add_trace(go.Scatterpolar(
      r=[0.81, 0.13, 0.05, 0.01],
      theta=categories,
      fill='toself',
      name='Europe'
))

# SEA
fig.add_trace(go.Scatterpolar(
      r=[0.75, 0.16, 0.06, 0.03],
      theta=categories,
      fill='toself',
      name='SEA'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
			tickfont=dict(
				size=16
			),
      visible=True,
      range=[0, 1]
    ),
		angularaxis=dict(
			visible=True
		)
		),
#	paper_bgcolor="white",
# not working for radar, use polar_bgcolor instead
#	plot_bgcolor="white",
#	polar_bgcolor="white",
#	polar_radialaxis_gridcolor="gray",
#  polar_angularaxis_gridcolor="gray",
#	title="Game Class Contribution by Downloads",
  template="plotly_white",
	margin=dict(
		l=120,
		r=120
	),
	width=900,
	height=600,
  showlegend=True,
	#legend=dict(
	#	font=dict(
	#		size=32
	#	)
	#)
	font=dict(
		size=24
	)
)

fig.show()
"""

# Game Class revenue
"""
categories = ['Casual', 'Mid-core', 'Sports & Racing', 'Casino']

fig = go.Figure()

# US
fig.add_trace(go.Scatterpolar(
      r=[0.40, 0.38, 0.03, 0.19],
      theta=categories,
      fill='toself',
      name='US'
))

# EUROPE
fig.add_trace(go.Scatterpolar(
      r=[0.39, 0.46, 0.05, 0.11],
      theta=categories,
      fill='toself',
      name='Europe'
))

# SEA
fig.add_trace(go.Scatterpolar(
      r=[0.22, 0.65, 0.06, 0.08],
      theta=categories,
      fill='toself',
      name='SEA'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
			tickfont=dict(
				size=16
			),
      visible=True,
      range=[0, 0.8]
    ),
		angularaxis=dict(
			visible=True
		)
		),
#	paper_bgcolor="white",
# not working for radar, use polar_bgcolor instead
#	plot_bgcolor="white",
#	polar_bgcolor="white",
#	polar_radialaxis_gridcolor="gray",
# polar_angularaxis_gridcolor="gray",
  template="plotly_white",
	title=dict(
		text="Game Class",
		font=dict(
			color="#4BA49A"
		),
		x=0.5,
		xanchor="center"
	),
	margin=dict(
		l=120,
		r=120
	),
	width=900,
	height=600,
  showlegend=True,
	font=dict(
		size=24
	)
)

fig.show()
"""

# Game Genre downloads
"""
categories = ['Puzzle', 'Casino', 'Strategy', 'RPG', 'Simulation', 'Other']

fig = go.Figure()

# US
fig.add_trace(go.Scatterpolar(
      r=[0.15, 0.03, 0.04, 0.02, 0.08, 0.68],
      theta=categories,
      fill='toself',
      name='US'
))

# EUROPE
fig.add_trace(go.Scatterpolar(
      r=[0.12, 0.01, 0.04, 0.02, 0.11, 0.70],
      theta=categories,
      fill='toself',
      name='Europe'
))

# SEA
fig.add_trace(go.Scatterpolar(
      r=[0.08, 0.03, 0.05, 0.02, 0.12, 0.70],
      theta=categories,
      fill='toself',
      name='SEA'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 0.8]
    ),
		angularaxis=dict(
			visible=True
		)
		),
#	paper_bgcolor="white",
# not working for radar, use polar_bgcolor instead
#	plot_bgcolor="white",
#	polar_bgcolor="white",
#	polar_radialaxis_gridcolor="gray",
#  polar_angularaxis_gridcolor="gray",
#	title="Game Class Contribution by Downloads",
  template="plotly_white",
	margin=dict(
		l=110,
		r=110
	),
	width=600,
	height=600,
  showlegend=True
)

fig.show()
#"""

# Game Genre revenue
"""
categories = ['Puzzle', 'Casino', 'Strategy', 'RPG', 'Simulation', 'Other']

fig = go.Figure()

# US
fig.add_trace(go.Scatterpolar(
      r=[0.21, 0.19, 0.18, 0.11, 0.09, 0.22],
      theta=categories,
      fill='toself',
      name='US'
))

# EUROPE
fig.add_trace(go.Scatterpolar(
      r=[0.19, 0.11, 0.24, 0.12, 0.11, 0.24],
      theta=categories,
      fill='toself',
      name='Europe'
))

# SEA
fig.add_trace(go.Scatterpolar(
      r=[0.06, 0.08, 0.27, 0.18, 0.08, 0.33],
      theta=categories,
      fill='toself',
      name='SEA'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
			tickfont=dict(
				size=16
			),
      visible=True,
      range=[0, 0.5]
    ),
		angularaxis=dict(
			visible=True
		)
		),
#	paper_bgcolor="white",
# not working for radar, use polar_bgcolor instead
#	plot_bgcolor="white",
#	polar_bgcolor="white",
#	polar_radialaxis_gridcolor="gray",
#  polar_angularaxis_gridcolor="gray",
#	title="Game Class Contribution by Downloads",
  template="plotly_white",
	title=dict(
		text="Game Genre",
		font=dict(
			color="#4BA49A"
		),
		x=0.5,
		xanchor="center"
	),
	margin=dict(
		l=120,
		r=120
	),
	width=900,
	height=600,
  showlegend=True,
		font=dict(
		size=24
	)
)

fig.show()
"""

# Game Setting downloads
"""
categories = ['Modern', 'High Fantasy', 'Cartoon Fantasy', 'Sci-Fi', 'Historical']

fig = go.Figure()

# US
fig.add_trace(go.Scatterpolar(
      r=[0.25, 0.05, 0.08, 0.05, 0.02],
      theta=categories,
      fill='toself',
      name='US'
))

# EUROPE
fig.add_trace(go.Scatterpolar(
      r=[0.28, 0.05, 0.09, 0.05, 0.02],
      theta=categories,
      fill='toself',
      name='Europe'
))

# SEA
fig.add_trace(go.Scatterpolar(
      r=[0.28, 0.05, 0.11, 0.07, 0.01],
      theta=categories,
      fill='toself',
      name='SEA'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 0.3]
    ),
		angularaxis=dict(
			visible=True
		)
		),
#	paper_bgcolor="white",
# not working for radar, use polar_bgcolor instead
#	plot_bgcolor="white",
#	polar_bgcolor="white",
#	polar_radialaxis_gridcolor="gray",
#  polar_angularaxis_gridcolor="gray",
#	title="Game Class Contribution by Downloads",
  template="plotly_white",
	margin=dict(
		l=110,
		r=110
	),
	width=600,
	height=600,
  showlegend=True
)

fig.show()
"""

# Game Setting revenue
"""
categories = ['Modern', 'High Fantasy', 'Cartoon Fantasy', 'Sci-Fi', 'Historical']

fig = go.Figure()

# US
fig.add_trace(go.Scatterpolar(
      r=[0.25, 0.21, 0.12, 0.09, 0.06],
      theta=categories,
      fill='toself',
      name='US'
))

# EUROPE
fig.add_trace(go.Scatterpolar(
      r=[0.30, 0.27, 0.09, 0.09, 0.08],
      theta=categories,
      fill='toself',
      name='Europe'
))

# SEA
fig.add_trace(go.Scatterpolar(
      r=[0.25, 0.37, 0.05, 0.08, 0.09],
      theta=categories,
      fill='toself',
      name='SEA'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
			tickfont=dict(
				size=16
			),
      visible=True,
      range=[0, 0.5]
    ),
		angularaxis=dict(
			visible=True
		)
		),
#	paper_bgcolor="white",
# not working for radar, use polar_bgcolor instead
#	plot_bgcolor="white",
#	polar_bgcolor="white",
#	polar_radialaxis_gridcolor="gray",
#  polar_angularaxis_gridcolor="gray",
#	title="Game Class Contribution by Downloads",
  template="plotly_white",
	title=dict(
		text="Game Setting",
		font=dict(
			color="#4BA49A"
		),
		x=0.5,
		xanchor="center"
	),
	margin=dict(
		l=120,
		r=120
	),
	width=900,
	height=600,
  showlegend=True,
	font=dict(
		size=24
	)
)

fig.show()
"""

# Game Art Style downloads
"""
categories = ['Cartoon', 'Realistic', 'Anime', 'Other']

fig = go.Figure()

# US
fig.add_trace(go.Scatterpolar(
      r=[0.39, 0.18, 0.02, 0.42],
      theta=categories,
      fill='toself',
      name='US'
))

# EUROPE
fig.add_trace(go.Scatterpolar(
      r=[0.41, 0.20, 0.01, 0.38],
      theta=categories,
      fill='toself',
      name='Europe'
))

# SEA
fig.add_trace(go.Scatterpolar(
      r=[0.42, 0.22, 0.03, 0.33],
      theta=categories,
      fill='toself',
      name='SEA'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 0.5]
    ),
		angularaxis=dict(
			visible=True
		)
		),
#	paper_bgcolor="white",
# not working for radar, use polar_bgcolor instead
#	plot_bgcolor="white",
#	polar_bgcolor="white",
#	polar_radialaxis_gridcolor="gray",
#  polar_angularaxis_gridcolor="gray",
#	title="Game Class Contribution by Downloads",
  template="plotly_white",
	margin=dict(
		l=110,
		r=110
	),
	width=600,
	height=600,
  showlegend=True
)

fig.show()
"""

# Game Art Style revenue
#"""
categories = ['Cartoon', 'Realistic', 'Anime', 'Other']

fig = go.Figure()

# US
fig.add_trace(go.Scatterpolar(
      r=[0.58, 0.28, 0.07, 0.07],
      theta=categories,
      fill='toself',
      name='US'
))

# EUROPE
fig.add_trace(go.Scatterpolar(
      r=[0.53, 0.34, 0.07, 0.06],
      theta=categories,
      fill='toself',
      name='Europe'
))

# SEA
fig.add_trace(go.Scatterpolar(
      r=[0.30, 0.48, 0.17, 0.05],
      theta=categories,
      fill='toself',
      name='SEA'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
			tickfont=dict(
				size=16
			),
      visible=True,
      range=[0, 0.6]
    ),
		angularaxis=dict(
			visible=True
		)
		),
#	paper_bgcolor="white",
# not working for radar, use polar_bgcolor instead
#	plot_bgcolor="white",
#	polar_bgcolor="white",
#	polar_radialaxis_gridcolor="gray",
#  polar_angularaxis_gridcolor="gray",
#	title="Game Class Contribution by Downloads",
  template="plotly_white",
	title=dict(
		text="Game Art Style",
		font=dict(
			color="#4BA49A"
		),
		x=0.5,
		xanchor="center"
	),
	margin=dict(
		l=120,
		r=120
	),
	width=900,
	height=600,
  showlegend=True,
	font=dict(
		size=24
	)
)

fig.show()
#"""
