class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

def create_scoops():
    scoops = [Scoop('chocolate'), Scoop('vanilla'), Scoop('persimmon')]
    for scoop in scoops:
        print(scoop.flavor)
        
create_scoops()

class Beverage():
    def __init__(self, name, temperature = 0):
        self.name = name
        self.temperature = temperature

def create_beverages():
    beverages = [Beverage('coffee', 45), Beverage('water', 10), Beverage('soda', 5), Beverage('mystery liquid')]
    for beverage in beverages:
        print(beverage.name, beverage.temperature)
        
create_beverages()
