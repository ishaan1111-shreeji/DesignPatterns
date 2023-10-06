# Program to demonstrate Decorator Design Pattern,
# here,concrete_coffee is made abstract so that it cannot be  instantiated.
# so we would use decorater class to cretae decorator coffee to add attributes to concrete coffee
# concrete_coffee-->sugar_concrete_coffee-->Milk_sugar_concrete_coffee-->Vanilla_Milk_sugar_concrete_coffee

import six
# Six is a Python 2 and 3 compatibility library.
# It provides utility functions for smoothing over the differences between the Python versions

from abc import ABCMeta


@six.add_metaclass(ABCMeta)
class Abstract_coffee(object):
    def coffee_type(self):
        pass

    def get_cost(self):
        pass

    def get_ingredients(self):
        pass

    def get_tax(self):
        return 0.1 * self.get_cost()


class concrete_coffee(Abstract_coffee):
    def coffee_type(self):
        return "concrete_coffee"

    def get_cost(self):
        return 100.00

    def get_ingredients(self):
        return "coffee"


# creating abstractor decorator to modify concrete structure
@six.add_metaclass(ABCMeta)
class Abstract_coffee_Decorator(Abstract_coffee):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def coffee_type(self):
        return self.coffee_type()

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()


# adding properties to base concrete class
class Sugar(Abstract_coffee_Decorator):
    def __init__(self, decorated_coffee):
        Abstract_coffee_Decorator.__init__(self, decorated_coffee)

    def coffee_type(self):
        return self.decorated_coffee.coffee_type() + " Sugar"

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ", Sugar"


# adding properties to base concrete class
class Milk(Abstract_coffee_Decorator):
    def __init__(self, decorated_coffee):
        Abstract_coffee_Decorator.__init__(self, decorated_coffee)

    def coffee_type(self):
        return self.decorated_coffee.coffee_type() + " MIlk"

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 25.00

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ", Milk"


# adding properties to base concrete class
class Vanilla(Abstract_coffee_Decorator):
    def __init__(self, decorated_coffee):
        Abstract_coffee_Decorator.__init__(self, decorated_coffee)

    def coffee_type(self):
        return self.decorated_coffee.coffee_type() + " Vanilla"

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 50.00

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ", Vanilla"


# creating objects for above

mycoffee = concrete_coffee()
print(
    "Coffee_type: " + mycoffee.coffee_type() + "\n" + "Ingredients: " + mycoffee.get_ingredients() + "\n" + "cost: " + str(
        mycoffee.get_cost()) + "\n" + "Sales_Tax=" + str(mycoffee.get_tax()))
print("*" * 25)
mycoffee = Sugar(mycoffee)
print(
    "Coffee_type: " + mycoffee.coffee_type() + "\n" + "Ingredients: " + mycoffee.get_ingredients() + "\n" + "cost: " + str(
        mycoffee.get_cost()) + "\n" + "Sales_Tax=" + str(mycoffee.get_tax()))
print("*" * 25)
mycoffee = Milk(mycoffee)
print(
    "Coffee_type: " + mycoffee.coffee_type() + "\n" + "Ingredients: " + mycoffee.get_ingredients() + "\n" + "cost: " + str(
        mycoffee.get_cost()) + "\n" + "Sales_Tax=" + str(mycoffee.get_tax()))
print("*" * 25)
mycoffee = Vanilla(mycoffee)
print(
    "Coffee_type: " + mycoffee.coffee_type() + "\n" + "Ingredients: " + mycoffee.get_ingredients() + "\n" + "cost: " + str(
        mycoffee.get_cost()) + "\n" + "Sales_Tax=" + str(mycoffee.get_tax()))
