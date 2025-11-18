from tree import BinaryTree
from pokemondata import pokemon_list

## Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total)
## de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega
## evolucion (bool) y si tiene forma gigamax (bool) para el cual debemos construir
## tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:

#los índices de cada uno de los árboles deben ser nombre, número y tipo;
tree_nombre = BinaryTree()
tree_numero = BinaryTree()
tree_tipo = BinaryTree()

for pokemon in pokemon_list:
    
    tree_nombre.insert(pokemon['name'], pokemon) 
    tree_numero.insert(pokemon['number'], pokemon)

    for tipo in pokemon['types']:
        
        nodo_tipo = tree_tipo.search(tipo) #se busca si existe el tipo para que no hayan tipos repetidos
        
        if nodo_tipo is None:
            tree_tipo.insert(tipo, {'lista_pokemon': [pokemon]})
        else:
            nodo_tipo.other_values['lista_pokemon'].append(pokemon)

##mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último,
##la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los 
## Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
def buscar_pokemon_por_numero (numero):
    nodo = tree_numero.search(numero)
    if nodo is not None:
        return nodo.other_values
    else:
        return None

print ("Buscar Pokémon por número 25:")
print (buscar_pokemon_por_numero (25))

def buscar_pokemon_por_nombre_proximidad (tree_nombre, nombre_parcial):
    resultados = []
    nombre_parcial_minuscula = nombre_parcial.lower()
    def recorrido_proximidad(root):
        if root is not None:
            recorrido_proximidad(root.left)
            if nombre_parcial_minuscula in root.value.lower():
                resultados.append(root.other_values)
            recorrido_proximidad(root.right)
    recorrido_proximidad(tree_nombre.root)
    return resultados

print ("\nBuscar Pokémon por nombre con proximidad 'bul':")
resultados_proximidad = buscar_pokemon_por_nombre_proximidad (tree_nombre, "bul")
for resultado in resultados_proximidad:
    print (resultado)

#mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
def listar_pokemons_por_tipo (tree_tipo, tipo_buscado):
    nodo_tipo = tree_tipo.search(tipo_buscado)
    if nodo_tipo is not None:
        return [pokemon['name'] for pokemon in nodo_tipo.other_values['lista_pokemon']]
    else:
        return []
    
print ("\nListar Pokémons por tipo 'Fire':")
pokemons_fuego = listar_pokemons_por_tipo (tree_tipo, "Fire")
for nombre in pokemons_fuego:
    print (nombre)
print ("\nListar Pokémons por tipo 'Ghost':")
pokemons_fantasma = listar_pokemons_por_tipo (tree_tipo, "Ghost")
for nombre in pokemons_fantasma:
    print (nombre)
print ("\nListar Pokémons por tipo 'Steel':")
pokemons_acero = listar_pokemons_por_tipo (tree_tipo, "Steel")
for nombre in pokemons_acero:
    print (nombre)
print ("\nListar Pokémons por tipo 'Electric':")
pokemons_electrico = listar_pokemons_por_tipo (tree_tipo, "Electric")
for nombre in pokemons_electrico:
    print (nombre)

#realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;

print ("\nListado en orden ascendente por número:")
tree_numero.in_order()

print ("\nListado en orden ascendente por nombre:")
tree_nombre.in_order()

print ("\nListado por nivel por nombre:")
tree_nombre.by_level()

#mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;

def tipos_del_pokemon (tree_nombre, pokemon_nombre):
    pokemon = tree_nombre.search(pokemon_nombre)
    if pokemon is not None:
        return pokemon.other_values['types']
    else:
        return None
def encontrar_pokemon_debil (tree_nombre, tipos):
    pokemon_debiles = []
    def recorrido(root):                 ##hice otra función porque el recorrido in_order que
        if root is not None:             ##esta definido en tree imprime el nombre de todos los pokemon
            recorrido(root.left)         ##que recorre, y no quería eso.
            for debilidad in root.other_values['weaknesses']:
                if debilidad in tipos:
                    pokemon_debiles.append(root.other_values['name'])
                    break ##para no agregar el mismo pokemon mas de una vez
            recorrido(root.right)
    recorrido(tree_nombre.root)
    return pokemon_debiles

print ("\nPokémons débiles frente a Jolteon, Lycanroc y Tyrantrum:")
tipos_jolteon = tipos_del_pokemon (tree_nombre, "Jolteon")
tipos_lycanroc = tipos_del_pokemon (tree_nombre, "Lycanroc")
tipos_tyrantrum = tipos_del_pokemon (tree_nombre, "Tyrantrum")
debilidades_a_buscar = set(tipos_jolteon + tipos_lycanroc + tipos_tyrantrum)
print (encontrar_pokemon_debil (tree_nombre, debilidades_a_buscar))

#mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;

def contar_pokemons_por_tipo (tree_tipo):
    tipo_y_cantidad = {}
    def recorrido(root):
        if root is not None:
            recorrido(root.left)
            tipo_y_cantidad[root.value] = len(root.other_values['lista_pokemon'])
            recorrido(root.right)
    recorrido(tree_tipo.root)
    return tipo_y_cantidad

print ("\nCantidad de Pokémons por tipo:")
cantidad_por_tipo = contar_pokemons_por_tipo (tree_tipo)
if cantidad_por_tipo:
    for tipo, cantidad in cantidad_por_tipo.items():
        print(f"  - Tipo: {tipo}, Cantidad: {cantidad}")
else:
    print("  (No se encontraron tipos)")

#determinar cuantos Pokémons tienen megaevolucion.
def contar_pokemon_con_megaevolucion (tree_nombre):
    contador = 0
    def recorrido(root):
        nonlocal contador  #si no le aviso que contador es nonlocal, da error cuando se quiere sumar +1
        if root is not None:
            recorrido(root.left)
            if root.other_values['mega']:
                contador += 1
            recorrido(root.right)
        return contador
    return recorrido(tree_nombre.root)
print ("Cantidad de Pokémons con megaevolución:")
cantidad_megaevolucion = contar_pokemon_con_megaevolucion (tree_nombre)
print (cantidad_megaevolucion)

#determinar cuantos Pokémons tiene forma gigamax.
def contar_pokemon_con_gigamax (tree_nombre):
    contador = 0
    def recorrido(root):
        nonlocal contador
        if root is not None:
            recorrido(root.left)
            if root.other_values['gigamax']:
                contador += 1
            recorrido(root.right)
        return contador
    return recorrido(tree_nombre.root)
print ("Cantidad de Pokémons con forma Gigamax:")
cantidad_gigamax = contar_pokemon_con_gigamax (tree_nombre)
print (cantidad_gigamax)