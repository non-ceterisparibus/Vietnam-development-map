#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# Launch the application:
app = dash.Dash()

# Create a DataFrame from the .csv file:
dt = pd.read_csv("faithful.csv")


# Create a Dash layout that contains a Graph component:
app.layout = html.Div([
    dcc.Graph(
        id='graph1',
        figure={
            'data': [
                go.Scatter(
                    x = dt['eruptions'],
                    y = dt['waiting'],
                    mode = ' markers',
                    marker ={
                        'size': 12,
                        'color': 'rgb(51,204,153)',
                        'symbol': 'pentagon',
                        'line': {'width': 2}
                        }
    
                )
            ],
            'layout': go.Layout(
                    title= " Eruption and waiting time",
                    xaxis = {'title': "eruption"},
                    yaxis = {'title': "waiting time"},
                    hovermode='closest'
            )
        }
    
    )
])



# Add the server clause:

if __name__ == '__main__':
    app.run_server()
