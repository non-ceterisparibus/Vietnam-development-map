
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Plot in browser (recommended)
import plotly.io as pio
pio.renderers.default = 'browser'

def plot_animation_frame_vietnamstate(df,geo_json, color, hover_data, title):
    """
    Function to plot choropleth interactive plot by year. 
        Args:
        -------
            df(DataFrame): Dataframe containing the data to be plotted.
            color(column): DataFrame column name of the coloring variable.
            hover_data(column): DataFrame column name of the outcome variable.
            
        Returns:
        ---------
            plot.choropleth

    """
    fig = px.choropleth(
        df,
        locations ="Code",
        animation_frame = "year",
        geojson = geo_json,
        color = color,
        range_color=(min(df[color]), max(df[color])),
        hover_name = "Name",
        hover_data = [hover_data],
        title = title,
    )
    fig.update_geos(fitbounds = "locations", visible=False)
    fig.show()

# if __name__ == '__main__':
