#Objects = attributes (variables) + methods (functions)
#Attributes = Class Attributes (In the main class not a methods) and Instance Attributes (Like inside the methods)
# __init__(self,colour,flavour,topping) - colour etc are instance attributes for the init method
#Methods = Class Methods and Static Method (static don't need to know about the class or instances they relate too)


#Example 1

class Cake:
    TotalCakes = 0 #Examples of a class attributes

    def __init__(self,colour,flavour,topping):
        self.colour = colour
        self.flavour = flavour
        self.topping = topping
        Cake.TotalCakes += 1

    def order(self):
        return "You have ordered a cake which is {}, and is flavour: {} with topping: {}".format(self.colour, self.flavour, self.topping)


    @classmethod #This is an example of a class methods
    def getTotalCakes(cls):
        return "Total Cakes = {}".format(cls.TotalCakes)

    @staticmethod #An example of a static method
    def isCommonDecoration(ingredient):
        commonDecor = ["Sprinkles", "Candles", "Hearts"]
        return ingredient in commonDecor

'''
birthdayCake = Cake("Pink", "Chocolate", "Sprinkles")
redCake = Cake("Red", "Red Velvet", "Red Hearts")

print(birthdayCake.topping)
print(birthdayCake.order())

print(redCake.topping)
print(redCake.order())

'''

#Example 2

class Vehicle:

    def __init__(self, make, colour):
        self.make = make
        self.colour = colour

    def driving(self):
        return ("{} is driving and it is a {} car". format(self.make, self.colour))

'''
NewCar = Vehicle("UP", "White")

print(NewCar.make)
print(NewCar.colour)
print(NewCar.driving())

'''

#Example 3

class WhatsAppProfile:

    def __init__(self, name, phone_number):
        self.__name = name #Encapsualtion - Hiding private data - put __ after self.
        self.__phone_numer = phone_number #Encapsualtion - Hiding private data
        self.status = "Hey there! I'm using WhatsApp" #But not required when making an instance so this is like the default

    def getName(self): #Called a getter
        return self.__name

    def setName(self, newName): #Called a setter
         self.__name = newName


    def setStatus(self, newStatus):
        self.status = newStatus

    def displayProfile(self):
        print("Name: {}". format(self.__name))
        print("Phone: {}".format(self.__phone_numer))
        print("Status: {}". format(self.status))

"""
Profile1 = WhatsAppProfile("Kate", 123)
#print(Profile1.name) #Doesn't work because we have used encapsulation
print(Profile1.getName()) #Now this works

Profile1.setName("KateNew")
print(Profile1.getName()) #Now this will get the new name and it has replaced the original name

print(Profile1.status)
Profile1.setStatus("Hello this is my New Status")
print(Profile1.status)

Profile1.displayProfile()
"""

#Example 4
#Child Class of the WhatsApp Class (Parent)

class BusinessProfile(WhatsAppProfile):

    def __init__(self, name, phone_number, business_name ): #When we make a new init
        super().__init__(name, phone_number) #Uses these attributes from the parent class - Inheritance
        self.business_name = business_name

    # Polymorphism - child can implement an inherited method
    def displayProfile(self): #We can use the same method from the parent
        print("Business Name: {}". format(self.business_name)) # However we are changing it - method overriding

'''
Profile2 =  BusinessProfile("Kate", 456, "Kate Bakes")
Profile2.displayProfile()
'''

#Example 5
#Cannot create an instance of an abstract class - it is there as a blueprint - they have no implementation
#Like a placeholder - shows only essential features - so then any childs of this class MUST follow this same structure

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def makeSound(self):
        pass

    @abstractmethod
    def eatFood(self):
        pass

