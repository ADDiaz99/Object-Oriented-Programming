class User:
    id = ''
    name = ''
    document = ''
    email = ''
    password = ''


class Driver:
    id = ''
    name = ''
    document = ''
    email = ''
    password = ''

class Route:
    id = ''
    start:list[2]
    end:list[2]

class UberX:
    id = ''
    license = ''
    driver = ''
    passengers = ''
    brand = ''
    model = ''

class UberPool:
    id = ''
    license = ''
    driver = ''
    passengers = ''
    brand = ''
    model = ''

class UberBlack:
    id = ''
    license = ''
    driver = ''
    passengers = ''
    typecar_accepted = []

class UberVan:
    id = ''
    license = ''
    driver = ''
    passengers = ''
    typecar_accepted = []
    seats_material = []

class Card:
    id = ''
    number = ''
    cvv = ''
    date = ''

class Paypal:
    id = ''
    email = ''

class Cash:
    id = ''
    