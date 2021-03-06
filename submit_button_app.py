import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6('How a button, rather than input values, trigger the callback function'),
    html.Div([
        dcc.Input(id='input-1-state', value='Income', type='text'),
        dcc.Input(id='input-2-state', value='KES', type='text'),
        html.Button(id='button-state', children='Submit', n_clicks=0),
    ]),
    html.Div(id='output-state')
])


@app.callback(
    Output('output-state', 'children'),
    Input('button-state', 'n_clicks'),
    State('input-1-state', 'value'),
    State('input-2-state', 'value')
)
def update_output(n_clicks, input1, input2):
    return u'''
        The button has been pressed {} times,
        Input 1 is {},
        Input 2 is {}
    '''.format(n_clicks, input1, input2)


if __name__ == '__main__':
    app.run_server(debug=True)
