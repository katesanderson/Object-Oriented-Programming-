'''
Single Responsibility
Open and Close
Liskov
Interface
Dependancy Inversion


SINGLE RESPONSIBILITY PRINCIPLE
A class should have only one job and therefore it
should have only a single reason to change.

OPEN-CLOSED PRINCIPLE
Classes, modules, functions, etc. should be open for extension, but closed for modification.

Simply means that if you need to add additional functionality then you should NOT be editing the
existing classes or methods to make it happen.

LISKOV SUBSTITUTION PRINCIPLE
If we have a base class A (SUPER CLASS) and subclass B (SUB CLASS),
we should be able to substitute the main class A with the subclass B without breaking the code.

INTERFACE SEGREGATION PRINCIPLE
A class should not be forced to implement interfaces it does not use.
In other words, a class should not be forced to implement methods it does not need.

DEPENDENCY INVERSION PRINCIPLE
(Not to be confused with DEPENDENCY INJECTION PRINCIPLE
which is slightly different by we're going to assume both to be same for now)

High-level modules should not depend on low-level modules.
Both should depend on abstractions (e.g. interfaces).

'''

#Examples:


# BAD EXAMPLE FIRST

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def calculate_salary(self):
        # Calculate the salary
        pass

    def save_to_database(self):
        # Save the employee data to the database
        pass


"""
### WHY IS IT BAD?
In this example, the Employee class has two responsibilities: calculating the salary and
 saving the employee data to the database. If there are changes in the database structure,
  it will affect the Employee class, violating the Single Responsibility Principle.
"""
# GOOD EXAMPLE NOW

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def calculate_salary(self):
        # Calculate the salary
        pass


class EmployeeDatabase:
    def save_to_database(self, employee):
        # Save the employee data to the database
        pass


"""
### WHY IS IT GOOD?
In the improved example, the Employee class is responsible only for representing an employee,
 and a new class EmployeeDatabase is introduced to handle the database-related operations.
  This adheres to the Single Responsibility Principle, as each class now has only one reason
   to change. If there are changes in the database, it won't affect the Employee class
"""





# BAD EXAMPLE FIRST
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class AreaCalculator:
    def calculate_area(self, rectangle):
        return rectangle.width * rectangle.height


# Later, you need to add Circle class and support for calculating the area of a circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

# Which means that you have to now "modify" this AreaCalculator! Which is BAD!!
class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return math.pi * (shape.radius ** 2)

"""
### WHY IS IT BAD?
In this example, if you need to add support for calculating the area of a circle, you would have
 to modify the AreaCalculator class, violating the Open-Closed Principle.
"""


# GOOD EXAMPLE NOW
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class AreaCalculator:
    def calculate_area(self, shape):
        return shape.calculate_area()


"""
### WHY IS IT GOOD?
In this improved example, we introduce an abstract base class Shape that declares the
 calculate_area method. Both Rectangle and Circle classes inherit from Shape and provide
  their own implementations of calculate_area. The AreaCalculator class now works with any
   shape that is a subclass of Shape without modification, adhering to the Open-Closed Principle.
    If you need to add a new shape, you can do so by creating a new class that extends Shape
     without changing the existing code
"""





# BAD EXAMPLE FIRST

class Parent:
    def eat(self):
        print("Eating food.")

    def sleep(self):
        print("Sleeping.")

    def work(self):
        print("Working a job.")

    def pay_taxes(self):
        print("Paying taxes.")


class Child(Parent):
    def work(self):
        # Violates LSP. Kids can't work!
        print("Playing with toys instead of working.")

    def pay_taxes(self):
        # Violates LSP as it makes no sense for a child to pay taxes.
        print("Children don't pay taxes.")


"""
### WHY IS IT BAD?
In this example, Child is a subclass of Parent. However, it violates the Liskov Substitution
 Principle because the behavior of work and pay_taxes methods in Child are not
  consistent with the behavior of the same methods in the base class Parent.
"""

