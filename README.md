# Plotting Vietnam Development Map

> This is my personal project that I use plotly to analyse and visualize data of Vietnam's regions with interactive map to improve and inform constructive dialogue and decision making for sustainable and equitable development.

## Content
    * 1 General Geography
        1.1 Soil Map
        1.2 Road and Railway Network
    * 2. Poverty in Vietnam
        2.1 The percentage of malnourished children under 5 in 2018 by locality
        2.2 Proportion of poor households by region in Vietnam from 1998 to 2016
    * 3. Vietnam Economy
        3.1 Employment
        3.2 The Aquaculture Production of Vietnam from 2013 to 2018 by Provinces
        3.3 Various sources of income by provinces  in 2018 in Vietnam

<img src="figures/vietnam_physio-2001.png" width=300>

## Install environment

```bash
conda env create -f environment.yml
```

## Visualization packages

### [Plotly](https://plotly.com/python/)
Plotly is a technical computing company that develops online data analytics and visualization tools. Plotly provides online graphing, analytics, and statistics tools for individuals and collaboration, as well as scientific graphing libraries for Python, R, MATLAB, Perl, Julia, Arduino, and REST.

Method 1: Low-level API `plotly.graph_objects`
Python visualization library automatically serializes to JSON for rendering by the Plotly.js JavaScript library.

Method 2: High-level API `plotly.express`
Plotly Express is a new high-level Python visualization library: it's a wrapper for Plotly.py that exposes a simple syntax for complex charts.

### [GeoJSON](https://geojson.org/)
An open standard format designed for representing simple geographical features, along with their non-spatial attributes.

## Data
### [OpenDevelopmentMekong](https://opendevelopmentmekong.net//)
Open Development Mekong (OD Mekong) and related country websites are independent collectors and providers of objective data on development trends in the Mekong Delta.

### [The General Statistics Office of Vietnam](https://www.gso.gov.vn/en/employment/)
GSO is an organization directly under the Ministry of Planning and Investment (MPI) realizing the function as an adviser for the MPI Minister in state management for statistics; conducting statistical activities and providing social and economic information to organizations and individuals domestically and internationally in accordance with the law.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Thu-Duong/plotting-geo-map/main?filepath=https%3A%2F%2Fgithub.com%2FThu-Duong%2Fplotting-geo-map%2Fblob%2Fmain%2FVietnam_Map.ipynb)

## References

- https://plotly.com/python/choropleth-maps/

- https://plotly.com/python/colorscales/

- https://plotly.com/python/bubble-maps/

- https://plotly.com/python/mapbox-layers/
