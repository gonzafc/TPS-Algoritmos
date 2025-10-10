from tree import BinaryTree
jedi_list = [
    {
        "nombre": "Yoda",
        "especie": "Unknown",
        "nacimiento": -896,
        "sable": ["green"],
        "ranking": ["Jedi Master"],
        "maestros": []
    },
    {
        "nombre": "Luke Skywalker",
        "especie": "Human",
        "nacimiento": 19,
        "sable": ["green", "blue"],
        "ranking": ["Jedi Knight"],
        "maestros": ["Yoda", "Obi-Wan Kenobi"]
    },
    {
        "nombre": "Anakin Skywalker",
        "especie": "Human",
        "nacimiento": 41,
        "sable": ["blue"],
        "ranking": ["Jedi Knight"],
        "maestros": ["Obi-Wan Kenobi"]
    },
    {
        "nombre": "Obi-Wan Kenobi",
        "especie": "Human",
        "nacimiento": 57,
        "sable": ["blue"],
        "ranking": ["Jedi Master"],
        "maestros": ["Qui-Gon Jinn"]
    },
    {
        "nombre": "Ahsoka Tano",
        "especie": "Togruta",
        "nacimiento": 36,
        "sable": ["green", "yellow"],
        "ranking": ["Padawan"],
        "maestros": ["Anakin Skywalker"]
    },
    {
        "nombre": "Mace Windu",
        "especie": "Human",
        "nacimiento": 72,
        "sable": ["purple"],
        "ranking": ["Jedi Master"],
        "maestros": []
    },
    {
        "nombre": "Plo Koon",
        "especie": "Kel Dor",
        "nacimiento": 382,
        "sable": ["blue"],
        "ranking": ["Jedi Master"],
        "maestros": []
    },
    {
        "nombre": "Ki-Adi-Mundi",
        "especie": "Cerean",
        "nacimiento": 92,
        "sable": ["blue"],
        "ranking": ["Jedi Master"],
        "maestros": []
    },
    {
        "nombre": "Shaak Ti",
        "especie": "Togruta",
        "nacimiento": 59,
        "sable": ["blue"],
        "ranking": ["Jedi Master"],
        "maestros": []
    }
]

##a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
arbol_nombre = BinaryTree()
arbol_especie = BinaryTree()
arbol_ranking = BinaryTree()

for jedi in jedi_list:
    # clave por nombre
    arbol_nombre.insert(jedi["nombre"], jedi)
    # clave por especie (concateno nombre para que no choque si hay varios de la misma especie)
    arbol_especie.insert(jedi["especie"] + "_" + jedi["nombre"], jedi)
    # clave por ranking (igual, agrego nombre para unicidad)
    arbol_ranking.insert(jedi["ranking"][0] + "_" + jedi["nombre"], jedi)

##realizar un barrido inorden del árbol por nombre y ranking;
print("Barrido inorden por nombre:")
arbol_nombre.in_order()

print("\nBarrido inorden por ranking:")
arbol_ranking.in_order()

##c. realizar un barrido por nivel de los árboles por ranking y especie;
print("Por nivel (ranking):")
arbol_ranking.by_level()

print("\nPor nivel (especie):")
arbol_especie.by_level()

##d. mostrar toda la información de Yoda y Luke Skywalker;
nodo_yoda = arbol_nombre.search("Yoda")
nodo_luke = arbol_nombre.search("Luke Skywalker")

print("Info Yoda:", nodo_yoda.other_values)
print("Info Luke:", nodo_luke.other_values)

##e. mostrar todos los Jedi con ranking “Jedi Master”;
def listar_jedi_master(root):
    if root is not None:
        listar_jedi_master(root.left)
        if "Jedi Master" in root.other_values["ranking"]:
            print(root.value, root.other_values)
        listar_jedi_master(root.right)

listar_jedi_master(arbol_nombre.root)

##f. listar todos los Jedi que utilizaron sable de luz color verde;
def listar_sable_verde(root):
    if root is not None:
        listar_sable_verde(root.left)
        if "green" in root.other_values["sable"]:
            print(root.value, root.other_values)
        listar_sable_verde(root.right)

listar_sable_verde(arbol_nombre.root)

##g. listar todos los Jedi cuyos maestros están en el archivo;
def listar_con_maestros(root, arbol_nombres):
    if root is not None:
        listar_con_maestros(root.left, arbol_nombres)
        for maestro in root.other_values["maestros"]:
            if arbol_nombres.search(maestro):
                print(root.value, "tiene como maestro a", maestro)
        listar_con_maestros(root.right, arbol_nombres)

listar_con_maestros(arbol_nombre.root, arbol_nombre)

##h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
def listar_togruta_cerean(root):
    if root is not None:
        listar_togruta_cerean(root.left)
        if root.other_values["especie"] in ["Togruta", "Cerean"]:
            print(root.value, root.other_values)
        listar_togruta_cerean(root.right)

listar_togruta_cerean(arbol_nombre.root)

##i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.
def listar_por_nombre(root):
    if root is not None:
        listar_por_nombre(root.left)
        if root.value.startswith("A") or "-" in root.value:
            print(root.value, root.other_values)
        listar_por_nombre(root.right)

listar_por_nombre(arbol_nombre.root)

