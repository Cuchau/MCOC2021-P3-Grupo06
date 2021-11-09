import networkx as nx
import matplotlib.pyplot as plt
from numpy.lib.function_base import append
from math import sqrt
from networkx.algorithms import dijkstra_path
G = nx.Graph() 

vel1 = 120
vel2 = 120
vel3 = 40
vel4 = 40
vel5 = 40
vel6 = 60
vel7 = 40
vel8 = 60
vel9 = 40 
vel10 = 60
vel11 = 120
vel12 = 120
vel13 = 120
vel14 = 60
vel15 = 60

largo1 = sqrt((1- 4)**2 + (0 - 0)**2)
largo2 = sqrt((1- 1)**2 + (0 - 6)**2)
largo3 =  sqrt((1- 4)**2 + (0 - 3)**2)
largo4 =  sqrt((4- 1)**2 + (3 - 6)**2)
largo5 =  sqrt((4- 5)**2 + (3 - 8)**2)
largo6 =  sqrt((4- 3)**2 + (7 - 3)**2)
largo7 =  sqrt((1- 0)**2 + (6 - 10)**2)
largo8 =  sqrt((7- 5)**2 + (3 - 8)**2)
largo9 =  sqrt((7- 9)**2 + (3 - 7)**2)
largo10 =  sqrt((7-10)**2 + (3 - 1)**2)
largo11 = sqrt((10-4)**2 + (1 - 0)**2)
largo12 = sqrt((10-9)**2 + (1 - 7)**2)
largo13 = sqrt((0- 5)**2 + (10 - 8)**2)
largo14 =  sqrt((5- 8)**2 + (8 - 10)**2)
largo15 =  sqrt((9- 8)**2 + (7 - 10)**2)

tiempo1 =  largo1/vel1
tiempo2 =  largo2/vel2
tiempo3 =  largo3/vel3
tiempo4 =  largo4/vel4
tiempo5 =  largo5/vel5
tiempo6 =  largo6/vel6
tiempo7 =  largo7/vel7
tiempo8 =  largo8/vel8
tiempo9 =  largo9/vel9
tiempo10 = largo10/vel10
tiempo11 = largo11/vel11
tiempo12 = largo12/vel12
tiempo13 = largo13/vel13
tiempo14 = largo14/vel14
tiempo15 = largo15/vel15

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

G.add_edge("0","6", tiempo = tiempo1)
G.add_edge("0","2", tiempo = tiempo2)
G.add_edge("0","1", tiempo = tiempo3)
G.add_edge("1","2", tiempo = tiempo4)
G.add_edge("1","7", tiempo = tiempo5)
G.add_edge("1","3", tiempo = tiempo6)
G.add_edge("2","5", tiempo = tiempo7)
G.add_edge("3","7", tiempo = tiempo8)
G.add_edge("3","8", tiempo = tiempo9)
G.add_edge("3","4", tiempo = tiempo10)
G.add_edge("4","6", tiempo = tiempo11)
G.add_edge("4","8", tiempo = tiempo12)
G.add_edge("5","7", tiempo = tiempo13)
G.add_edge("7","9", tiempo = tiempo14)
G.add_edge("8","9", tiempo = tiempo15)


pos = nx.get_node_attributes(G,"pos")
labels = nx.get_edge_attributes(G,"tiempo")
edgelist=[("0","6"),("0","2"),("0","1"),("1","2"),("1","7"),("1","3"),("2","5"),("3","7"),("3","8"),("3","4"),("4","6"),("4","8"),("5","7"),("7","9"),("8","9")]
colores=["grey","grey","brown","brown","brown","g","brown","g","brown","g","grey","grey","grey","g","g"]


plt.figure(1)
ax=plt.subplot()
nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
nx.draw_networkx_edges(G, pos, edgelist=edgelist, edge_color=colores,ax=ax)
plt.grid()

