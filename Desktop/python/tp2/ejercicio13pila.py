from clasestack import Stack 

trajes = Stack()

datos = [
    {"modelo": "Mark XLII", "pelicula": "Iron Man 3", "estado": "Destruido"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"},
    {"modelo": "Mark XLVI", "pelicula": "Capitan America: Civil War", "estado": "Impecable"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Dañado"},
    {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Destruido"},
]

for traje in datos:
    trajes.push(traje)

def buscar_traje(modelo):
    aux_stack = Stack()
    encontrado = False

    while trajes.size() > 0:
        traje = trajes.pop()
        if traje["modelo"] == modelo:
            encontrado = True
            break
        aux_stack.push(traje)

    while aux_stack.size() > 0:
        trajes.push(aux_stack.pop())

    return encontrado, traje if encontrado else None

def mostrar_daniados(trajes):
    aux = Stack()
    daniados = []

    while trajes.size() > 0:
        traje = trajes.pop()
        if traje["estado"] == "Dañado":
            daniados.append(traje)
        aux.push(traje)

    while aux.size() > 0:
        trajes.push(aux.pop())

    return daniados

def eliminar_destruidos(trajes):
    aux = Stack()

    while trajes.size() > 0:
        traje = trajes.pop()
        if traje["estado"] == "Destruido":
            print(f"Eliminado: {traje['modelo']}")
        else:
            aux.push(traje)

    while aux.size() > 0:
        trajes.push(aux.pop())
        
        
def poner_trajes(trajes):
    print("ingrese el modelo del traje, luego la pelicula en la que fue usado y luego el estado en el que quedo al final de la pelicula:")
    modelo = input("Modelo: ")
    pelicula = input("Película: ")
    estado = input("Estado: ")
    traje = {"modelo": modelo, "pelicula": pelicula, "estado": estado}
    trajes.push(traje)

##añadir trajes
print("desea añadir un traje? (s/n)")
respuesta = input()
while respuesta.lower() == "s":
    if respuesta.lower() == "s":
        poner_trajes(trajes)
    print ("desea añadir otro traje? (s/n)")
    respuesta = input()


##añadir Mark LXXXV si no esta en la misma peli
trajeaux = {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Impecable"}
aux = Stack()
existe = False

while trajes.size() > 0:
    traje = trajes.pop()
    if traje["modelo"] == trajeaux["modelo"] and traje["pelicula"] == trajeaux["pelicula"]:
        existe = True
    aux.push(traje)

while aux.size() > 0:
    trajes.push(aux.pop())

if existe:
    print("El traje Mark LXXXV ya existe en la misma película.")
else:
    trajes.push(trajeaux)
    print("se agrego el traje Mark LXXXV")

##buscar trajes en homecoming y civil war
while trajes.size() > 0:
    traje = trajes.pop()
    if traje["pelicula"] == "Spider-Man: Homecoming":
        print(f"Traje encontrado en Homecoming: {traje}")
    elif traje["pelicula"] == "Capitan America: Civil War":
        print(f"Traje encontrado en Civil War: {traje}")
    aux.push(traje)
while aux.size() > 0:
    trajes.push(aux.pop())

##buscar dañados
trajes_daniados = mostrar_daniados(trajes)
if trajes_daniados:
    print("Trajes dañados encontrados:")
    for traje in trajes_daniados:
        print(f" {traje}")
else:
    print("No se encontraron trajes dañados.")

##buscar hulkbuster
encontrado, traje = buscar_traje("Mark XLIV")
if encontrado:
    print(f"El Hulkbuster fue encontrado: {traje}")
else: 
    print("El Hulkbuster no fue encontrado")

##sacar destruidos
eliminar_destruidos(trajes)