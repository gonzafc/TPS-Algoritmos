from jedi import Jedi
from list_ import List

jedis = List()
jedis.extend([
    Jedi("Yoda", "Desconocida", [], ["Verde"], "Jedi Master"),
    Jedi("Luke Skywalker", "Humano", ["Yoda"], ["Verde"], "Jedi Knight"),
    Jedi("Ahsoka Tano", "Togruta", ["Anakin Skywalker"], ["Verde", "Azul", "Blanco"], "Padawan"),
    Jedi("Kit Fisto", "Nautolano", ["Yoda"], ["Verde"], "Jedi Master"),
    Jedi("Qui-Gon Jin", "Humano", ["Conde Dooku"], ["Verde"], "Jedi Master"),
    Jedi("Mace Windu", "Humano", ["Cyslin Myr"], ["Violeta"], "Jedi Master"),
    Jedi("Obi-Wan Kenobi", "Humano", ["Qui-Gon Jin"], ["Azul"], "Jedi Master"),
    Jedi("Anakin Skywalker", "Humano", ["Obi-Wan Kenobi"], ["Azul", "Rojo"], "Jedi Knight"),
    Jedi("Plo Koon", "Kel Dor", ["Tyvokka"], ["Naranja", "Azul"], "Jedi Master"),
    Jedi("Shaak Ti", "Togruta", ["Yaddle"], ["Azul"], "Jedi Master"),
])

##a. listado ordenado por nombre y por especie;
print("Ordenados por nombre")
jedis.sort_by_criterion("nombre")
jedis.show()

print("Ordenados por especie")
jedis.sort_by_criterion("especie")
jedis.show()


##b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
print("Info de Ahsoka y Kit Fisto")
for jedi in jedis:
    if jedi.nombre in ["Ahsoka Tano", "Kit Fisto"]:
        print(jedi)

##c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
print("Padawans de Yoda y Luke")
for jedi in jedis:
    if "Yoda" in jedi.maestros or "Luke Skywalker" in jedi.maestros:
        print(jedi.nombre)

##d. mostrar los Jedi de especie humana y twi'lek;
print("Humanos y Twi'lek")
for jedi in jedis:
    if jedi.especie.lower() in ["humano", "twi'lek"]:
        print(jedi.nombre)

##e. listar todos los Jedi que comienzan con A;
print("Jedi que comienzan con A")
for jedi in jedis:
    if jedi.nombre.startswith("A"):
        print(jedi.nombre)

##f. mostrar los Jedi que usaron sable de luz de más de un color;
print("Jedi con más de un color")
for jedi in jedis:
    if len(jedi.colores) > 1:
        print(jedi.nombre, jedi.colores)

##g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
print("Jedi con sable amarillo o violeta")
for jedi in jedis:
    if "Amarillo" in jedi.colores or "Violeta" in jedi.colores:
        print(jedi.nombre, jedi.colores)

##h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
print("Padawans de Qui-Gon Jin y Mace Windu")
for jedi in jedis:
    if "Qui-Gon Jin" in jedi.maestros or "Mace Windu" in jedi.maestros:
        print(jedi.nombre, "cuyo maestro es ", jedi.maestros)

