import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import geopandas as gps

zonas_gdf = gps.read_file("zonas-eod.json")

ox.config(use_cache=True, log_console= True)

G = nx.read_gpickle("santiago_grueso.gpickle")

gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)

street_centroids = gdf_edges.centroid

#print (f"gdf_nodes={gdf_nodes}")
#print (f"gdf_edges={gdf_edges}")

plt.figure()
ax = plt.subplot(111)

O = [281,435]
D = [306]
zonas_c=[281,435,306,434,267,266,290,304,269,289,291,288,307,287,306,682,677,666,683,433,282,505,512,432,496,305,292,320,507,508,668,669,672,678,667]
zonas_seleccionadas = zonas_gdf[zonas_gdf["ID"].isin(zonas_c)]
#zonas_O = zonas_gdf[zonas_gdf["ID"].isin(O)]
#zonas_D = zonas_gdf[zonas_gdf["ID"].isin(D)]

calles_clipp=zonas_seleccionadas.clip(zonas_seleccionadas["geometry"])
#calles_clipp_O=zonas_O.clip(zonas_O["geometry"])
#calles_clipp_D=zonas_D.clip(zonas_D["geometry"])

centroid_seleccionados = zonas_seleccionadas.centroid
#poner nombre de las zonas arriba de los centroides
for idx, row in zonas_seleccionadas.iterrows():
    #print(f"idx = {idx}")
    #print("ID = ",row["ID"])
    #print("comuna = ",row["Comuna"])
    #break
    c = row.geometry.centroid
    ax.annotate(text=row["ID"], xy=(c.x,c.y), horizontalalignment="center" )


motorway = gdf_edges[gdf_edges.highway=="motorway"]
primary = gdf_edges[gdf_edges.highway=="primary"]
secondary = gdf_edges[gdf_edges.highway=="secondary"]
tertiary = gdf_edges[gdf_edges.highway=="tertiary"]

#Estas tres serian Parte de AVO
AVO1 = gdf_edges[gdf_edges.name=="Avenida Ossa"]
AVO2 = gdf_edges[gdf_edges.name=="Avenida Américo Vespucio Norte"]
AVO3 = gdf_edges[gdf_edges.name=="Avenida Américo Vespucio Sur"]

#cortar Grafo
motorway1 = gps.clip(motorway,calles_clipp.geometry)
secondary1 = gps.clip(secondary,calles_clipp.geometry)
tertiary1 = gps.clip(tertiary,calles_clipp.geometry)
primary1 = gps.clip(primary,calles_clipp.geometry)
AVO1_1 = gps.clip(AVO1,calles_clipp.geometry)
AVO2_1 = gps.clip(AVO2,calles_clipp.geometry)
AVO3_1 = gps.clip(AVO3,calles_clipp.geometry)

#Plotear
motorway1 .plot(ax=ax, color="orange")
secondary1.plot(ax=ax, color="yellow")
tertiary1 .plot(ax=ax, color="green")
primary1  .plot(ax=ax, color="blue")
AVO1_1.plot(ax=ax,color = "red")
AVO2_1.plot(ax=ax,color = "red")
AVO3_1.plot(ax=ax,color = "red")
zonas_seleccionadas.plot(ax=ax, color= "#9D9D9D")

plt.show() 