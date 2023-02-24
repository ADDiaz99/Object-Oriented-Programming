'''
Cualquier variable enlazada a una clase es un atributo de clase. Cualquier función definida en una clase es un método. 
Los métodos reciben como primer argumento una instancia de la clase, que convencionalmente se denomina self. 
Por ejemplo, para definir algunos atributos de clase y métodos, puede entrar el siguiente código:
'''
class MyClass:
    attr1 = 10        #class attributes
    attr2 = "hello"

    def method1(self):
        print(MyClass.attr1)   #reference the class attribute

    def method2(self):
        print(MyClass.attr2)   #reference the class attribute

    def method3(self, text):
        self.text = text        #instance attribute
        print(text, self.text)   #print my argument and my attribute

    method4 = method3   #make an alias for method3

'''
Dentro de una clase, debe cualificar todas las referencias a los atributos de clase con el nombre de clase;
por ejemplo, MyClass.attr1. 
Todas las referencias a los atributos de la instancia deben cualificarse con la variable self, por ejemplo, self.text. 
Fuera de la clase, debe cualificar todas las referencias a los atributos de clase con el nombre de clase (por ejemplo, MyClass.attr1) 
o con una instancia de la clase (por ejemplo, x.attr1, donde x es una instancia de la clase). 
Fuera de la clase, todas las referencias a las variables de la instancia deben cualificarse con una instancia de la clase, por ejemplo, x.text.
'''