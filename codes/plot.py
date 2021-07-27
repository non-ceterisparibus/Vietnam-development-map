# Plot Choropleth Maps

import plotly.express as px

def plotmap(df,loc,frame,your_geojson, your_color, your_hover_name, your_title):
    """
    
    """
    fig = px.choropleth(
        df,
        locations =loc,
        animation_frame = frame,
        geojson = your_geojson,
        color =your_color,
        hover_name = your_hover_name,
        title =your_title,
        )
    fig.update_geos(fitbounds ="locations", visible=False)
    fig.show()