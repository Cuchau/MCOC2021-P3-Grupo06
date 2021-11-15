import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.weighted import dijkstra_path

f1 = lambda f: 10 + f/120      # (r,v,z)
f2 = lambda f: 14 + (3*f)/240  # (s,u,w,y)
f3 = lambda f: 10 + f/240      # (t,x)    

# Matriz origen destino
OD = {
    ("A","B") : 1100 , ("A","C"): 1110 , ("A","E"): 1110 , ("B","C"): 1140 , ("B","D"): 1160 , ("C","E"): 1170 , ("C","G"): 1180 , ("D","C"): 350 , ("D","E"): 1190 , ("D","G"): 1200
}

#copia
OD_target = OD.copy()

G = nx.DiGraph()

G.add_node("A",pos=(1,4))
G.add_node("B",pos=(1,3))
G.add_node("C",pos=(3,3))
G.add_node("D",pos=(3,1.5))
G.add_node("E",pos=(5,4))
G.add_node("G",pos=(5,3))

G.add_edge("A","B", fcosto = f1, flujo = 0)
G.add_edge("A","C", fcosto = f2, flujo = 0)
G.add_edge("B","C", fcosto = f3, flujo = 0)
G.add_edge("B","D", fcosto = f2, flujo = 0)
G.add_edge("C","E", fcosto = f2, flujo = 0)
G.add_edge("C","G", fcosto = f3, flujo = 0)
G.add_edge("D","C", fcosto = f1, flujo = 0)
G.add_edge("D","G", fcosto = f2, flujo = 0)
G.add_edge("G","E", fcosto = f1, flujo = 0)

def costo(ni, nf, attr):
    f_costo_arco = attr["fcosto"]
    flujo_arco = attr["flujo"]
    return f_costo_arco(flujo_arco)

#Ruta minima

while True:
    se_asigno_demanda = False
    for key in OD:

        origen = key[0]
        destino = key[1]
        demanda_actual = OD[key]
        demanda_objetivo = OD_target[key]
        
        if demanda_actual > 0:
            #Ruta minima
            path = dijkstra_path(G, origen, destino, weight = costo)

            #Incrementar flujo en rua minima
            Nparadas = len(path)
            for i in range(Nparadas-1):
                o = path[i]
                d = path[i+1]
                G.edges[o,d]["flujo"] += 0.01
            print(f"demanda {demanda_actual} {path}")

            OD[key] -=0.01
            se_asigno_demanda=True

    if not se_asigno_demanda:
        break

#Para ver costo
for ni, nf in G.edges:
    arco = G.edges[ni,nf]
    f_costo_arco = arco["fcosto"]
    flujo_arco = arco["flujo"]
    arco["costo"] = f_costo_arco(flujo_arco)

plt.figure(1)
ax1 = plt.subplot(111)
pos = nx.get_node_attributes(G,"pos")
nx.draw(G, pos, with_labels=True, font_weight = "bold")
labels = nx.get_edge_attributes(G,"flujo")
nx.draw_networkx_edge_labels(G, pos, edge_labels= labels)
plt.suptitle("Flujo")

plt.figure(2)
ax1 = plt.subplot(111)
pos = nx.get_node_attributes(G,"pos")
nx.draw(G, pos, with_labels=True, font_weight = "bold")
labels = nx.get_edge_attributes(G,"costo")
nx.draw_networkx_edge_labels(G, pos, edge_labels= labels)
plt.suptitle("Costo")

plt.show()
