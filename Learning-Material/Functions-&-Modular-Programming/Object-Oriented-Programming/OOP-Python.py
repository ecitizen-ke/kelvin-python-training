# Module1: Introduction to Object-Oriented-Programming
# Lesson 1.1:Understanding Programming Paradigms
'''
A programming paradigm is a fundamental style or approach to programming,
characterized by a set of principles and methods of writing code. Different 
paradigms offer different ways of thinking about and structuring programs.
'''

# Procedural Programming
'''
This is a way of structuring program scripts in a proceedural (step-by-step)
structure/ format. (Top to bottom)
'''

# Example 
def greeting(name):
    print(f"Hellow my name is {name}!")

greeting("Kelvin")


# Functional Programming
'''
Treats computation as the evaluation of mathematical functions. It emphasizes
the use of pure functions and avoids mutable data.
'''
# Example

def add_t1(a,b):
    x = a + b 
    print(x)

add_t1(1,2)

def add_t2(a,b):
    return (a+b)

numbers = [1,2,3,4]
result = map(lambda x: add_t2(x,2), numbers)
print(list(result))


# Object Oriented Programming(OOP)
'''
Bases on the concept of objects which are instances of classes and empasizes
inheritance, encapsulation and polymorphism.
'''
# Example

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says woof!!")

my_dog = Dog("Buddy")
my_dog.bark()

# Lesson 1.2: Basics of Object-Oriented Programming
## Objects 
'''
Instances of classes that contain both data (attributes/ properties) and behaviour
(methods)
'''
## Classes
'''
Blueprints for creating objects, defining their structure and behaviour
'''

# Module 2: Classes and Objects 
# Lesson 2.1: Creating Classes and Objects 

# Defining a class
class Dog:
    # Class body
    pass  # Placeholder indicating that the class has no attributes or methods yet

# Creating an Object/ Instance of a given class
my_dog = Dog()
print(my_dog)  # Output: <__main__.Dog object at 0x7fabcabc1234>

# The __init__ Method (Constructor)
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance variable for the dog's name
        self.age = age    # Instance variable for the dog's age

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")


class Circle: # Defining a class named Circle
    # Constructor method (__init__) initilizes the object(s)(self) 
    # and the objects attributes (radius)
    def __init__(self, radius):
        # Initialize instance variable 'radius' with the value passes as a parameter 
        self.radius = radius
    
    # Method named 'area' to calculate the area of the circle
    def area(self):
        # Return the area of the circle using the formula: pi * radius^2
        return 3.14 * self.radius * self.radius
    
# Create an instance of the Circle class with radius 5 and assign it to 'my_circle'
my_circle = Circle(5)
# print the area of the circle using the 'area' method of the 'my_circle' object
print(f"The area of the circle is {my_circle.area()}") 

# Trial Code
'''
This is an attempt to create a class called Shape with various subclasses within it
(square, triangle) each with their own attributes (length, height, base) but can access 
methods inherited from the mother calss
'''
# Instance Variables and Methods
# Defining and accessing Instance Variables
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

# Creating an object of the Car class
my_car = Car("Toyota", "Camry", 2020)
print(my_car.display_info())  # Output: 2020 Toyota Camry


import math # Importing the math module 
# Defining the parent class shape
class Shape:
    # Defining methods of the parent class that can be inherited by the 
    # Child classes
    def area(self):
        pass
    def perimeter(self):
        pass

# Defining the child class square, inheriting from shape 
class square(Shape):
    # Defining attributes of the child class 
    def __init__(self, length):
        self.length = length
    # Assigning child class attributes to inherited methods of the mother class
    def area(self):
        return self.length * self.length
    def perimeter(self):
        return self.length * 4

# Defining the child class triangle
class triangle(Shape):
    # Defining attributes of the child class 
    def __init__(self, height, base):
        self.height = height
        self.base = base
    # Assigning child class attributes to inherited methods of the mother class
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.base + 2*(math.sqrt(self.height**2+(0.5*self.base)**2))

# Setting the square child class attribute and initializing an object/ instance of it
my_square = square(5)
# Calculating area and perimeter of the my_square object by calling methods
area_s = my_square.area()
peremeter_s = my_square.perimeter()

# Setting the triangle child class attribute and initializing an object/ instance of it
my_triangle = triangle(10,10)
# Calculating the area and perimeter of the my_triangle object by calling methods
area_t = my_triangle.area() 
peremeter_t = my_triangle.perimeter()

# Printing the area and perimeter of the square object created
print(f"Area of my square is {area_s}")
print(f"Peremeter of my square is {peremeter_s}")

# Printing the area and perimeter of the triangle object created
print(f"Area of my triangle is {area_t}")
print(f"Peremeter of my triangle is {peremeter_t}")


# Instance Methods
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

# Creating an object of the Circle class
my_circle = Circle(5)
print(f"Area: {my_circle.area()}")  # Output: Area: 78.5
print(f"Circumference: {my_circle.circumference()}")  # Output: Circumference: 31.400000000000002

# Module 3: Class Attributes and Class Methods 
## Difference Bewtween Instance variables and Class variables
### Instance Variables
'''
These are variables that are specific/ unique to a certain instance of a class and thus depending on the instance the variable value may change from one instance to another.
'''

