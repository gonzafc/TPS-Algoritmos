from info_superheroes import superheroes
from lista import Lista
from cola import Cola


listaSuperHeroes = Lista()

class Superhero:
    
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain
        
    def __str__(self):
        return f"{self.name} ,{self.alias}, {self.real_name}, {self.first_appearance}, {self.is_villain}" #no le puse el short_bio porque se hace muy largo el print


for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    listaSuperHeroes.append(hero)


#listar a los superheroes de manera ascendente por nombre

def sacarNombre(hero):
    """"sirve para sacar el atributo nombre del objeto hero"""
    if hero.name is not None:
        return hero.name
    else:
        return "no tiene nombre puesto en la lista" # por esto, no va a mostrar a los que no tienen el nombre lleno en la lista

listaSuperHeroes.add_criterion("name", sacarNombre)
listaSuperHeroes.sort_by_criterion("name")
listaSuperHeroes.show()

#Determinar en que posicion esta The Thing y Rocket Raccoon. (la lista ya esta ordenada por nombre, asi que la posición varía de su posición original)
print("")
pos = listaSuperHeroes.search('The Thing', 'name')
if pos is not None:
    print(f"The Thing esta en la posicion: {pos}")
else:
    print("The Thing no esta en la lista")
    
pos = listaSuperHeroes.search('Rocket Raccoon', 'name')
if pos is not None:
    print(f"Rocket Raccoon esta en la posicion: {pos}")
else:
    print("Rocket Raccoon no esta en la lista")

#listar villanos
print("")
print("Villanos:")

for hero in listaSuperHeroes:
    if hero.is_villain:
        print(hero)
        
#poner villanos en una cola
colaVillanos = Cola()

for hero in listaSuperHeroes:
    if hero.is_villain:
        colaVillanos.arrive(hero)
        
#ver que villanos aparecieron antes de 1980
colaVillanos1980 = Cola()

while colaVillanos.size() > 0:
    villano = colaVillanos.attention()
    if villano.first_appearance < 1980:
        colaVillanos1980.arrive(villano)   
        
print("")
print("Villanos que aparecieron antes de 1980:")
while colaVillanos1980.size() > 0:
    villano = colaVillanos1980.attention()
    print(villano)

#listar los heroes que empiezan con Bi, G, My, W
print("")
print("Heroes que empiezan con Bi, G, My, W:")
for hero in listaSuperHeroes:
    if hero.name.startswith(('Bi', 'G', 'My', 'W')):
        print(hero)

#listar a los superheroes de manera ascendente por nombre real

def sacarRealName(hero):
    """"sirve para sacar el atributo real_name del objeto hero"""
    if hero.real_name is not None:
        return hero.real_name
    else:
        return "no tiene nombre puesto en la lista" # por a esto, no va a mostrar a los que no tienen el nombre real lleno en la lista

print("")
listaSuperHeroes.add_criterion("real_name", sacarRealName)
listaSuperHeroes.sort_by_criterion("real_name")
listaSuperHeroes.show()

#lista en orden de aparicion

def sacarFirstAppearance(hero):
    """"sirve para sacar el atributo first_appearance del objeto hero"""
    if hero.first_appearance is not None:
        return hero.first_appearance
    else:
        return 0  # por esto, no va a mostrar a los que no tienen el año de primera aparicion lleno en la lista

print("")
listaSuperHeroes.add_criterion("first_appearance", sacarFirstAppearance)
listaSuperHeroes.sort_by_criterion("first_appearance")
listaSuperHeroes.show()

#modificar el nombre real de antman a scott lang
print("")
index = listaSuperHeroes.search('Ant Man', 'name')
if index:
    print(listaSuperHeroes[index].real_name)
    listaSuperHeroes[index].real_name = "Scott Lang"
    print(listaSuperHeroes[index].real_name)
else:
    print('el superheroe no esta en la lista')

#Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit
print("")
for hero in listaSuperHeroes:
    if "time-traveling" in hero.short_bio or "suit" in hero.short_bio:
        print(hero)

#Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.
print("")
heroeaBorrar = listaSuperHeroes.delete_value('Electro', 'name')
if heroeaBorrar is not None:
    print(f"Se ha eliminado a {heroeaBorrar.name} de la lista, su informacion era:")
    print(heroeaBorrar)
else:
    print("Electro no estaba en la lista.")
    
heroeaBorrar = listaSuperHeroes.delete_value('Baron Zemo', 'name')

print("")

if heroeaBorrar is not None:
    print(f"Se ha eliminado a {heroeaBorrar.name} de la lista, su informacion era:")
    print(heroeaBorrar)
else:
    print("Baron Zemo no estaba en la lista.")