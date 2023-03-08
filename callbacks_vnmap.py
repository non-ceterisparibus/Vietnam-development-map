import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import json

app = dash.Dash()

# Import csv and geojson
income_df = pd.read_csv("geodata/thunhapbinhquan.csv")
categories = sorted(income_df.columns[2:])

#Vietnam map
vietnam_geo = json.load(open("geodata/vietnam_state.geojson","r"))

cat_options = []
for cat in categories:
    cat_options.append({'label':str(cat[7:]),'value':cat})

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='income-picker',
                 options=cat_options,
                 value=cat_options[0])
])

@app.callback(Output('graph', 'figure'),
              [Input('income-picker', 'value')])
def update_graph(selected_income):
    trace = go.Choroplethmapbox(
        geojson = vietnam_geo,
        featureidkey= 'properties.Code',
        locations = income_df["Code"],
        z= income_df.loc[0:, selected_income],
        hovertext = 'Province: ' + income_df['Name_EN'],
        colorscale ='viridis',
        marker_opacity=0.9,
        marker_line_width=0.9,
        showscale=True
        )
    layout = go.Layout(
        title='Income by provinces',
        height=900,  # set the height of the chart to 500 pixels
        width=600,   # set the width of the chart to 800 pixels
        mapbox=dict(
            style='white-bg',  # replace with your own mapbox style
            center=dict(
                lat=17,  # replace with your own latitude
                lon=106  # replace with your own longitude
            ),
            zoom=4.5,  # replace with your own zoom level
        ),
)
    return {
        'data': [trace],
        'layout': layout
    }

    
if __name__ == '__main__':
    app.run_server()
