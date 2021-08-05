import pandas as pd
import numpy as np

def convert_id_map(geomap, name, id):
    id_map = {}
    for feature in geomap["features"]:
        feature[id] = feature["properties"][id]
        id_map[feature["properties"][name]] = feature[id]
    return id_map

def submit_event_handler(args):
    if category.value in ['Income_from_agriculture_forestry_aquaculture','Income_from_non_agriculture_forestry_aquaculture','Others_income','Salary']:
        df_curr = df_grouped.get_group(year.value).reset_index(drop=True)
        new_data = df_curr.loc[1:, 'LRate_' + str(category.value)]
        with fig.batch_update():
            fig.data[0].z = new_data
            fig.layout.title = ' '.join([str(category.value), 'in 2018'])