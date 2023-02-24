'''
Los datos se pueden ocultar creando variables privadas. Solo la propia clase puede acceder a las variables privadas.
Si declara nombres con el formato __xxx o __xxx_yyy, estos es, con dos signos de subrayado antes de los nombres, 
el analizador Python automáticamente añadirá el nombre de clase al nombre declarado y creará las variables ocultas, 
por ejemplo:
'''

class MyClass:
    __attr = 10   #private class attribute

    def method1(self):
        pass

    def method2(self, p1, p2):
        pass

    def __privateMethod(self, text):
        self.__text = text    #private attribute

#A diferencia de Java, en Python todas las referencias a variables de instancia deben estar calificadas con self; no existe un uso implícito de this.

