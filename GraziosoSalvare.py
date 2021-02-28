from jupyter_plotly_dash import JupyterDash

import base64

import dash
import dash_leaflet as dl
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import dash_table
from dash.dependencies import Input, Output


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pymongo import MongoClient

from CRUD import AnimalShelter


###########################
# Data Manipulation / Model
###########################

username = "aacuser"
password = "Polkmn123"
shelter = AnimalShelter(username, password)


# class read method must support return of cursor object and accept projection json input
df = pd.DataFrame.from_records(shelter.read_all({}))


#########################
# Dashboard Layout / View
#########################
app = JupyterDash('Project2')

#Declare Grazioso Salvare’s logo
image_filename = 'Grazioso Salvare Logo.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

app.layout = html.Div([
    html.Div(id='hidden-div', style={'display':'none'}),
    html.Center(
        children=[
            html.B(html.H1('Grazioso Salvare Animal Center Outcomes by Anthony Quijano')),
            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),
                     style={'width': '100px', 'height': '100px'}),    
        ]
    ),
    html.Hr(),
    html.P("Min Age (years):"),
    dcc.Dropdown(id='min-age',
                 clearable=False,
                 options=[{'value': x, 'label': x}
                         for x in [0, 1, 2, 3, 4, 5]]), # user can select age of the animal in years
    dash_table.DataTable(
        id='datatable-id',
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in df.columns
        ],
        data=df.to_dict('records'),
        editable=False,
        filter_action="native",
        page_size=20,
        sort_action="native",
        row_selectable="single"
    ),
        html.Div(className='row',
            id='test-output'),
    html.Br(),
    html.Hr(),
    html.Div(className='row',
         style={'display' : 'flex'},
             children=[
        html.Div(
            id='graph-id',
            className='col s12 m6',

            ),
        html.Div(
            id='map-id',
            className='col s12 m6',
            )
        ]),

])

#############################################
# Interaction Between Components / Controller
#############################################
#This callback will highlight a row on the data table when the user selects it
@app.callback(
    Output('datatable-id', 'style_data_conditional'),
    [Input('datatable-id', 'selected_columns')]
)
def update_styles(selected_columns):
    return [{
        'if': { 'column_id': i },
        'background_color': '#D2F3FF'
    } for i in selected_columns]

# Handles the change of the age filter
@app.callback(
    Output('datatable-id', 'data'),
    [Input('min-age', 'value')]
)
def age_change(minAge):
    dff = pd.DataFrame.from_records(shelter.read_all({
        'age_upon_outcome_in_weeks': {
            '$gte': minAge * 52 # 52 weeks in a year
        }
    }))
    return dff.to_dict('records')

@app.callback(
    Output('graph-id', "children"),
    [Input('datatable-id', "derived_viewport_data")])
def update_graphs(viewData):
    if viewData == None:
        return []
    dff = pd.DataFrame.from_dict(viewData)
    return [
       dcc.Graph(            
           figure = px.pie(dff, names='breed', title="Breed Totals")
       )    
    ]

@app.callback(
    Output('map-id', "children"),
    [Input('datatable-id', "selected_rows"),
     Input('datatable-id', "derived_viewport_data")])
def update_map(rows, viewData):
    dff = pd.DataFrame.from_dict(viewData)
    # get the lat and lon of the selected row
    lat = dff.iat[rows[0], 13]
    lon = dff.iat[rows[0], 14]
    return [
        dl.Map(style={'width': '1000px', 'height': '500px'}, center=[30.75,-97.48], zoom=10, children=[
            dl.TileLayer(id="base-layer-id"),
            # Marker with tool tip and popup
            dl.Marker(position=[lat, lon], children=[
                dl.Tooltip(dff.iat[rows[0], 4]),
                dl.Popup([
                    html.H1("Animal Name"),
                    html.P(dff.iat[rows[0], 9])
                ])
            ])
        ])
    ]
    

app