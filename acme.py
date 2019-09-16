import random

class Product():
    def __init__(self, name, price = 10, weight = 20,
    flamibility = 0.5, identifier = random.randint(100000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flamibility = flamibility
        self.identifier = identifier
    
    def stealability(self):
        theft = (self.price/self.weight)
        if theft < 0.5:
            return(theft, 'Not so stealable...')
        elif theft >= 0.5 and theft < 1.0:
            return(theft, "Kinda stealable.")
        else:
            return(theft, "Very stealable!")

    def explode(self):
        boom = (self.flamibility*self.weight)
        if boom < 10:
            return('...fizzle.')
        elif boom >= 10 and boom < 50:
            return('...boom!')
        else:
            return('...BABOOM!')

class BoxingGlove(Product):
    def __init__(self, name, price = 10, weight = 10,
    flamibility = 0.5, identifier = random.randint(100000, 9999999)):
        self.weight = weight
        self.price = price
        self.flamibility = flamibility
        self.identifier = identifier

    def punch(self):
        punch = (self.flamibility*self.weight)
        if punch < 5:
            return('That tickles.')
        elif punch >= 5 and punch < 15:
            return('Hey that hurt!')
        else:
            return('OUCH!')

    def explode(self):
        boom = (self.flamibility*self.weight)
        if boom < 10:
            return('...its a glove.')
        elif boom >= 10 and boom < 50:
            return('...its a glove.')
        else:
            return('...its a glove.')
