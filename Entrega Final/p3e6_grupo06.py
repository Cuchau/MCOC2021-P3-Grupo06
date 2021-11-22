from math import sqrt
from sys import path
from numpy import infty, number
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import geopandas as gps
from networkx.algorithms import astar_path, all_simple_paths, all_shortest_paths,dijkstra_path
import numpy as np

zonas_gdf = gps.read_file("zonas-eod.json")

ox.config(use_cache=True, log_console= True)

G = nx.read_gpickle("santiago_grueso.gpickle")

gdf_nodes, gdf_edges = ox.graph_to_gdfs(G)

street_centroids = gdf_edges.centroid

#print (f"gdf_nodes={gdf_nodes}")
#print (f"gdf_edges={gdf_edges}")

plt.figure()
ax = plt.subplot(111)



#zona_origen = 181
#zona_destino = 677

OD = {
    ("201","307"): 681.6691069 , ("200","307"): 208.4113087 , ("268","307"): 333.0497306 , ("471","307"): 1377.864682 , ("287","307"): 36.83261648 , ("471","307"): 1377.864682 , ("287","307"): 36.83261648 , ("500","307"): 1170.159221 , ("512","307"): 107.7533561,
    ("307","307"): 4074.92268173,("497","307"): 55.14852889,  ("370","307"): 609.1797, 
    ("437","307"): 54.35116175,  ("490","307"): 526.0962531,  ("696","307"): 159.6066279, 
    ("695","307"): 153.8278962,  ("724","307"): 124.5140875
}

#copia
OD_target = OD.copy()

def weightfun(n1,n2,attr_arco):

    usar_arco_numero = 0
    if "name" in attr_arco[usar_arco_numero]:
        name = str(attr_arco[usar_arco_numero]["name"])
    else:
        name = ""
    #if "lanes" in attr_arco[usar_arco_numero]:
    #    p = str(attr_arco[usar_arco_numero]["lanes"])
    #else:
    #    p = ""
    length = attr_arco[usar_arco_numero]["length"]
    street_type = attr_arco[usar_arco_numero]["highway"]
    G.add_edge(n1,n2,usar_arco_numero, flujo = 0)
    #G.add_edge(n1,n2 , flujo = 0)
    #f = 0 #agregar atributo de flujo al grafo
    f = attr_arco[usar_arco_numero]["flujo"]
    q = f/5400
    p=2
    #if name.find("Autopista Vespucio Oriente")>=0:
    #    vel=25
    #    u= 5
    if street_type=="motorway":
        vel=25
        u= 5
    elif street_type=="primary":
        vel=15
        u= 3
    elif street_type=="secondary":
        vel=15
        u= 3
    else:
        vel=8
        u= 2

    tiempo = length/vel
    costo = tiempo + 12*(5-u)+(900/u*p)*(10*q-(u*p)+np.sqrt(((10*q-u*p)**2)+q/9)) 

    return costo

zonas_origen =  [201,200,268,471,287,500,512,307,497,370,437,490,696,695,724]
zonas_destino = [307,307,307,307,307,307,307,307,307,307,307,307,307,307,307]
zonas_c=[307,201,200,268,471,287,500,512,307,497,370,437,490,696,695,724,700]

zonas_seleccionadas = zonas_gdf[zonas_gdf["ID"].isin(zonas_c)]
centroid_seleccionados = zonas_seleccionadas.centroid
#poner nombre de las zonas arriba de los centroides
#for idx, row in zonas_seleccionadas.iterrows():
#    #print(f"idx = {idx}")
#    #print("ID = ",row["ID"])
#    #print("comuna = ",row["Comuna"])
#    #break
#    c = row.geometry.centroid
#    ax.annotate(text=row["ID"], xy=(c.x,c.y), horizontalalignment="center" )

 
for zona_destino in zonas_destino:  
    p_d = zonas_gdf[zonas_gdf.ID==zona_destino].representative_point()
    cx_zona_destino, cy_zona_destino = float(p_d.x),  float(p_d.y)
    distancia_minima = np.infty
    for i,node in enumerate (G.nodes):
        cx_nodo = G.nodes[node]["x"]
        cy_nodo = G.nodes[node]["y"]
        dist_nodo_actual = np.sqrt((cx_nodo - cx_zona_destino)**2 + (cy_nodo - cy_zona_destino)**2)
        if dist_nodo_actual < distancia_minima:
            distancia_minima = dist_nodo_actual
            nodo_destino = node
            
#-------    ------------------------------------------------------- 
for zona_origen in zonas_origen:
    p_o = zonas_gdf[zonas_gdf.ID==zona_origen].representative_point()
    cx_zona_origen, cy_zona_origen = float(p_o.x), float(p_o.y)
    #print (cx_zona_origen, cy_zona_origen
    distancia_minima = np.infty
    for i,node in enumerate (G.nodes):
        cx_nodo = G.nodes[node]["x"]
        cy_nodo = G.nodes[node]["y"]
        dist_nodo_actual = np.sqrt((cx_nodo - cx_zona_origen)**2 + (cy_nodo - cy_zona_origen)**2)

        if dist_nodo_actual < distancia_minima:
            distancia_minima = dist_nodo_actual
            nodo_origen = node
            take_path = dijkstra_path(G, nodo_origen, nodo_destino, weight=weightfun)

            Nparadas=len(take_path)
            XX=[]
            YY=[]
            for i in range(Nparadas-1):
                n1=take_path[i]
                n2=take_path[i+1]
                tomar_arco = 0
                arco = G.edges[n1,n2,tomar_arco]
                if "name" in arco:
                    nombre = arco["name"]
                else:
                    nombre = ""
                    #print(f"uniendo {n1} con {n2} sigue por {nombre}")

                xx=[G.nodes[n1]["x"], G.nodes[n2]["x"]]
                yy=[G.nodes[n1]["y"], G.nodes[n2]["y"]]
                XX.append(xx)
                YY.append(yy)
                #print(f"uniendo {n1} con {n2} sigue por {nombre}")
                #print(f"info{arco}")
                #ax.plot(xx,yy, color = "red", linewidth=2)
