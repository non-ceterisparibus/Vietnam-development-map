
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# Plot in browser (recommended)
import plotly.io as pio
pio.renderers.default = 'browser'

def plot_animation_frame_vietnamstate(df, geo_json, color_data, title):
    """
    Function to plot choropleth interactive plot by year. 
        Args:
        -------
            df(DataFrame): Dataframe containing the data to be plotted.
            color_data(column): DataFrame column name of the coloring variable.
            geo_json 
        Returns:
        ---------
            plot.choropleth
    """
    fig = px.choropleth(
        df,
        geojson = geo_json,
        locations ="Code",
        featureidkey="properties.Code",
        animation_frame = "year",
        color = color_data,
        range_color=(min(df[color_data]), max(df[color_data])),
        hover_name = "Name",
        # hover_data = [hover_data],
        title = title,
    )
    fig.update_geos(fitbounds = "locations", visible=False)
    fig.show()

def add_subplot(geo,df,cat,i,rows, cols):
    
    fig.add_trace(go.Choroplethmapbox(
        geojson = geo,
        featureidkey = "properties.Code",
        locations = df["Code"],
        z = df[cat],
        zmin =  20,
        zmax = 4000,
        hovertext = 'State: ' + df["Name_EN"] + '<br>' + cat + ': '+df[cat].astype('str'),
        colorscale='Bluered',
        # showscale=True,
        # name = '{}'.format('Wages_agri')
                ),
    row = i//rows+1, 
    col = i%cols+1
    )

# if __name__ == '__main__':
