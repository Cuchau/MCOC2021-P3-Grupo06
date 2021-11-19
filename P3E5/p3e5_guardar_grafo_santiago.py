import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

ox.config(use_cache=True, log_console= True)



G = ox.graph_from_bbox(
    north = -33.3637,
    south = -33.56,
    east = -70.5240 ,
    west = -70.80 ,
    network_type="drive",
    clean_periphery=True,
    custom_filter='["highway"~"motorway|primary|secondary|tertiary|construction"]'
    )

nx.write_gpickle(G, "santiago_grueso.gpickle")


