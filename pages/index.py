# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app
from .predictions import inputs, row1, row2, row3, row4

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# dcc.Markdown reference
# https://dash.plotly.com/dash-core-components/markdown

layout = html.Div(
    [
        inputs,
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Link(dbc.Button('Calculate', color='primary'), href='/predictions')
                )
            ],
            align='center',
        )
    ], 
    style={
        'background-image':'url("/assets/background.jpg")'
    }
)
