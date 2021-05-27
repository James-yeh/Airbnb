# Import libraries
import dash
import dash_bootstrap_components as dbc

# Bootstrap index for theme selection
"""
Go to https://bootswatch.com/ to preview these Bootswatch themes:
dbc.themes.BOOTSTRAP
dbc.themes.CERULEAN
dbc.themes.COSMO
dbc.themes.CYBORG
dbc.themes.DARKLY
dbc.themes.FLATLY
dbc.themes.JOURNAL
dbc.themes.LITERA
dbc.themes.LUMEN
dbc.themes.LUX
dbc.themes.MATERIA
dbc.themes.MINTY
dbc.themes.PULSE
dbc.themes.SANDSTONE
dbc.themes.SIMPLEX
dbc.themes.SKETCHY
dbc.themes.SLATE
dbc.themes.SOLAR
dbc.themes.SPACELAB
dbc.themes.SUPERHERO
dbc.themes.UNITED
dbc.themes.YETI
"""

# Reference to Plotly Workshop 
external_stylesheets = [
    dbc.themes.LUX, # Bootswatch theme
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css', # for social media icons
]

meta_tags=[
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
# URL-Support see https://dash.plotly.com/urls
app.config.suppress_callback_exceptions = True
# Browser title bar
app.title = 'AirBnb Optimal Price' 
server = app.server
