import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
from dateutil.rrule import rrule, MONTHLY
from datetime import datetime as dt, timedelta


app = dash.Dash()

current = pd.read_csv('current.csv')

# process datime
current['Date'] = pd.to_datetime(current['Date'], format='%m/%d/%Y')

start_date = current['Date'].min()
end_date = current['Date'].max()+ timedelta(1)

# months_range = [dt.strftime('%B %Y') for dt in rrule(MONTHLY, dtstart=start_date, until=end_date)]

# process team 
teams = sorted(current.columns[3:])
team_options = []
for team in teams:
    team_options.append({'label':str(team),'value':str(team)})

skill_types = current['Category'].unique()

# app setup
app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='team-option',
                options=teams,
                value=teams[0]
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.RadioItems(
                id='skill-type',
                options=[{'label': i, 'value': i} for i in skill_types],
                value = skill_types[0],
                labelStyle={'display': 'inline-block'}
            )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='radar-skill'),

    dcc.Slider(
        id='month--slider',
        min=0,
        max=end_date.month,
        value=end_date.month,
        step=None,
        marks={dt.month: dt.strftime('%b %Y') for dt in rrule(MONTHLY, dtstart=start_date, until=end_date)},
        updatemode='drag'
    )
], style={'padding':10})

@app.callback(
    Output('radar-skill', 'figure'),
    [Input('team-option', 'value'),
     Input('skill-type', 'value'),
     Input('month--slider', 'value')])
def current_graph(selected_team, skill_type,selected_date):

    sorted_current = current[(current['Date'].dt.month == selected_date)&(current['Category']==skill_type)]

    data= go.Scatterpolar(
        r = sorted_current[selected_team],
        theta = sorted_current['Skills'],
        fill ='toself'
        )
    
    layout = go.Layout(
        title='Actual Skill Map by Time',
            polar=dict(
            radialaxis=dict(
            visible=True
            ),
        ),
        showlegend=False
    )
    return {
        'data': [data],
        'layout': layout
    }


if __name__ == '__main__':
    app.run_server(debug=True)