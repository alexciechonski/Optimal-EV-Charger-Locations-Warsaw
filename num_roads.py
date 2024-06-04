from distances import Distances as dst
import json
import osmnx as ox 
import networkx as nx
import requests
from time import perf_counter
import numpy as np
import numpy as np

def find_roads_within_range(lat, lon):
    """ find significant roads in the radius of 4km from a specified location"""
    
    # Define a bounding box around the coordinates with a specified distance in meters
    north, south, east, west = ox.utils_geo.bbox_from_point((lat, lon), dist=4000)
    
    # Fetch the graph with a custom filter if provided
    filter1 = '["highway"~"motorway|trunk|primary|secondary|motorway_link|trunk_link|primary_link"]'
    filter2 = '["highway"~"motorway|trunk|primary|motorway_link|trunk_link|primary_link"]'
    graph = ox.graph_from_bbox(north, south, east, west, custom_filter=filter1)
    
    # Convert the graph to GeoDataFrame of edges
    edges_gdf = ox.graph_to_gdfs(graph, nodes=False, edges=True)
    
    # Filter edges to include only those with non-empty name attribute
    named_edges = edges_gdf.dropna(subset=['name'])
    
    # Flatten the lists in the 'name' column
    named_edges['name'] = named_edges['name'].apply(lambda x: x[0] if isinstance(x, list) else x)
    
    # Return the GeoDataFrame containing roads within the range and matching the custom filter
    return list(set(named_edges['name']))

with open('updated_parkings.json','r') as f:
    parkings = json.load(f)
    
for n, data in parkings.items():
    lat = data['lat']
    lon = data['lon']
    lst = find_roads_within_range(lat, lon)
    num = len(lst)
    parkings[n]['roads_num'] = num

with open('u2p.json', 'w') as f:
    json.dump(parkings, f, indent=2)
