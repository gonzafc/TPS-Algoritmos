from clasecola import Cola

cola_mcu = Cola()

cola_mcu.arrive({"nombre": "Tony Stark", "superheroe": "Iron Man", "genero": "M"})
cola_mcu.arrive({"nombre": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"})
cola_mcu.arrive({"nombre": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"})
cola_mcu.arrive({"nombre": "Thor Odinson", "superheroe": "Thor", "genero": "M"})
cola_mcu.arrive({"nombre": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"})
cola_mcu.arrive({"nombre": "Wanda Maximoff", "superheroe": "Scarlet Witch", "genero": "F"})
cola_mcu.arrive({"nombre": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"})

def buscar_nombre_por_apodo(apodo):
    cola_aux = Cola()
    while cola_mcu.size() > 0:
        personaje = cola_mcu.attention()
        cola_aux.arrive(personaje)
        if personaje["superheroe"] == apodo:
            print(f"{personaje['nombre']}")
    while cola_aux.size() > 0:
        cola_mcu.arrive(cola_aux.attention())
        
##nombre de capitana marvel
print("Nombre de Capitana Marvel:")
buscar_nombre_por_apodo("Capitana Marvel")

def buscar_nombre_por_genero(genero):
    colaaux = Cola()
    while cola_mcu.size() > 0:
        personaje = cola_mcu.attention()
        colaaux.arrive(personaje)
        if personaje["genero"] == genero:
            print(f"{personaje['nombre']}")
    while colaaux.size() > 0:
        cola_mcu.arrive(colaaux.attention())

##nombre superheroes mujeres y hombres
print("")
print("Nombres de superheroes mujeres:")
buscar_nombre_por_genero("F")
print("")
print("Nombres de superheroes hombres:")
buscar_nombre_por_genero("M")

def buscar_apodo_por_nombre(nombre):
    colaaux = Cola()
    while cola_mcu.size() > 0:
        personaje = cola_mcu.attention()
        colaaux.arrive(personaje)
        if personaje["nombre"] == nombre:
            print(f"{personaje['superheroe']}")
    while colaaux.size() > 0:
        cola_mcu.arrive(colaaux.attention())
        
##buscar apodo de scott lang
print("")
print("Apodo de Scott Lang:")
buscar_apodo_por_nombre("Scott Lang")

def datos_por_inicial(inicial):
    colaaux = Cola()
    while cola_mcu.size() > 0:
        personaje = cola_mcu.attention()
        colaaux.arrive(personaje)
        if personaje["nombre"].startswith(inicial.upper()):
            print(f"Nombre: {personaje['nombre']}, Apodo: {personaje['superheroe']}, Genero: {personaje['genero']}")
    while colaaux.size() > 0:
        cola_mcu.arrive(colaaux.attention())
        
##mostrar datos de personajes que empiezan con la letra s
print("")
print("Datos de personajes que empiezan con la letra S:")
datos_por_inicial("S")

def determinar_si_esta(nombre):
    colaaux = Cola()
    while cola_mcu.size() > 0:
        personaje = cola_mcu.attention()
        colaaux.arrive(personaje)
        if personaje["nombre"] == nombre:
            print(f"El personaje {nombre} está en la cola y su nombre de superhéroe es {personaje['superheroe']}")
    while colaaux.size() > 0:
        cola_mcu.arrive(colaaux.attention())
        
##verificar si está el personaje Carol Danvers
print("")
print("Verificar si está el personaje Carol Danvers:")
determinar_si_esta("Carol Danvers")