#ax.plot(XX,YY, color = "red", linewidth=2)
#---------------------------------------------------------------------------------------
#while True:
#    se_asigno_demanda = False
#    for key in OD:
#
#        origen = int(key[0])
#        destino = int(key[1])
#        demanda_actual = OD[key]
#        demanda_objetivo = OD_target[key]
#        
#        if demanda_actual > 0:
#            #Ruta minima
#            p_o = zonas_gdf[zonas_gdf.ID==origen].representative_point()
#            cx_zona_origen, cy_zona_origen = float(p_o.x), float(p_o.y)
#            #print (cx_zona_origen, cy_zona_origen
#            distancia_minima = np.infty
#            for i,node in enumerate (G.nodes):
#                cx_nodo = G.nodes[node]["x"]
#                cy_nodo = G.nodes[node]["y"]
#                dist_nodo_actual = np.sqrt((cx_nodo - cx_zona_origen)**2 + (cy_nodo - cy_zona_origen)**2)
#
#                if dist_nodo_actual < distancia_minima:
#                    distancia_minima = dist_nodo_actual
#                    nodo_origen = node
#  
#            p_d = zonas_gdf[zonas_gdf.ID==destino].representative_point()
#            cx_zona_destino, cy_zona_destino = float(p_d.x),  float(p_d.y)
#            distancia_minima = np.infty
#            for i,node in enumerate (G.nodes):
#                cx_nodo = G.nodes[node]["x"]
#                cy_nodo = G.nodes[node]["y"]
#                dist_nodo_actual = np.sqrt((cx_nodo - cx_zona_destino)**2 + (cy_nodo - cy_zona_destino)**2)
#                if dist_nodo_actual < distancia_minima:
#                    distancia_minima = dist_nodo_actual
#                    nodo_destino = node
#
#            path = dijkstra_path(G, nodo_origen, nodo_destino,weight=weightfun)
#
#            #Incrementar flujo en ruta minima
#            Nparadas = len(path)
#            for i in range(Nparadas-1):
#                o = path[i]
#                d = path[i+1]
#                G.edges[o,d,0]["flujo"] += 1
#            #print(f"demanda {demanda_actual} {path}")¿
#            OD[key] -=1
#            se_asigno_demanda=True
#    if not se_asigno_demanda:
#        break
#-----------------------------------------------------------------------------------
#
#take_path = dijkstra_path(G, nodo_origen, nodo_destino, weight=weightfun)
#Nparadas=len(take_path)
#XX=[]
#YY=[]
#for i in range(Nparadas-1):
#    n1=take_path[i]
#    n2=take_path[i+1]
#    tomar_arco = 0
#    arco = G.edges[n1,n2,tomar_arco]
#    if "name" in arco:
#        nombre = arco["name"]
#    else:
#        nombre = ""
#        #print(f"uniendo {n1} con {n2} sigue por {nombre}")
#
#    xx=[G.nodes[n1]["x"], G.nodes[n2]["x"]]
#    yy=[G.nodes[n1]["y"], G.nodes[n2]["y"]]
#    XX.append(xx)
#    YY.append(yy)
#    print(f"uniendo {n1} con {n2} sigue por {nombre}")
#    print(f"info{arco}")
#    ax.plot(XX,YY, color = "red", linewidth=3)



calles_clipp=zonas_seleccionadas.clip(zonas_seleccionadas["geometry"])

motorway = gdf_edges[gdf_edges.highway=="motorway"]
primary = gdf_edges[gdf_edges.highway=="primary"]
secondary = gdf_edges[gdf_edges.highway=="secondary"]
tertiary = gdf_edges[gdf_edges.highway=="tertiary"]
AVO = gdf_edges[(gdf_edges.highway=="construction") & (gdf_edges.name=="Autopista Vespucio Oriente")]

motorway1 = gps.clip(motorway,calles_clipp.geometry)
secondary1 = gps.clip(secondary,calles_clipp.geometry)
tertiary1 = gps.clip(tertiary,calles_clipp.geometry)
primary1 = gps.clip(primary,calles_clipp.geometry)
AVO1 = gps.clip(AVO,calles_clipp.geometry)

motorway .plot(ax=ax, color="orange")
secondary.plot(ax=ax, color="yellow")
tertiary .plot(ax=ax, color="green")
primary .plot(ax=ax, color="blue")
AVO     .plot(ax=ax, color="purple")
zonas_seleccionadas.plot(ax=ax, color= "#9D9D9D")

#plt.figure(2)
#ax1 = plt.subplot(111)
#pos = nx.get_node_attributes(G)
#nx.draw(G, pos, with_labels=True, font_weight = "bold")
#labels = nx.get_edge_attributes(G,"costo")
#nx.draw_networkx_edge_labels(G, pos, edge_labels= labels)
#plt.suptitle("Costo")

plt.show() 
