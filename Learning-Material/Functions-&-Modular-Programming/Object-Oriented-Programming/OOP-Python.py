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

## Objects 
'''
Instances of classes that contain both data (attributes/ properties) and behaviour
(methods)
'''
## Classes
'''
Blueprints for creating objects, defining their structure and behaviour
'''

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


# Lesson #1
# Defining a class
class Dog:
    # Class body
    pass  # Placeholder indicating that the class has no attributes or methods yet

# Creating an Object
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

# Lesson #2
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

#