# clase de persona

class persona:
    # metodo costructor
    def __init__(self, Nombre, Apellidos, Edad):
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Edad = Edad

    # metod para mostrar 
    def Mostrarpersona(self):
        print("nombre" + self.Nombre)
        print("apellido" + self.Apellidos)
        print("edad" + str(self.Edad))

# metodo principal
def main():
    p1 = persona(" julian", " sanchez",  14)
    p1.Mostrarpersona()
    p2 = persona(" oscar", " sanchez",  16)
    p2.Mostrarpersona()
    p1.Edad =  20
    p1.Mostrarpersona()
    p1 = p2
    p1.Mostrarpersona()
    p2.Mostrarpersona()

if __name__ == "__main__":
    main()