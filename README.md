# MCOC2021-P3-Grupo06
Integrantes: 
* Bruno Riquelme 
* Ignacio Inostroza

#Entrega 2

![fig1](https://user-images.githubusercontent.com/88348645/141021573-eaebf19c-6829-46f1-ad93-bb768c75869c.png)

![fig2](https://user-images.githubusercontent.com/88348645/141021589-a7983a79-503e-480c-a6ce-d3f9b09d5653.png)

![fig3](https://user-images.githubusercontent.com/88348645/141021594-a217c8f5-5baf-4d30-bd3d-864848e981d2.png)

![fig4](https://user-images.githubusercontent.com/88348645/141021595-b1eaa47f-c78b-4797-81ec-730e153eada7.png)

#Entrega 3

*Zona Bruno Riquelme

![zona_bruno_riquelme](https://user-images.githubusercontent.com/88348645/141487246-eb9f5b5c-37bb-4153-a3e7-9b0a291e6e6c.png)

#Entrega 4

incrementos = [0.1]*9 + [0.01]*9 + [0.001]*9 + [0.0001]*10
            for i in range(Nparadas-1):
                o = path[i]
                d = path[i+1]
                for i, incremento in enumerate(incrementos):
                    G.edges[o,d]["flujo"] += incremento
            print(f"demanda {demanda_actual} , {path} ")
            OD[key] -=1
            
Con esta función se aumenta el flujo y se disminuye la demanda hasta que es 0, esto es para que el ciclo pare cuando ya no hay demanda en la ruta respectiva, aunque igual hay diferencias con la entrega, esto puede deberse a que el decremento de la funcion no es correcta.

#Entrega 5

Con la siguiente imagen se entiende lo de :No muestre otras calles y corte todas las calles para que solo estén en las zonas seleccionadas.

![calles_zonas](https://user-images.githubusercontent.com/88348645/142656589-49fc5f95-a305-4937-b2ba-1509ccc8d901.png)

igual dejo una imagen donde se aprecian todos las calles por si acaso

![zona_completa](https://user-images.githubusercontent.com/88348645/142656786-b42217b3-69f7-4f4e-9aef-841daf5e5424.png)