#plt.suptitle(f"Ruta minima: {ruta} costo={costo_ruta}")
ax.tick_params( left=True, bottom=True, labelleft=True, labelbottom=True)
plt.xticks([0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],["0","1.0","2.0","3.0","4.0","5.0","6.0","7.0","8.0","9.0","10"])
plt.yticks([0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],["0","1.0","2.0","3.0","4.0","5.0","6.0","7.0","8.0","9.0","10"])
plt.xlabel("X (Km)")
plt.ylabel("Y (Km)")
plt.show()  

#mejor ruta------------------------------------------------------------------------
path1 = dijkstra_path(G, "0", "9", weight="tiempo")
path2 = dijkstra_path(G, "4", "5", weight="tiempo")
path3 = dijkstra_path(G, "0", "4", weight="tiempo")

edgelist1=[]
colores1=[]
ancho1=[]
for ni,nf in G.edges:
    if ni in path1 and nf in path1:
        colores1.append("r")
        ancho1.append(5)
    else:
        colores1.append("g")
        ancho1.append(1)
    edgelist1.append((ni,nf))

edgelist2=[]
colores2=[]
ancho2=[]
for ni,nf in G.edges:
    if ni in path2 and nf in path2:
        colores2.append("r")
        ancho2.append(5)
    else:
        colores2.append("g")
        ancho2.append(1)
    edgelist2.append((ni,nf))

edgelist3=[]
colores3=[]
ancho3=[]
for ni,nf in G.edges:
    if ni in path3 and nf in path3:
        colores3.append("r")
        ancho3.append(5)
    else:
        colores3.append("g")
        ancho3.append(1)
    edgelist3.append((ni,nf))

plt.figure(2)
ax=plt.subplot()
nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
nx.draw_networkx_edges(G, pos, edgelist=edgelist1, edge_color=colores1,width=ancho1,ax=ax)
#nx.draw_networkx_edge_labels(G, pos, edge_labels= labels)
plt.suptitle(f"andate por apth1")
plt.grid()
ax.tick_params( left=True, bottom=True, labelleft=True, labelbottom=True)
plt.xticks([0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],["0","1.0","2.0","3.0","4.0","5.0","6.0","7.0","8.0","9.0","10"])
plt.yticks([0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],["0","1.0","2.0","3.0","4.0","5.0","6.0","7.0","8.0","9.0","10"])
plt.xlabel("X (Km)")
plt.ylabel("Y (Km)")
plt.show()  

plt.figure(3)
ax=plt.subplot()
nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
nx.draw_networkx_edges(G, pos, edgelist=edgelist2, edge_color=colores2,width=ancho2,ax=ax)
#nx.draw_networkx_edge_labels(G, pos, edge_labels= labels)
plt.suptitle(f"andate por path2")
plt.grid()
ax.tick_params( left=True, bottom=True, labelleft=True, labelbottom=True)
plt.xticks([0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],["0","1.0","2.0","3.0","4.0","5.0","6.0","7.0","8.0","9.0","10"])
plt.yticks([0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],["0","1.0","2.0","3.0","4.0","5.0","6.0","7.0","8.0","9.0","10"])

plt.xlabel("X (Km)")
plt.ylabel("Y (Km)")
plt.show()  

plt.figure(4)
ax=plt.subplot()
nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
nx.draw_networkx_edges(G, pos, edgelist=edgelist3, edge_color=colores3,width=ancho3,ax=ax)
#nx.draw_networkx_edge_labels(G, pos, edge_labels= labels)
plt.suptitle(f"andate por path3")
plt.grid()
ax.tick_params( left=True, bottom=True, labelleft=True, labelbottom=True)
plt.xticks([0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],["0","1.0","2.0","3.0","4.0","5.0","6.0","7.0","8.0","9.0","10"])
plt.yticks([0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],["0","1.0","2.0","3.0","4.0","5.0","6.0","7.0","8.0","9.0","10"])

plt.xlabel("X (Km)")
plt.ylabel("Y (Km)")
plt.show()  


