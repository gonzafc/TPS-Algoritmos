from graph import Graph
from typing import Any
                                ##h. debe utilizar un grafo no dirigido.
Grafo = Graph(is_directed=True) ##Profe, el grafo debe ser no dirigido, pero en la clase Graph, el valor is_directed esta mal introducido,
                                ##siendo False cuando es dirigido y True cuando es no dirigido. Por eso lo puse asi.
#a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
node_info = [ ("Red Hat", "Notebook"),
              ("Debian", "Notebook"),
              ("Arch", "Notebook"),
              ("Ubuntu", "PC"),
              ("Mint", "PC"),
              ("Fedora", "PC"),
              ("Manjaro", "PC"),
              ("Parrot", "PC"),
              ("Guarani", "Server"),
              ("MongoDB", "Server"),
              ("Impresora", "Impresora"),
              ("Switch1", "Switch"),
              ("Switch2", "Switch"),
              ("Router1", "Router"),
              ("Router2", "Router"),
              ("Router3", "Router")
]

for node, tipo in node_info:
    Grafo.insert_vertex(node)

edges_info = [ ("Red Hat", "Router2", 25),
                ("Guarani", "Router2", 9),  
                ("Router2", "Router3", 50),
                ("Debian", "Switch1", 17),
                ("Ubuntu", "Switch1", 18),
                ("Impresora", "Switch1", 22),
                ("Mint", "Switch1", 80),
                ("Switch1", "Router1", 29),
                ("Router1", "Router2", 37),
                ("Router1", "Router3", 43),
                ("Router3", "Switch2", 61),
                ("Switch2", "Manjaro", 40),
                ("Switch2", "Parrot", 12),
                ("Switch2", "MongoDB", 5),
                ("Switch2", "Arch", 56),
                ("Switch2", "Fedora", 3)
]

for origin, destination, weigth in edges_info:
        Grafo.insert_edge(origin, destination, weigth)

#Grafo.show()

#b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:Red Hat, Debian, Arch;

print("Barrido en profundidad desde las 3 notebooks:")
notebooks = ["Red Hat", "Debian", "Arch"]
for notebook in notebooks:
      print("Desde la notebook ", notebook + ":")
      Grafo.deep_sweep(notebook)
      print("")
print("Barrido en amplitud desde las 3 notebooks:")
for notebook in notebooks:
      print("Desde la notebook ", notebook + ":")
      Grafo.amplitude_sweep(notebook)
      print("")

#c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora;

print("c) Camino más corto a la impresora: ")
pcs = ["Manjaro", "Red Hat", "Fedora"]
for pc in pcs:
    path = Grafo.dijkstra(pc)
    destination = 'Impresora'
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
    
    print(f'Camino desde {pc}: {" -> ".join(camino_completo)} (Costo: {peso_total})')


#d. encontrar el árbol de expansión mínima;
tree = Grafo.kruskal("Red Hat")
print("Árbol de expansión mínima usando el algoritmo de Kruskal:")
print(tree)


#e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
print("Caminos más cortos hasta el servidor Guarani desde las pcs:")
pcs = ["Ubuntu", "Parrot", "Mint", "Fedora", "Manjaro"]
peso_minimo = None
mejor_pc = None
mejor_camino = []
for pc in pcs:
    path = Grafo.dijkstra(pc)
    destination = "Guarani"
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
    if peso_total is not None and (peso_minimo is None or peso_total < peso_minimo):
        peso_minimo = peso_total
        mejor_pc = pc
        mejor_camino = camino_completo
print(f'El camino más corto hasta Guarani es desde {mejor_pc}: {" -> ".join(mejor_camino)} (Costo: {peso_minimo})')

#f. indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”;
pcs = ["Ubuntu", "Mint", "Debian"]
peso_minimo = None
mejor_pc = None
mejor_camino = []
for pc in pcs:
    path = Grafo.dijkstra(pc)
    destination = "MongoDB"
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
    if peso_total is not None and (peso_minimo is None or peso_total < peso_minimo):
        peso_minimo = peso_total
        mejor_pc = pc
        mejor_camino = camino_completo
print(f'El camino más corto hasta MongoDB (Con las computadoras del switch1) es desde {mejor_pc}: {" -> ".join(mejor_camino)} (Costo: {peso_minimo})')

#g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;

Grafo.delete_edge("Impresora", "Switch1")
Grafo.insert_edge("Impresora", "Router2", 33)
print("Barrido en profundidad desde las 3 notebooks después de cambiar la conexión de la impresora:")
for notebook in notebooks: #las notebooks ya las definí en el punto b
      print("Desde la notebook ", notebook + ":")
      Grafo.deep_sweep(notebook)
      print("")
print("Barrido en amplitud desde las 3 notebooks:")
for notebook in notebooks:
      print("Desde la notebook ", notebook + ":")
      Grafo.amplitude_sweep(notebook)
      print("")