# poo en python
introduccion a la poo en python

- el paradigam de POO esta basado en una abstraccion del mundo real que nos va a permitir desarrolar programas de forma mas cercana a como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos.

## clase

- una clase es un tipo de dato cuyas variables se llaman objtos o instancias
- la clase es el concepto del mundo real y los objetos o instancias son el propio objeto del mundo real.
- las clases estan compuestas por dos elementos: atributos y métodos.

### atributos 
- los atributos son informacion que almacena la clase

### métodos
- operaciones que pueden realizar las clases

## definicion de una clase en python 
```python
class nombreclase: 
    def __init__(self, variable1, variable2): 
        self.atributo1 = valor1 
        self.atributo2 = valor2 

def nombremetodo(self) 
    bloquecodigo 
```

### componentes


```class```: palabra reservada en python para definir una clase.

```NombreClase```:nombre de la clase que quieres crear.

```def```: palabra reservada en python que se utiliza para definir tanto el construcctor de la clase(método que se ejecuta la primera vez que usas una clase) como los diferentes métodos que tiene.

```__init__```: palabra reservada en python para definir el metodo constructor de la clase. Es lo primero que se ejecuta cuando creas un objeto de una clase.

```(self, variableX)```: parámetro del constructor de la clase. El parámetro self es obligatorio y despues puedes tener tantos parámetros como quieras. La forma de añadir parámetros es la misma que en las funciones.

```self.atributoX```: forma de utilización y acceso a los atributos de la clase.

```nombremetodo```: nombre del metodo de la clase.

```(self)```: parámetro del método. el parámetro self es obligatorio y despúes puedes tener tantos parámetros como quieras. la forma de añadir parámetros es la misma que en las funciones.

```bloquecodigo```: instrucciones que ejecutara el método.

- cuando defines una clase debes tener en cuenta los siguientes puntos:
  - puedes definir tantos atributos como necesites.
  - puedes definir tantos metodos como necesites.
  - puede definir tantos parametros en el constructor y en los metodos como necesites.