import os
import dash
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash(__name__)
server = app.server

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

styles = {}

app.layout = html.Div([
    html.H1('Produção de Alimentos na América Latina'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['2015','2016', '2017']],
        value='2015'
    ),
    html.Div(id='display-value')
])
@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)
if __name__ == '__main__':
    app.run_server(debug=True)
