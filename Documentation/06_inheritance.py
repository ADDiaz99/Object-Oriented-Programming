'''
La posibilidad de herencia de las clases es fundamental en la programación orientada a objetos. 
Python da soporte a la herencia individual y múltiple. Herencia individual significa que solo puede haber una superclase. 
Herencia múltiple significa que puede haber más de una superclase.

La herencia se implementa generando subclases de otras clases. Cualquier número de clases Python pueden ser superclases. 
En la implementación de Jython en Python, solo se puede heredar directa o indirectamente de una clase Java. 
No es necesario suministrar una superclase.

Cualquier atributo o método de una superclase también está en cualquier subclase y lo puede utilizar la propia clase o cualquier cliente, 
siempre que el atributo o método no esté oculto. Se puede utilizar cualquier instancia de una subclase; 
esto se denomina polimorfismo. Estas características permiten la reutilización y facilitan la extensión.
'''
#Ejemplo

class Class1: pass    #no inheritance

class Class2: pass

class Class3(Class1): pass     #single inheritance

class Class4(Class3, Class2): pass     #multiple inheritance