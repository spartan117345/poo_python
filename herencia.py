# Clase Persona
class Persona:
    
    # Método constructor
    def __init__(self):
        self.__Nombre = ""
        self.__Apellidos = ""
        self.__Edad = 0
        self.__Telefono = ""  # Atributo teléfono

    def getNombre(self):
        return self.__Nombre
    
    def setNombre(self, nombre):
        self.__Nombre = nombre

    def getApellidos(self):
        return self.__Apellidos
    
    def setApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def getEdad(self):
        return self.__Edad
    
    def setEdad(self, edad):
        self.__Edad = edad

    def getTelefono(self):
        return self.__Telefono
    
    def setTelefono(self, telefono):
        self.__Telefono = telefono

    # Método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.__Nombre)
        print("Apellidos: " + self.__Apellidos)
        print("Edad: " + str(self.__Edad))
        print("Teléfono: " + self.__Telefono)

# Clase Alumno hereda de Persona
class Alumno(Persona):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base Persona
        self.__Curso = ""
        self.__Asignaturas = []

    def getCurso(self):
        return self.__Curso
    
    def setCurso(self, curso):
        self.__Curso = curso

    def getAsignaturas(self):
        return self.__Asignaturas
    
    def setAsignaturas(self, asignaturas):
        if isinstance(asignaturas, list):  # Verificamos que asignaturas sea una lista
            self.__Asignaturas = asignaturas
        else:
            print("Error: Asignaturas debe ser una lista.")

    def mostrarAlumno(self):
        print("Alumno:")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tTeléfono: ", self.getTelefono())
        print("\tCurso: ", self.__Curso)
        print("\tMatrículas: ", ", ".join(self.__Asignaturas))

# Clase Profesor hereda de Persona
class Profesor(Persona):
    def __init__(self):
        super().__init__()
        self.__Tutoria = ""
        self.__Antiguedad = 15

    def getTutoria(self):
        return self.__Tutoria

    def setTutoria(self, tutoria):
        self.__Tutoria = tutoria

    def getAntiguedad(self):
        return self.__Antiguedad

    def setAntiguedad(self, antiguedad):
        self.__Antiguedad = antiguedad

    def mostrarProfesor(self):
        print("Profesor:")
        print("\tNombre: ", self.getNombre())
        print("\tApellidos: ", self.getApellidos())
        print("\tEdad: ", self.getEdad())
        print("\tTeléfono: ", self.getTelefono())
        print("\tTutoria: ", self.__Tutoria)
        print("\tAntiguedad: ", self.__Antiguedad, "años")

# Método principal
def main():
    # Crear un alumno
    alumno = Alumno()
    alumno.setNombre("Néstor")
    alumno.setApellidos("Páez Sarmiento")
    alumno.setEdad(25)
    alumno.setTelefono("123-456-789")
    alumno.setCurso("Bachillerato")
    alumno.setAsignaturas(["Matemáticas", "Tecnología", "Inglés"])
    alumno.mostrarAlumno()

    # Crear un profesor
    profesor = Profesor()
    profesor.setNombre("Nesticor")
    profesor.setApellidos("Páez Sarmiento")
    profesor.setEdad(40)
    profesor.setTelefono("987-654-321")
    profesor.setTutoria("Matemáticas")
    profesor.setAntiguedad(15)
    profesor.mostrarProfesor()

if __name__ == "__main__":
    main()