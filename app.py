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
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("VanArt: Discover Public Art in Vancouver!",
                        style={'textAlign': 'center'}),
                width=12),
    ]),
    dbc.Row([
        dbc.Col(dcc.Dropdown(
                    id="neighbourhood-widget",
                    options=[{'label': i, 'value': i} for i in data.Neighbourhood.unique()],
                    #multi=True,
                    value=None,
                ), width=12),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="map"), width = 6),
        dbc.Col(dcc.Graph(id="hist"), width = 6)
    ]),
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody(id="art-num-card", className="card-num")), width=12),
    ]),
])

# Set up callbacks/backend
@app.callback(
    Output("map", "figure"),
    Output("hist", "figure"),
    Output("art-num-card", "children"), 
    Input("neighbourhood-widget", "value")
)
def plot_plotly(neighbourhood_input):
    # filter data according to user input
    if neighbourhood_input is None:
        # show all data
        filtered_data = data
        neighbourhood_input = "Vancouver"
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
                    "longitude":False,
                    "SiteAddress":True},
        zoom=10.5
    )

    # add mapbox style
    fig.update_layout(
        mapbox_style="open-street-map",
        margin={"r":0,"t":0,"l":0,"b":0},
    )
    
    hist = (px.histogram(filtered_data, y="Type", color="Type",
                         labels={'count':'Count'},
                         title=f"Art Types in {neighbourhood_input}",
                         hover_data={"Type":False})
            .update_yaxes(categoryorder="total descending")
            .update_layout(showlegend=False,
                           xaxis_title="Count"))
    return fig, hist, card_text

if __name__ == '__main__':
    app.run_server(debug=True)