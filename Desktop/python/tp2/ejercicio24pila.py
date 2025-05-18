from clasestack import Stack

Personajes = Stack()
datos = [
    {"nombre": "Iron Man", "peliculas": 10},
    {"nombre": "Rocket Raccoon", "peliculas": 4},
    {"nombre": "Groot", "peliculas": 5},
    {"nombre": "Black Widow", "peliculas": 7},
    {"nombre": "Doctor Strange", "peliculas": 4},
    {"nombre": "Captain America", "peliculas": 9},
    {"nombre": "Gamora", "peliculas": 6},
    {"nombre": "Drax", "peliculas": 5},
    {"nombre": "Star-Lord", "peliculas": 5},
]

for personaje in datos:
    Personajes.push(personaje)


def posicion_pj(nombre):
    aux_stack = Stack()
    posicion = 1
    encontrada = None

    while Personajes.size() > 0:
        personaje = Personajes.pop()
        if personaje["nombre"] == nombre:
            encontrada = posicion
            aux_stack.push(personaje) 
            break
        else:
            posicion = posicion + 1
            aux_stack.push(personaje)

    while aux_stack.size() > 0:
        Personajes.push(aux_stack.pop())

    return encontrada

## la a)
print("La posicion de Groot es:", posicion_pj("Groot"))
print("La posicion de Rocket Raccoon es:", posicion_pj("Rocket Raccoon"))

def masdexpelis(x):
    aux_stack = Stack()
    encontrados = Stack()

    while Personajes.size() > 0:
        personaje = Personajes.pop()
        if personaje["peliculas"] > x:
            encontrados.push(personaje)
        aux_stack.push(personaje)

    while aux_stack.size() > 0:
        Personajes.push(aux_stack.pop())

    print("Personajes con más de", x, "películas:")
    while encontrados.size() > 0:
        print(encontrados.pop()["nombre"])



## la b)
print("Personajes con más de 5 películas:")
masdexpelis(5)



def cuantaspelis(nombre):
    aux_stack = Stack()
    pelis = None
    while Personajes.size() > 0:
        aux = Personajes.pop()
        if aux["nombre"] == nombre:
            pelis = aux["peliculas"]
            aux_stack.push(aux)
        else:
            aux_stack.push(aux)
    while aux_stack.size() > 0:
        Personajes.push(aux_stack.pop())
    return pelis

## la c)
print("La cantidad de películas de Black Widow es:", cuantaspelis("Black Widow"))

def buscar_letra_inicial(letra):
    aux_stack = Stack()
    pjs = Stack()
    while Personajes.size() > 0:
        personaje = Personajes.pop()
        if personaje["nombre"][0].lower() == letra.lower():
            pjs.push(personaje)
        aux_stack.push(personaje)

    while aux_stack.size() > 0:
        Personajes.push(aux_stack.pop())
    while pjs.size() > 0:
        print(pjs.pop()["nombre"])

## la d)
print("Personajes que empiezan con la letra 'c':")
buscar_letra_inicial("c")
print("Personajes que empiezan con la letra 'd':")
buscar_letra_inicial("d")
print("Personajes que empiezan con la letra 'g':")
buscar_letra_inicial("g")