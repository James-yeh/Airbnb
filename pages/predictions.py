# Import libraries
import pandas as pd
import numpy as np
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load

# Import application
from app import app

model = load('assets/pipeline2.joblib')

@app.callback(
    Output('prediction-values', 'children'),
    [
        Input('room_type', 'value'),
        Input('property_type', 'value'),
        Input('accomodates', 'value'),
        Input('beds', 'value'),
        Input('bedrooms', 'value'),
        Input('host_response_time', 'value'),
        Input('is_superhost', 'value'),
        Input('host_id_verify', 'value'),
    ]
)

# Reference https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

def predict(
    room_type, property_type, accomodates, beds, bedrooms,
    host_response_time, host_is_superhost, host_identity_verified
    ):
    df = pd.DataFrame(
        columns = 
            [
            'room_type', 'property_type', 'accomodates', 'beds',
            'bedrooms', 'host_response_time', 'is_superhost', 'host_id_verify'
            ],
        data = 
            [
                [room_type, property_type, accomodates, beds, bedrooms,
                host_response_time, host_is_superhost, host_identity_verified]
            ]
    )
    y_pred = model.predict(df)
    results = np.round(np.exp(y_pred), 2)
    return print("$", results)


# Layout
row1 = dbc.Col(
    children=[
    html.Div(id='prediction-values', className='lead')
    ]
)

row2 = dbc.Container(
    [
       dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label('Room Type'),
                        dcc.Dropdown(
                            id='room_type',
                            options=[
                                {"label": "Entire home/apt", "value": "Entire home/apt"},
                                {"label": "Private room", "value": "Private room"},
                                {"label": "Shared room","value": "Shared room"}
                                ],
                            multi=False
                        )
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Label('Property Type'),
                        dcc.Dropdown(
                            id='property_type',
                            options=[
                                {"label": "Entire apartment", "value": "Entire apartment"},
                                {"label": "Private room in apartment", "value": "Private room in apartment"},
                                {"label": "Entire condominium","value": "Entire condominium"},
                                {"label": "Private room in house ","value": "Private room in house "},
                                {"label": "Entire house","value": "Entire house"},
                                {"label": "Private room in condominium","value": "Private room in condominium"},
                                {"label": "Entire guest suite","value": "Entire guest suite"},
                                {"label": "Room in boutique hotel","value": "Room in boutique hotel"},
                                {"label": "Entire serviced apartment","value": "Entire serviced apartment"},
                                {"label": "Entire loft","value": "Entire loft"},
                                {"label": "Entire townhouse","value": "Entire townhouse"},
                                {"label": "Private room in townhouse","value": "Private room in townhouse"},
                                {"label": "Private room in bungalow","value": "Private room in bungalow"},
                                {"label": "Entire guesthouse","value": "Entire guesthouse"},
                                {"label": "Shared room in apartment","value": "Shared room in apartment"},
                                {"label": "Room in hotel","value": "Room in hotel"},
                                {"label": "Private room in loft","value": "Private room in loft"},
                                {"label": "Shared room in house","value": "Shared room in house"},
                                {"label": "Private room in bed and breakfast","value": "Private room in bed and breakfast"},
                                {"label": "Private room in guest suite","value": "Private room in guest suite"},
                                {"label": "Entire bungalow","value": "Entire bungalow"},
                                {"label": "Shared room in condominium","value": "Shared room in condominium"},
                                {"label": "Room in serviced apartment","value": "Room in serviced apartment"},
                                {"label": "Room in bed and breakfast","value": "Room in bed and breakfast"},
                                {"label": "Private room in guesthouse","value": "Private room in guesthouse"},
                                {"label": "Room in hostel","value": "Room in hostel"},
                                {"label": "Boat","value": "Boat"},
                                {"label": "Private room in cottage","value": "Private room in cottage"},
                                {"label": "Entire cottage","value": "Entire cottage"},
                                {"label": "Private room in hostel","value": "Private room in hostel"},
                                {"label": "Private room in tiny house","value": "Private room in tiny house"},
                                {"label": "Shared room in hostel","value": "Shared room in hostel"},
                                {"label": "Room in aparthotel","value": "Room in aparthotel"},
                                {"label": "Tiny house","value": "Tiny house"},
                                {"label": "Private room","value": "Private room"},
                                {"label": "Private room in serviced apartment","value": "Private room in serviced apartment"},
                                {"label": "Shared room in cave","value": "Shared room in cave"},
                                {"label": "Entire home/apt","value": "Entire home/apt"},
                                {"label": "Private room in villa","value": "Private room in villa"},
                                {"label": "Shared room","value": "Shared room"},
                                {"label": "Entire villa","value": "Entire villa"},
                                {"label": "Campsite","value": "Campsite"},
                                {"label": "Shared room in serviced apartment","value": "Shared room in serviced apartment"},
                                {"label": "Shared room in loft","value": "Shared room in loft"},
                                {"label": "Private room in cabin","value": "Private room in cabin"},
                                {"label": "Shared room in bungalow","value": "Shared room in bungalow"},
                                {"label": "Private room in farm stay","value": "Private room in farm stay"},
                                {"label": "Entire place ","value": "Entire place "}
                                    ],
                            multi=False,
                            placeholder="Type",
                        )
                    ]
                ),
            ]
        ),
    ],
)   

