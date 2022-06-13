import pandas as pd
import numpy as np

def convert_id_map(geomap, name, id):
    id_map = {}
    for feature in geomap["features"]:
        feature[id] = feature["properties"][id]
        id_map[feature["properties"][name]] = feature[id]
    return id_map