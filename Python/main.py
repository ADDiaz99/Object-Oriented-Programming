from car import *
from account import Account


if __name__ == "__main__":
    print('Hola Python!')

    car = Car("TRA456", Account("Martin Fierro", "1204572314"))
    car.passenger = 3
    print(vars(car))
    print(vars(car.driver))

    car2 = Car("DWA789", Account("Jack Daniels","10245877568"))
    car2.passenger = 2
    print(vars(car2))
    print(vars(car2.driver))
    
    car3 = Car("EYY469", Account("Armando Mendoza","14526354566"))
    car3.passenger = 4
    print(vars(car3))
    print(vars(car3.driver))
    