row3 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                    dbc.Label('Accomodates'),
                    dcc.Slider(
                        id='accomodates',
                        min=1,
                        max=16,
                        step=1,
                        marks={i: '{}'.format(i) for i in range(1,17,1)},
                        className='mb-5'
                        )
                    ]      
                )    
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                    dbc.Label('Beds'),
                    dcc.Slider(
                        id='beds',
                        min=1,
                        max=16,
                        step=1,
                        marks={i: '{}'.format(i) for i in range(1,17,1)},
                        className='mb-5'
                        )
                    ]      
                )    
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                    dbc.Label('Bedrooms'),
                    dcc.Slider(
                        id='bedrooms',
                        min=1,
                        max=16,
                        step=1,
                        marks={i: '{}'.format(i) for i in range(1,17,1)},
                        className='mb-5'
                        )
                    ]      
                )    
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label('Amenities'),
                        dcc.Dropdown(
                            id='amenities',
                            options=
                                [
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
                            multi=True,
                        )
                    ]  
                )
            ]
        ),  
    ]
)

row4 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Label("Host's Response Time"),
                        dcc.Dropdown(
                            id='host_response_time',
                            options=
                            [
                                {'label': 'within an hour', 'value': 'within an hour '},
                                {'label': 'within a few hours', 'value': 'within a few hours'},
                                {'label': 'within a day ', 'value': 'within a day'},
                                {'label': 'a few days or more', 'value': 'a few days or more'}
                            ]
                        )
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Label('Host is superhost?'),
                        dcc.Dropdown(
                            id='is_superhost',
                            options=
                            [
                                {'label': 'Yes', 'value':'1.0'},
                                {'label': 'No', 'value':'0.0'}
                            ]
                        )
                    ]
                ),
                dbc.Col(
                    [
                        dbc.Label('Host identity verified?'),
                        dcc.Dropdown(
                            id='host_id_verify',
                            options=
                            [
                                {'label': 'Yes', 'value':'1.0'},
                                {'label': 'No', 'value':'0.0'}
                            ]
                        )
                    ]
                ),
            ]
        )
    ]
)

inputs = dbc.Container(
    [
    dbc.Row(row1),
    dbc.Row(row2),
    html.Hr(),
    dbc.Row(row3),
    html.Hr(),
    dbc.Row(row4)
    ]
)

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            #Your calculated price is:#

            """
        ),
    ],
    md=0
)

layout = dbc.Row([column1])