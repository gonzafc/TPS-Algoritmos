class Jedi:
    def __init__(self, nombre, especie, maestros, colores, ranking=None):
        self.nombre = nombre
        self.especie = especie
        self.maestros = maestros        # lista de strings
        self.colores = colores          # lista de strings
        self.ranking = ranking          # opcional

    def __str__(self):
        return (f"Nombre: {self.nombre}, Especie: {self.especie}, "
                f"Maestros: {', '.join(self.maestros)}, "
                f"Sables: {', '.join(self.colores)}")
