import networkx as nx
import matplotlib.pyplot as plt
from numpy.lib.function_base import append
from math import sqrt
G = nx.Graph() 

#Agregando nodos(nodes) 
G.add_node("0", pos=[1,0])
G.add_node("1", pos=[4,3])
G.add_node("2", pos=[1,6])
G.add_node("3", pos=[7,3])
G.add_node("4", pos=[10,1])
G.add_node("5", pos=[0,10])
G.add_node("6", pos=[4,0])
G.add_node("7", pos=[5,8])
G.add_node("8", pos=[9,7])
G.add_node("9", pos=[8,10])


pos = nx.get_node_attributes(G,"pos")


labels = nx.get_edge_attributes(G,"vel")

edgelist=[("0","6"),("0","2"),("0","1"),("1","2"),("1","7"),("1","3"),("2","5"),("3","7"),("3","8"),("3","4"),("4","6"),("4","8"),("5","7"),("7","9"),("8","9")]

colores=["grey","grey","brown","brown","brown","g","brown","g","brown","g","grey","grey","grey","g","g"]


plt.figure()
ax=plt.subplot()
nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
nx.draw_networkx_edges(G, pos, edgelist=edgelist, edge_color=colores,ax=ax)
nx.draw_networkx_edge_labels(G, pos)
plt.grid()

#plt.suptitle(f"Ruta minima: {ruta} costo={costo_ruta}")
ax.tick_params( left=True, bottom=True, labelleft=True, labelbottom=True)
plt.xticks([0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],["0","1.0","2.0","3.0","4.0","5.0","6.0","7.0","8.0","9.0","10"])
plt.yticks([0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],["0","1.0","2.0","3.0","4.0","5.0","6.0","7.0","8.0","9.0","10"])

plt.xlabel("X (Km)")
plt.ylabel("Y (Km)")
plt.show()  


#otras parte

G.add_edge(("0","6"), vel = 120, largo = sqrt((1- 4)**2 + (0 - 0)**2))
G.add_edge(("0","2"), vel = 120, largo = sqrt((1- 1)**2 + (0 - 6)**2))
G.add_edge(("0","1"), vel = 40, largo =  sqrt((1- 4)**2 + (0 - 3)**2))
G.add_edge(("1","2"), vel = 40, largo =  sqrt((4- 1)**2 + (3 - 6)**2))
G.add_edge(("1","7"), vel = 40, largo =  sqrt((4- 5)**2 + (3 - 8)**2))
G.add_edge(("1","3"), vel = 60, largo =  sqrt((4- 3)**2 + (7 - 3)**2))
G.add_edge(("2","5"), vel = 40, largo =  sqrt((1- 0)**2 + (6 - 10)**2))
G.add_edge(("3","7"), vel = 60, largo =  sqrt((7- 5)**2 + (3 - 8)**2))
G.add_edge(("3","8"), vel = 40, largo =  sqrt((7- 9)**2 + (3 - 7)**2))
G.add_edge(("3","4"), vel = 60, largo =  sqrt((7-10)**2 + (3 - 1)**2))
G.add_edge(("4","6"), vel = 120, largo = sqrt((10-4)**2 + (1 - 0)**2))
G.add_edge(("4","8"), vel = 120, largo = sqrt((10-9)**2 + (1 - 7)**2))
G.add_edge(("5","7"), vel = 120, largo = sqrt((0- 5)**2 + (10 - 8)**2))
G.add_edge(("7","9"), vel = 60, largo =  sqrt((5- 8)**2 + (8 - 10)**2))
G.add_edge(("8","9"), vel = 60, largo =  sqrt((9- 8)**2 + (7 - 10)**2))