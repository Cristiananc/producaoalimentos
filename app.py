import os
import json
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_cytoscape as cyto

app = dash.Dash(__name__)
app.title = "Producao alimentos"
server = app.server

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

with open('producaoalimentos.json', 'r') as f:
    data = json.loads(f.read())
    
##https://github.com/plotly/dash-cytoscape/blob/master/demos/data/edge-types/cy-style.json
with open('cy-style.json') as f:
    stylesheet = json.loads(f.read())


styles = {
    'container': {
        'position': 'fixed',
        'display': 'flex',
        'flex-direction': 'column',
        'height': '100%',
        'width': '100%'
    },
    'cy-container': {
        'flex': '1',
        'position': 'relative'
    },
    'cytoscape': {
        'position': 'absolute',
        'width': '100%',
        'height': '100%',
        'z-index': 999
    }
}

app.layout = html.Div([
    html.H2('Produção de Grãos e Cereais na América Latina'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['2015','2016', '2017']],
        value='2015'
    ),
    html.Div(id='display-value'),
    html.Div(className='cy-container', style=styles['cy-container'], children=[
        cyto.Cytoscape(
            id='cytoscape',
            elements= data['elements']['nodes'] + data['elements']['edges'],
            stylesheet=stylesheet,
            style=styles['cytoscape'],
            layout={
                'name': 'cose',
                'idealEdgeLength': 100,
                'nodeOverlap': 20,
                'refresh': 20,
                'fit': True,
                'padding': 30,
                'randomize': False,
                'componentSpacing': 100,
                'nodeRepulsion': 400000,
                'edgeElasticity': 100,
                'nestingFactor': 5,
                'gravity': 80,
                'numIter': 1000,
                'initialTemp': 200,
                'coolingFactor': 0.95,
                'minTemp': 1.0
            },
            responsive=True
        )
    ])
])
@app.callback(Output('display-value', 'children'),
              [Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
