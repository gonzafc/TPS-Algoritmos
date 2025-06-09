from lista import Lista # Fijese profe que la clase es Lista, y no List, lo cambie porque me confundia con list de python
listaSuperHeroes = Lista()
superheroes = [
    {
        "name": "Kang",
        "alias": "Kang the Conqueror",
        "real_name": "Nathaniel Richards",
        "short_bio": "Kang the Conqueror is a time-traveling warlord who has battled many heroes, especially the Avengers. He is known for his mastery of advanced technology and his ability to manipulate time.",
        "first_appearance": 1964,
        "is_villain": True
    },
    {
        "name": "Hulk",
        "alias": "The Hulk",
        "real_name": "Bruce Banner",
        "short_bio": "Hulk is a gamma-powered superhero with incredible strength and durability. He transforms into a green giant when angered or stressed.",
        "first_appearance": 1962,
        "is_villain": False
    },
    {
        "name": "Black Widow",
        "alias": "Natasha Romanoff",
        "real_name": "Natasha Romanoff",
        "short_bio": "Black Widow is a highly trained spy and former assassin with exceptional skills in hand-to-hand combat and espionage.",
        "first_appearance": 1964,
        "is_villain": False
    },
    {
        "name": "Black Cat",
        "alias": "Felicia Hardy",
        "real_name": "Felicia Hardy",
        "short_bio": "Black Cat is a skilled burglar with a unique power that brings bad luck to her enemies. She often operates in the gray area between hero and villain.",
        "first_appearance": 1979,
        "is_villain": True
    },
    {
        "name": "Iron Man",
        "alias": "Iron Man",
        "real_name": "Tony Stark",
        "short_bio": "A billionaire inventor who built a powered suit of armor to save his life and became a founding Avenger.",
        "first_appearance": 1963,
        "is_villain": False
    },
    {
        "name": "Magneto",
        "alias": "Master of Magnetism",
        "real_name": "Max Eisenhardt",
        "short_bio": "A powerful mutant with control over magnetic fields, often portrayed as an adversary to the X-Men, though with complex motivations.",
        "first_appearance": 1963,
        "is_villain": True
    },
    {
        "name": "Storm",
        "alias": "Storm",
        "real_name": "Ororo Munroe",
        "short_bio": "A mutant with the ability to manipulate weather, known for her leadership in the X-Men and her strong moral compass.",
        "first_appearance": 1975,
        "is_villain": False
    },
    {
        "name": "Venom",
        "alias": "Venom",
        "real_name": "Eddie Brock",
        "short_bio": "A journalist who bonds with an alien symbiote to become the anti-hero Venom, often torn between vengeance and justice.",
        "first_appearance": 1988,
        "is_villain": True
    },
    {
        "name": "Scarlet Witch",
        "alias": "Scarlet Witch",
        "real_name": "Wanda Maximoff",
        "short_bio": "A mutant with chaos magic and reality-warping powers, known for her complex role as both hero and threat.",
        "first_appearance": 1964,
        "is_villain": False
    },
    {
        "name": "Abomination",
        "alias": "Abomination",
        "real_name": "Emil Blonsky",
        "short_bio": "A former KGB agent who transforms into a gamma-powered monster and becomes one of Hulk's main enemies.",
        "first_appearance": 1967,
        "is_villain": True
    },
    {
        "name": "Adam Warlock",
        "alias": "Adam Warlock",
        "real_name": "Adam Warlock",
        "short_bio": "An artificially created perfect human who becomes a cosmic protector and wielder of the Soul Gem.",
        "first_appearance": 1967,
        "is_villain": False
    },
    {
        "name": "Angel",
        "alias": "Angel",
        "real_name": "Warren Worthington III",
        "short_bio": "A founding member of the X-Men with large feathered wings that allow him to fly.",
        "first_appearance": 1963,
        "is_villain": False
    },
    {
        "name": "Annihilus",
        "alias": "Annihilus",
        "real_name": "Annihilus",
        "short_bio": "A powerful insectoid ruler from the Negative Zone, obsessed with extending his lifespan.",
        "first_appearance": 1968,
        "is_villain": True
    },
    {
        "name": "Ant Man",
        "alias": "Ant Man",
        "real_name": "Hank Pym",
        "short_bio": "A brilliant scientist who discovered Pym Particles and became a size-changing superhero.",
        "first_appearance": 1962,
        "is_villain": False
    },
    {
    "name": "Apocalypse",
    "alias": "Apocalypse",
    "real_name": "En Sabah Nur",
    "short_bio": "One of the first mutants, Apocalypse believes in survival of the fittest and has enhanced his body over millennia with alien technology.",
    "first_appearance": 1986,
    "is_villain": True
    }
]

class Superhero:
    
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain
        
    def __str__(self):
        return f"{self.name}, {self.real_name} - {self.is_villain}"
    
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
    
def buscarSuperHeroe(Lista, nombre, i=0): 
    """Busca un superhéroe por su nombre en la lista de superhéroes de forma recursiva.
    Args:
        Lista (List): lista de los superheroes.
        nombre (str): nombre del heroe que se busca.
        i (int): la posicion en cada bucle.
    Returns:
        bool: True si encuentra al heroe, False si no.
    """
    if i >= len(Lista):
        return False
    if Lista[i].name == nombre:
        return True
    return buscarSuperHeroe(Lista, nombre, i + 1) 

# buscar a capitan america
nombre = "Capitan America"
encontrado = buscarSuperHeroe(listaSuperHeroes, nombre)
if encontrado:
    print(f"{nombre} encontrado en la lista de superheroes.")
else:
    print(f"{nombre} no encontrado en la lista de superheroes.")

def listarSuperHeroes(Lista, i=0):
    """ Lista todos los superhéroes de la lista de forma recursiva.
    Args:
        Lista (List): lista de los superheroes.
        i (int): la posicion en cada bucle.
    """
    if i >= len(Lista):
        return
    print(Lista[i])
    listarSuperHeroes(Lista, i + 1)

# todos los heroes:
listarSuperHeroes(listaSuperHeroes)