# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        raise NotImplementedError("Subclase debe implementar este método")

# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, raza):
        # Llamamos al constructor de la clase base
        super().__init__(nombre)
        self.raza = raza

    # Sobrescribimos el método hacer_sonido
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Guau!"

# Crear un objeto de la clase Perro
mi_perro = Perro("Rex", "Labrador")

print(mi_perro.nombre)  # Accede a un atributo heredado
print(mi_perro.raza)    # Atributo de la clase Perro
print(mi_perro.hacer_sonido())  # Método sobrescrito