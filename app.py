from dash import dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px

data = pd.read_csv("data/public-art.csv", delimiter=";")

# separate longitude and latitude and convert to numeric for plot
data[["latitude", "longitude"]] = data.geo_point_2d.str.split(", ", expand=True).astype(float)

# filter out missing neighborhood values
data = data[~data.Neighbourhood.isna()]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

# create layout
app.layout = html.Div([
    html.H1("VanArt: Discover Public Art in Vancouver!",
            style={'textAlign': 'center'}),
    dcc.Dropdown(
        id="neighbourhood-widget",
        options=[{'label': i, 'value': i} for i in data.Neighbourhood.unique()],
        #multi=True,
        value=None,
        style={'margin': '0px 750px 0px 250px'}
    ),
    dcc.Graph(id="map",
              style={'display': 'flex',
                     'align-items': 'center',
                     'justify-content': 'center',
                     'margin': '25px 500px 0px 500px'}
              ),
    dbc.Card(
        dbc.CardBody(id="art-num-card", className="card-num"),
        style={'margin': '25px 500px 0px 500px'}
    )
])

# Set up callbacks/backend
@app.callback(
    Output("map", "figure"),
    Output("art-num-card", "children"), 
    Input("neighbourhood-widget", "value")
)
def plot_plotly(neighbourhood_input):
    # filter data according to user input
    if neighbourhood_input is None:
        # show all data
        filtered_data = data
    else:
        # show selected neighbourhood data
        filtered_data = data[data.Neighbourhood == neighbourhood_input]
        
    num_art_pieces = len(filtered_data)
    card_text = (f"Number of art pieces in {neighbourhood_input}: \
                 {num_art_pieces}" if neighbourhood_input \
                     else f"Number of public art pieces in Vancouver: {len(data)}")

    # https://plotly.com/python/scattermapbox/
    # https://plotly.com/python/mapbox-layers/
    
    fig = px.scatter_mapbox(
        filtered_data,
        lat="latitude",
        lon="longitude",
        hover_name="Title of Work",
        hover_data={"Neighbourhood":True,
                    "YearOfInstallation":True,
                    "Type":True,
                    "latitude":False,
                    "longitude":False},
        zoom=10.5
    )

    # add mapbox style
    fig.update_layout(
        mapbox_style="open-street-map",
        margin={"r":0,"t":0,"l":0,"b":0},
    )
    return fig, card_text

if __name__ == '__main__':
    app.run_server(debug=True)