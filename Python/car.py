from account import Account

class Car:
    id          = int
    license     = str
    passenger   = int
    driver      = Account("","")

    def __init__(self,license, driver):
        self.license = license
        self.driver = driver