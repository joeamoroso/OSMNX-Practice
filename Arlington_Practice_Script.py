import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import networkx as nx
import osmnx as ox
from descartes import PolygonPatch
from shapely.geometry import Point, LineString, Polygon, shape, GeometryCollection
import json
ox.config(log_console=True, use_cache=True)
ox.__version__

# Create omx newtwork from OSM

   # See SHP file from OSM
arlington = ox.gdf_from_place('Arlington, Virginia')
ox.plot_shape(arlington)
   # Create Newtwork
G = ox.graph_from_place('Arlington, VA', network_type='all_private', simplify=True, retain_all=False, truncate_by_edge=False, which_result=1, buffer_dist=None,
 clean_periphery=True, custom_filter=None, timeout=None, memory=None, custom_settings=None, max_query_area_size=None)

   # Plot network
   fig, ax = ox.plot_graph(G, fig_height=8, show=False, close=False, edge_color='k', edge_alpha=0.2, node_color='none')
   plt.show()

   # Save to Disk
file_path = 'C:/Users/joe.amoroso/Python_GIS'
ox.io.save_graph_shapefile(G,filepath =file_path, encoding = 'utf-8')

