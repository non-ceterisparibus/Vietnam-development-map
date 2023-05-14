import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    html.Label('Select date range:'),
    dcc.DatePickerRange(
        id='date-range',
        min_date_allowed='2021-01-01',
        max_date_allowed='2023-12-31',
        start_date='2023-03-01',
        end_date='2023-06-30'
    ),
    html.Br(),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date')])
def update_output(start_date, end_date):
    return f'You have selected {start_date} to {end_date}'

if __name__ == '__main__':
    app.run_server()
