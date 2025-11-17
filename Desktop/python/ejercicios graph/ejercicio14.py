from graph import Graph
from typing import Any

#a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
#   baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

Grafo = Graph(is_directed=True) #El grafo debe ser no dirigido, pero en la clase Graph, el valor is_directed esta mal introducido,
                                #siendo False cuando es dirigido y True cuando es no dirigido. Por eso lo puse asi.

ambientes = [ ("Cocina"),
            ("Comedor"),
            ("Cochera"),
            ("Quincho"),
            ("Baño 1"),
            ("Baño 2"),
            ("Habitación 1"),
            ("Habitación 2"),
            ("Sala de estar"),
            ("Terraza"),
            ("Patio")
    ]
for ambiente in ambientes:
    Grafo.insert_vertex(ambiente)

#b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
#   ta es la distancia entre los ambientes, se debe cargar en metros;

edges_info = [ ("Cocina", "Comedor", 5),
                ("Cocina", "Patio", 10),
                ("Cocina", "Sala de estar", 7),
                ("Comedor", "Cocina", 5),
                ("Comedor", "Sala de estar", 4),
                ("Comedor", "Terraza", 12),
                ("Cochera", "Quincho", 15),
                ("Cochera", "Patio", 8),
                ("Cochera", "Baño 1", 20),
                ("Quincho", "Cochera", 15),
                ("Quincho", "Patio", 6),
                ("Quincho", "Baño 2", 18),
                ("Baño 1", "Habitación 1", 9),
                ("Baño 1", "Cochera", 20),
                ("Baño 1", "Sala de estar", 14),
                ("Baño 2", "Habitación 2", 11),
                ("Baño 2", "Quincho", 18),
                ("Baño 2", "Terraza", 13),
                ("Habitación 1", "Baño 1", 9),
                ("Habitación 1", "Sala de estar", 5),
                ("Habitación 1", "Terraza", 16),
                ("Habitación 2", "Baño 2", 11),
                ("Habitación 2", "Sala de estar", 6),
                ("Habitación 2", "Patio", 14),
                ("Sala de estar", "Cocina", 7),
                ("Sala de estar", "Comedor", 4),
                ("Sala de estar", "Habitación 1", 5),
                ("Sala de estar", "Habitación 2", 6),
                ("Sala de estar", "Terraza", 9),
                ("Terraza", "Comedor", 12),
                ("Terraza", "Baño 2", 13),
                ("Terraza", "Habitación 1", 16),
                ("Patio", "Cocina", 10),
                ("Patio", "Cochera", 8),
                ("Patio", "Quincho", 6),
                ("Patio", "Habitación 2", 14),
                ("Patio", "Baño 1", 17)
]
for origin, destination, metros in edges_info:
        Grafo.insert_edge(origin, destination, metros)

#c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
#   para conectar todos los ambientes;

print("El árbol de expansión mínima:")
tree = Grafo.kruskal("Cocina") #no importa la variable de entraada cuando se usa kruskal
print(tree)
separaciones = tree.split(';')
total_metros = 0
for separacion in separaciones:
    origen, destino, peso = separacion.split('-')
    total_metros += int(peso)

print("Se necesitan", total_metros, "metros de cable para conectar todos los ambientes.")

#d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#   determinar cuántos metros de cable de red se necesitan para conectar el router con el
#   Smart Tv.

path = Grafo.dijkstra("Habitación 1")
destination = 'Sala de estar'
peso_total = None
camino_completo = []
while path.size() > 0:
    value = path.pop()
    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1]
        camino_completo.append(value[0])
        destination = value[2]
camino_completo.reverse()
print("El camino más corto desde la habitación 1 hasta la sala de estar es: ", "-".join(camino_completo), " Necesitando ", peso_total, "metros.")