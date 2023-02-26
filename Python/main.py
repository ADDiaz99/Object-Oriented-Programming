from car import *


if __name__ == "__main__":
    print('Hola Python!')

    car = Car()
    car.license = 'TRA456'
    car.driver = 'Martin Fierro'
    car.passenger = 3
    print(vars(car))

    car2 = Car()
    car2.license = 'DWA789'
    car2.driver = 'Jack Daniels'
    car2.passenger = 2
    print(vars(car2))
    
    car3 = Car()
    car3.license = 'EYY469'
    car3.driver = 'Armando Mendoza'
    car3.passenger = 4
    print(vars(car3))
    