#Example 

class Fruit:
    def __init__(self, name , color, taste):
        self.name = name
        self.color = color
        self.taste  = taste

orange = Fruit('Orange', 'Orange','Bitter')
apple  = Fruit('Apple', 'Red', 'Sweet')
print(f'{apple.name} characteristics are color: {apple.color} and taste: {apple.taste}')

### Class Variables
'''
These are attributes sharable across all instances of a class. They are defined directly in any class body but outside any methods within the class. The values of such attributes/variabls remains constant across all class instances of a particular class
'''
class Planet:
    #-The variables below are examples of class variables and are defined in the class body but outside any methods
    speed_light = 299792458
    planck_constant = 6.63e-34

    '''
    This is the initialization of a standard method using the __init__ 
    constructor with the attributes ocean, sea, continent and country
    '''
    def __init__(self, name, ocean, sea, continent, country):
        self.name = name
        self.ocean =  ocean
        self.sea = sea
        self.continent = continent
        self.country = country

p4 = Planet('Mars', 0, 0, 100, 0)
p3 = Planet('Earth', 5, 50, 7, 195)

#-Class variables can be accessed through class instances or by calling the class name directly
print(f'{p4.name} has {p4.ocean} number of oceans but the speed of light is {p4.speed_light} m/s^2')
print(f'{p3.name} has {p3.ocean} number of oceans but the speed of light is {p3.speed_light} m/s^2')
print(f'{p3.name} has the speed of light set to {Planet.speed_light} m/s^2')

## Class Methods and Static Methods 
### Class Methods
'''
Methods that are bound to the class and not an instance of the class. They can modify class data/attributes across all instances of a class and defined using @calssmethod decorator with cls as the first parameter. They are used to modify or edit class variables/attributes. 
'''

class animal:

    #-This is a class variable/attribute that is accessible across various instances of the class
    count = 0

    # This is an __init__ constructor method that is automatically called when a new instance of the class is called so as to initialize the new class instance with default/provided values.
    def __init__(self, name, product):
        self.name = name
        self.product = product
        animal.count += 1 

    #- This is a class method that is initalized across several/ all instances of a given class depending on the nature of the class method that is being initialized
    @classmethod
    def get_count(cls):
        return cls.count
    
#- Here I initialize two class objects thus running the __init__ constructor twice setting the count value to +=1 twice which gives me a value of 2 
v1 = print(f'The initial value of count is: {animal.get_count()}') # before initialization 

insect = animal('Bee', 'honey')
herbivore = animal('Cow', 'milk') 

v2 = print(f'The final value of count is: {animal.get_count()}') # After initialization 



### Static Methods 
'''
Methods that don't access or modify class/instance data/attributes. Used for utility functions but don't access class or instance data. Defined using the @staticmethod decorator
'''

class Math:
    # This is the process of defining a static method using the @staticmethod decorator
    @staticmethod
    def add(x,y):
        return x + y 
    @staticmethod
    def multiply(x,y):
        return x * y
    
print(Math.add(4,5))
print(Math.multiply(6,7))


    #- Static methods carry out operations without the use of class or instance data/ attributes
class stringutils:
    @staticmethod
    def is_palindrome(s):
        return s== s[::-1]
    
print(stringutils.is_palindrome('hommer'))
print(stringutils.is_palindrome('racecar'))




# Module 4: Inheritance 
## Lesson 4.1: Basics of Inheritance
'''
Inheritance is a fundamental concept in OOP where a sub-class/ minor-class can inherit attributes/ methods from a super-class or base-class. This promotes code reusability and creates a logical relationship between classes 
'''

#- Creating a parent-child class 
'''
This is the parentclass titled as ParentClass with the ChildClass defined right below it. The child class is characterized with the ParentClass title/name acting as the self initilizer of the childclass thus creating a link/connetion between the parentclass and the childclass.
'''
class ParentClass:
    pass

class ChildClass(ParentClass):
    pass


## Method Overriding 
'''
Allows a subclass to provide a specific implementation of a method already defined in its superclass by defining a method with the same name in the subclass. The subclass's version overrides the superclass's version. 
'''
class Vehicle:
    def move(self, type):
        self.type = type 
        return f"The {self.type} is moving"
class Car(Vehicle):
    def move(self):
        return f"The car is driving"

car = Car()
vcar = Vehicle()
print(vcar.move('truck'))
print(car.move())


#- Or

class Vehicle:
    def move(self, type):
        return f"The {type} is moving"
class Car(Vehicle):
    def move(self):
        return f"The car is cruising"
    
car = Car()
vcar = Vehicle()
print(vcar.move('tractor'))
print(car.move())



## Types of Inheritance
'''
Inheritance is a fundamental concept in OOP [Object-Oriented-Programming] where a sub-class/ derived class inherits attributes and methods from a parent class/ super class this promotes code reusability and helps create a logical relationship between classes
'''

###1. Single Inheritance 
'''
Occurs when child class inherits from only one parent class. Parent class: Contains common attributes and methods. Child class:Inherits from parent class and can override or extend its behaviour.
'''
class Animal:
    def speak(self):
        return 'Animal is making a sound'

class Dog(Animal):
    def speak(self):
        return 'Dog is barking'

doug = Dog()
print(doug.speak())