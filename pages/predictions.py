# Import libraries
import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load

# Import application
from app import app

# Reference https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
pipeline = load('assets/pipeline.joblib')
