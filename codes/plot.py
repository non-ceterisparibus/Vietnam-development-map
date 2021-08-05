
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
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

# if __name__ == '__main__':
