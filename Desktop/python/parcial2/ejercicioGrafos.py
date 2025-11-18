from graph import Graph
from starwars_data import personajes_data

Grafo = Graph(is_directed=True) #para que el grafo sea no dirigido, is_directed tiene que ser true
# cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de 
# episodios en los que aparecieron juntos ambos personajes que se relacionan;
for personaje in personajes_data:
    Grafo.insert_vertex(personaje['name'], {'total_episodes': personaje['total_episodes']}) #modifiique la clase Graph para que pueda
                                                                                            #guardar dos valores en el nodo
edges_info = [ ('Luke Skywalker', 'Han Solo', 4),
                ('Luke Skywalker', 'Leia', 5),
                ('Luke Skywalker', 'Darth Vader', 3),
                ('Luke Skywalker', 'Obi-Wan Kenobi', 3),
                ('Luke Skywalker', 'Yoda', 2),
                ('Luke Skywalker', 'R2-D2', 6),
                ('Luke Skywalker', 'C-3PO', 6),
                ('Han Solo', 'Leia', 4),
                ('Han Solo', 'Chewbacca', 5),
                ('Han Solo', 'Boba Fett', 1),
                ('Leia', 'Chewbacca', 4),
                ('Leia', 'R2-D2', 5),
                ('Leia', 'C-3PO', 7),
                ('Darth Vader', 'Palpatine', 4),
                ('Darth Vader', 'Obi-Wan Kenobi', 2),
                ('Darth Vader', 'Yoda', 1), 
                ('R2-D2', 'C-3PO', 9), 
                ('R2-D2', 'BB-8', 2),
                ('Rey', 'Kylo Ren', 3),
                ('Rey', 'Chewbacca', 2),
                ('Rey', 'BB-8', 3),
                ('Kylo Ren', 'Palpatine', 1)
    ]
for origin, destination, weigth in edges_info:
        Grafo.insert_edge(origin, destination, weigth)

# hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
print ("Arbol de expansión mínima desde C-3PO:")
print(Grafo.kruskal('C-3PO'))
print ("\nArbol de expansión mínima desde Yoda:")
print(Grafo.kruskal('Yoda'))
print ("\nArbol de expansión mínima desde Leia:")
print(Grafo.kruskal('Leia'))

# determinar cuál es el número máximo de episodio que comparten dos personajes, 
# e indicar todos los pares de personajes que coinciden con dicho número;

def encontrar_max_episodios_juntos(Grafo):
    
    max_peso = 0
    pares_maximos = []
    
    pares_procesados = set() # se usa el set para que no se repitan los pares

    for vertice in Grafo:
        for arista in vertice.edges:
            
            # 3. Creamos un 'par' estándar (ordenado alfabéticamente)
            #    para evitar duplicados. ('Luke', 'Han')
            par = tuple(sorted((vertice.value, arista.value))) ## por el sorted si tenemos han - luke, o luke- han
                                                               ## siempre se va a escribir en el mismo orden (en este caso han - luke) 
            if par in pares_procesados:                        ## esto es para que no se repitan los pares
                # si ya se miro a, b no se mira b, a
                continue 
            pares_procesados.add(par)
            
            peso_actual = arista.weight
            if peso_actual > max_peso:
                max_peso = peso_actual
                pares_maximos = [par] # se cambia el anterior por el nuevo
            
            elif peso_actual == max_peso:
                pares_maximos.append(par)
    return max_peso, pares_maximos

max_episodios, pares = encontrar_max_episodios_juntos(Grafo)
print("\nEl número máximo de episodios compartidos es: ", max_episodios)
print("\nLos pares de personajes que comparten ese número de episodios son:", pares)

# calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
print("\nCamino más corto desde C-3PO a R2-D2:")
camino_C3PO_R2D2 = Grafo.dijkstra('C-3PO')
destination = 'R2-D2'
peso_total = None
camino_completo = []
    
while camino_C3PO_R2D2.size() > 0:
    value = camino_C3PO_R2D2.pop()
    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1]
        camino_completo.append(value[0])
        destination = value[2]
camino_completo.reverse()
    
print(f'Camino desde C-3PO: {" -> ".join(camino_completo)} (Costo: {peso_total})')


print("\nCamino más corto desde Yoda a Darth Vader:")
camino_Yoda_DarthVader = Grafo.dijkstra('Yoda')
destination = 'Darth Vader'
peso_total = None
camino_completo = []

while camino_Yoda_DarthVader.size() > 0:
    value = camino_Yoda_DarthVader.pop()
    if value[0] == destination:
        if peso_total is None:
            peso_total = value[1] 
            
        camino_completo.append(value[0])
        destination = value[2]
camino_completo.reverse()

print(f'Camino desde Yoda: {" -> ".join(camino_completo)} (Costo: {peso_total})')

#indicar qué personajes aparecieron en los nueve episodios de la saga.

def personajes_en_todos_los_episodios(Grafo, total_episodios=9):
    personajes_completos = []
    for vertice in Grafo:
        if vertice.other_values['total_episodes'] == total_episodios:
            personajes_completos.append(vertice.value)
    return personajes_completos
personajes_nueve_episodios = personajes_en_todos_los_episodios(Grafo)
print("\nPersonajes que aparecieron en los nueve episodios de la saga:", personajes_nueve_episodios)
