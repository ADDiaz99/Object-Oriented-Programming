'''
En una clase Python, se pueden definir tanto variables como métodos. A diferencia de Java, en Python puede definir cualquier número de clases públicas por archivo de origen (o module). Por lo tanto, un módulo en Python puede considerarse similar a un paquete en Java.

En Python, las clases se definen utilizando la sentencia class. La sentencia class tiene el formato siguiente:
'''

class name (superclasses): statement

#Or

class name (superclasses): 
    assignment
    .
    .
    function
    .
    .

'''
Cuando define una clase tiene la opción de proporcionar cero o más sentencias assignment. 
Estos crean atributos de clase que comparten todas las instancias de la clase. 
Puede proporcionar cero o más definiciones de function. Estas definiciones de función crean métodos. 
La lista de superclases es opcional.

El nombre de clase debe ser exclusivo en el mismo ámbito, esto es, dentro de un módulo, función o clase. Puede definir varias variables para que hagan referencia a la misma clase.
'''