from list_ import List

superheroes = List([
    {"nombre": "Linterna Verde", "anio": 1940, "casa": "DC", "bio": "Usa un anillo de poder y traje especial."},
    {"nombre": "Wolverine", "anio": 1974, "casa": "Marvel", "bio": "Posee garras de adamantium y factor curativo."},
    {"nombre": "Dr. Strange", "anio": 1963, "casa": "DC", "bio": "Hechicero supremo con capa levitante."},
    {"nombre": "Capitana Marvel", "anio": 1968, "casa": "Marvel", "bio": "Piloto con poderes cósmicos."},
    {"nombre": "Mujer Maravilla", "anio": 1941, "casa": "DC", "bio": "Princesa amazona con armadura y lazo de la verdad."},
    {"nombre": "Flash", "anio": 1940, "casa": "DC", "bio": "El hombre más rápido con traje rojo."},
    {"nombre": "Star-Lord", "anio": 1976, "casa": "Marvel", "bio": "Líder de los Guardianes con casco especial."},
    {"nombre": "Batman", "anio": 1939, "casa": "DC", "bio": "Detective enmascarado con traje negro."},
    {"nombre": "Spider-Man", "anio": 1962, "casa": "Marvel", "bio": "Héroe arácnido con traje rojo y azul."},
    {"nombre": "Superman", "anio": 1938, "casa": "DC", "bio": "Hombre de acero con traje azul y capa roja."},
])

## Criterios para ordenar/buscar
superheroes.add_criterion("nombre", lambda x: x["nombre"])
superheroes.add_criterion("anio", lambda x: x["anio"])
superheroes.add_criterion("casa", lambda x: x["casa"])

##a. eliminar el nodo que contiene la información de Linterna Verde;
superheroes.delete_value("Linterna Verde", "nombre")

##b. mostrar el año de aparición de Wolverine;
pos = superheroes.search("Wolverine", "nombre")
print("Año de aparición de Wolverine:", superheroes[pos]["anio"])

##c. cambiar la casa de Dr. Strange a Marvel;
pos = superheroes.search("Dr. Strange", "nombre")
if pos is not None:
    superheroes[pos]["casa"] = "Marvel"

##d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
for h in superheroes:
    if "traje" in h["bio"].lower() or "armadura" in h["bio"].lower():
        print(h["nombre"])

##e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
for h in superheroes:
    if h["anio"] < 1963:
        print(h["nombre"], "-", h["casa"])

##f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
for name in ["Capitana Marvel", "Mujer Maravilla"]:
    pos = superheroes.search(name, "nombre")
    if pos is not None:
        print(name, "es de", superheroes[pos]["casa"])

##g. mostrar toda la información de Flash y Star-Lord;
for name in ["Flash", "Star-Lord"]:
    pos = superheroes.search(name, "nombre")
    if pos is not None:
        print(superheroes[pos])


##h. listar los superhéroes que comienzan con la letra B, M y S;
for h in superheroes:
    if h["nombre"].startswith(("B", "M", "S")):
        print(h["nombre"])


##i. determinar cuántos superhéroes hay de cada casa de comic.
contador = {}
for h in superheroes:
    casa = h["casa"]
    contador[casa] = contador.get(casa, 0) + 1

print("Cantidad por casa:", contador)
