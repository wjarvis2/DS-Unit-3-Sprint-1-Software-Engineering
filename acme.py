"""
Utility functions for acme product inventory management
"""
from random import randint 


class Product(object):

    def __init__(self, name, price = 10, weight = 20, flammability = 0.5,
    identifier = randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight 
        self.flammability = flammability
        self.identifier = identifier
        

    def stealability(self) -> str:
        stealability_quotient = ((self.price / self.weight))
        if stealability_quotient < 0.5:
            return "Not so stealable..."
        elif stealability_quotient >= 0.5 and stealability_quotient < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"


    def explode(self) -> str:
        explosiveness = ((self.flammability * self.weight))
        if explosiveness < 10:
            return "...fizzle"
        elif explosiveness >= 10 and explosiveness < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"

class BoxingGlove(Product):

    def __init__(self, name, price = 10, weight = 10, flammability = 0.5,
    identifier = randint(1000000, 9999999)):
        super(BoxingGlove, self).__init__(name, price, flammability)
        self.weight = weight 

    def explode(self) -> str:
        return "...it's a glove."


    def punch(self) -> str:
        punch_weight = self.weight
        if punch_weight < 5:
            return "...That tickles."
        elif punch_weight >= 5 and punch_weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"




         


