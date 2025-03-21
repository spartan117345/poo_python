# composición

"""una coordenada en dos dimensiones esta compuesta por dos valores, el valor en el eje de las x y el valor en el eje y, ésto podria ser una clase. un cuadrado esta compuesto por cuatro coordenadas que son los cuatro vertices, esto podria ser una clase que esta compuesta por cuatro clases del objeto coordenada."""

# clase coordenada

class Coordenada:
    # método constructor
    def __init__(self, x, y):
        # atributos privados
        self._X = x
        self._Y = y

    # método de lectura y escritura de cada atributo
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y

    def setX(self, x):
        self._X = x

    def setY(self, y):
        self._y = y

    
    # metodo para mostrar coordenada
    def MostrarCoordenada(self):
        print("(", self._X , ",", self._Y, ")")

# clase cuadrado

class Cuadrado:
    # método constructor
    def __init__(self, v1, v2, v3, v4):
        # métodos privados
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4
# métodos privados para mostrar los vertices
    def _MostrarCoordenadaV1(self):
        print("(", self.__V1.getX(), ",", self.__V1.getY(),")")
    
    def _MostrarCoordenadaV2(self):
        print("(", self.__V2.getX(), ",", self.__V2.getY(),")")
    
    def _MostrarCoordenadaV3(self):
        print("(", self.__V3.getX(), ",", self.__V3.getY(),")")
    
    def _MostrarCoordenadaV4(self):
        print("(", self.__V4.getX(), ",", self.__V4.getY(),")")


    # metodo para mostrar los vertices
    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.__V1.MostrarCoordenada()
        self.__V2.MostrarCoordenada()
        self.__V3.MostrarCoordenada()
        self.__V4.MostrarCoordenada()

# metodo principal
def main():
    # input
    x1 = int(input("dijite el valor de x: "))
    x2 = int(input("dijite el valor de y: "))

    c1 = Coordenada(x1,x2)
    c1.MostrarCoordenada()

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)

    cuadrado1 = Cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrarVertices()

if __name__ == "__main__":
    main()