# GOOD EXAMPLE NOW

from abc import ABC, abstractmethod


class Human(ABC):
    def eat(self):
        print("Eating food.")

    def sleep(self):
        print("Sleeping.")

    @abstractmethod
    def activity(self):
        pass


class Adult(Human):
    def activity(self):
        print("Working a job and paying taxes.")


class Child(Human):
    def activity(self):
        print("Playing and going to school.")


"""
### WHY IS IT GOOD?
In this improved example,Here, Adult and Child both inherit from Human but implement activity() in ways 
that are appropriate to their roles. 
Now, we avoid the need for inappropriate method overrides
"""



# BAD EXAMPLE FIRST - Using a single large interface

class Entity:
    def move(self):
        pass

    def attack(self):
        pass

    def spawn(self):
        pass


class Character(Entity):
    def move(self):
        print("Character is moving")

    def attack(self):
        print("Character is attacking")

    def spawn(self):
        print("Character is spawned")


class Turret(Entity):
    def move(self):
        pass  # Turret doesn't move, but forced to implement the method

    def attack(self):
        print("Turret is attacking")

    def spawn(self):
        pass  # Turret doesn't spawn, but forced to implement the method


"""
### WHY IS IT BAD?
In this example, the Entity interface is too broad, and both Character and Turret
 have to implement methods that are not relevant to them
"""


# GOOD EXAMPLE NOW

# Good Example - Using specific interfaces

class Moveable:
    def move(self):
        pass


class Attacker:
    def attack(self):
        pass


class Spawner:
    def spawn(self):
        pass


class Character(Moveable, Attacker, Spawner):
    def move(self):
        print("Character is moving")

    def attack(self):
        print("Character is attacking")

    def spawn(self):
        print("Character is spawned")


class Turret(Attacker):
    def attack(self):
        print("Turret is attacking")


"""
### WHY IS IT GOOD?
In this improved example, we have specific interfaces (Moveable, Attacker, Spawner) 
that are implemented by the classes that need them. Now, Character implements all three 
interfaces, while Turret only implements the Attacker interface, reflecting a more 
segregated and flexible design.

"""



# BAD EXAMPLE FIRST

# Low-level Module
class CreditCardPaymentProcessor:
    def process_credit_card_payment(self, amount):
        # Logic for processing credit card payment
        print(f"Processing credit card payment of ${amount}")


# High-level Module
class Order:
    def __init__(self, payment_processor: CreditCardPaymentProcessor):
        self.payment_processor = payment_processor

    def checkout(self, amount):
        # Direct dependency on low-level module
        self.payment_processor.process_credit_card_payment(amount)


"""
### WHY IS IT BAD?
In this bad example, the Order class has a direct dependency on the low-level module 
CreditCardPaymentProcessor. This violates the Dependency Inversion Principle because 
the high-level module is directly dependent on a low-level module, and there's no use 
of an abstraction. If there are changes in the payment processing logic or if you want 
to introduce a different payment method, it would require modifications to the Order class.
"""

# GOOD EXAMPLE NOW


from abc import ABC


# Abstraction (Interface)
class PaymentProcessor(ABC):
    def process_payment(self, amount):
        pass


# Low-level Module
class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Logic for processing credit card payment
        print(f"Processing credit card payment of ${amount}")

class DebitCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Logic for processing credit card payment
        print(f"Processing debit card payment of ${amount}")


# High-level Module
class Order:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def checkout(self, amount):
        # Use the abstraction
        self.payment_processor.process_payment(amount)


"""
### WHY IS IT GOOD?
In this example, Order is the high-level module, and it depends on the abstraction 
PaymentProcessor. The CreditCardPaymentProcessor is a low-level module that implements 
the PaymentProcessor interface. This adheres to the Dependency Inversion Principle as 
the high-level module depends on an abstraction, and not directly on a low-level module.
"""
