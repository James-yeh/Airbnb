import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Airbnb Price Predictor"),

    dcc.Dropdown(id="room_type",
                 options=[
                     {"label": "Entire home/apt", "value": 99999},
                     {"label": "Private room", "value": 10000},
                     {"label": "Shared room","value": 4}],
                 multi=False,
                 value=4,
                 style={'width': "60%"}
                 ),

    html.Div(id='output_container', children=[]),
    dcc.Checklist(
        options=[
            {'label': 'Air conditioning', 'value': 'air_conditioning'},
            {'label': 'Kitchen', 'value': 'kitchen'},
            {'label': 'Heating', 'value': 'heating'},
            {'label': 'Essentials', 'value': 'essentials'},
            {'label': 'Hair dryer', 'value': 'hair_dryer'},
            {'label': 'Iron', 'value': 'iron'},
            {'label': 'Shampoo', 'value': 'shampoo'},
            {'label': 'Hangers', 'value': 'hangers'},
            {'label': 'Fire extinguisher', 'value': 'fire_extinguisher'},
            {'label': 'First aid kit', 'value': 'first_aid_kit'},
            {'label': 'Indoor fireplace', 'value': 'indoor_fireplace'},
            {'label': 'TV', 'value': 'tv'},
            {'label': 'Cable TV', 'value': 'cable_tv'}
        ],
    )
])


# ------------------------------------------------------------------------------
# callback
@app.callback(
    Output(component_id='output_container',component_property='children'),
    Input(component_id="room_type",component_property='value'),
) # TODO ^ inputs for all the booleans and add the final not boolean choices

def update_price(room):
    print(type(room),room)
    container = room

if __name__ == '__main__':
    app.run_server(debug=True)
