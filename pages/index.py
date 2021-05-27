# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# dcc.Markdown reference
# https://dash.plotly.com/dash-core-components/markdown
column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            *Ever wonder how much you should be charged for an Airbnb?*
            
            #### Find a rough estimation now!

            """
        ),
        dcc.Link(dbc.Button('Calculate', color='primary'), href='/predictions')
    ],
    md=0,)
layout = dbc.Row([column1])