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
# In this example Dog class inherits from Animal class and overrides the speak method
# Parent class
class Animal:
    def speak(self):
        return 'Animal is making a sound'

# Child class
class Dog(Animal): # Inherits from Animal
    def speak(self):
        return 'Dog is barking'

# Single inheritance in action
doug = Dog()
print(doug.speak())


###2. Multiple Inheritance 
'''
Occurs when a child class has more than one parent class and inherits from both of them.
'''
# In this case the child class has two parent classes from which it inherits two methods seperately one from each class (start & play_music) methods. 

# Parent class 1
class Engine:
    def start(self):
        return 'Engine has started'

# Parent class 2
class MusicSystem:
    def play_music(self):
        return 'Playing music'

# Child class
class Car(Engine, MusicSystem): # Inherits from both Engine and MusicSystem
    def  drive(self):
        return 'Car is driving'

# Using multiple inheritance
my_car = Car()
print(my_car.start())
print(my_car.play_music())
print(my_car.drive())


###3. Multilevel Inheritance 
'''
Occurs when a class is derived from a class that is already derived from another class. The chain-like structure shows where classes inherit through multiple levels.
'''
# The Dog class inherits the attributes and methods from the Animal and the Mammal class in a cascading/ leveling way.
class Animal:
    def move(self):
        return 'Animal is moving'
    
class Mammal(Animal):
    def walk(self):
        return 'Mammal is walking'
    
class Dog(Mammal):
    def bark(self):
        return 'Dog is barking'

# Using multilevel inheritance 
dog = Dog()
print(dog.move())
print(dog.walk())
print(dog.bark())


###4. Hierarchial Inheritance
'''
Occurs when more than one class inherits from the same parent class. Child classes share the same attributes and methods of the parent class but each can have its own specific functionality
'''
# Parent class 
class Animal:
    def move(self):
        return 'Animal is moving'

# Child class 1
class Bird(Animal): # Inherits from Animal
    def fly(self):
        return 'Bird is flying'

# Child class 2
class Fish(Animal): # Inherits from Animal also 
    def swim(self):
        return 'Fish is swimming'

# Using hierarchical inheritance [Instantiation]
bird = Bird()
fish = Fish()

print(bird.move())
print(bird.fly())
print(fish.move())
print(fish.swim())


# Module 5: Encapsulation
## Lesson 5.1: Encapsulation and Data Hiding
'''
Encapsulation: Process of bundling variables (data) and methods (functions) operating on the data into a single unit/ class. Also involves restricting access to some of an object's components ---> = Data hiding.
'''

### Access Modifiers
#### Public Attributes
'''
Accessible from anywhere both inside and outside a class.
'''
#### Protected Attributes
'''
Indicated using a single _ underscore preceding the attribute name. Can still be accessed outside the class but intended for internal use 
'''
#### Private Attributes
'''
Are prefixed with a double __ underscore thus making them inaccessible from outside the class.Python uses name-mangling to ensure privacy. 
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name        # Public attribute
        self._department = 'IT' # Protected attribute
        self.__salary = salary  # Private attribute
    
    def get_salary(self):
        return self.__salary # Used access private attribute

#-Create an object
emp = Employee('John', 5000)

#-Accessing public and protected attributes directly
print(emp.name)
print(emp._department)

#- Trying to access the private attribute directly will raise an error 
# print(emp.__salary) # Raises attribute error

# Accessing private attribute via method 
print(emp.get_salary())


## Lesson 5.2: Property Decorators
##***Note***##
'''
Attribute access is handled using property decorators thus allowing you to create getter and setter methods used to encapsulate the logic of getting or setting the attribute's value
@property decorator defs getter method
@name.setter decorator defs setter method
Getter and setter methods can both define the same function but implementation determines the use of the setter or the getter function.
'''

class Circle:
    def __init__(self, radius):
        self._radius = radius # Protected attribute 
    
    # Getter method
    @property
    def radius(self):
        return self._radius
    
    # Setter method
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive!")
        self._radius = value

# Create a circle object
circle = Circle(5)

# Access radius using getter 
print(circle.radius)

# Set radius using setter
circle.radius = 10 
print(circle.radius)

# Try to set an invalid radius 
# circle.radius = -3 # Raises a ValueError

### Managing Attribute Access 
'''
Encapsulation allows foor the definition of rules that manage the internal state of an object.Example for the circle class a setter method is employed to control how the radius is changed allowing only for positive values to be set. 
'''

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # Public attribute
        self.__balance = balance # Private attribute 

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print('Can not set a negative balance')
        else:
            self.__balance = amount
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print('Insufficient balance')
        else:
            self.__balance -= amount

# Create a banck account
account = BankAccount('Andrew', 10000)

# Access balance using getter
print(account.balance)

# Deposit and withdraw money 
account.deposit(5000)
print(account.balance)

account.withdraw(20000)
print(account.balance)

# Attempt to set negative balance directly (won't work)
account.balance = -500
print(account.balance)


# Module 6: Polymorphism
## Lesson 6.1: Understanding Polymorphism
'''
Concept in OOP that allows objects of a different class to be treated as objects of a common superclass. Means a single interface can represent different underlying forms (data types).

Relies mainly on method overriding and method overloading
'''

## Method Overloading
'''
This occurs when a class has a method with the same name but can take up multiple number of parameters or use different parameter types(Data types) depending on the use case. 
'''

#- Below is a Javascript example
'''
class MathOperation{
    # Overloaded method for integer parameters
    int add(int a, int b){
        return a + b;
    }

    # Overloaded method for double parameters
    double add(double a, double b){
        return a + b;
    }
}
'''

#- Below is a Python method overloading example
'''
Python does not have method signatures this changing parameters won't overload a method. Python uses default arguments or variable-length arguments to achieve similar functionality
'''

class MathOperation:
    def  add(self, *args):
        return sum(args)
    
# Usage
op = MathOperation()
print(op.add(1,2))
print(op.add(1,2,3,4))

#- Below is a variable arguments Python method overloading example
'''
By using **kwargs allows one to pass a variable number of keyword arguments in the class  
'''

class Person: # The Person class
    def info(self, name, age = None, city = None): # The information method that contains method overloading through use of conditional statements in logic to allow for multiple attribute use.
        if age and city:
            return f"{name} is {age} years old and lives in {city}."
        elif age:
            return f"{name} is {age} years old."
        else:
            return f"{name}'s information is not complete."

person = Person()
print(person.info('Bob', age = 25))
print(person.info('Bob', age = 21, city = 'Ruaka'))
print(person.info('Steven', city = 'Kwale',age = 45))

#- Example shows Python overloading by using type checking 
'''
This script checks the datatype of the argument and behaves differently depending on the datatype of the argument used.
'''

class Printer:
    def print_item(self, item):
        if isinstance(item, str):
            print(f'String: {item}')
        elif isinstance (item, int):
            print(f'Integer:{item}')
        elif isinstance(item, float):
            print(f'Float: {item}')
        else:
            print('Unsupported type')

printer = Printer()
printer.print_item('Hello')
printer.print_item(42)
printer.print_item(3.14)
printer.print_item({1,2,3,4})

#- Example shows method overlaoding whereby the behavior of the method changes based on the type of attribute that is used/entered.

class calculator: # Instantiates a calculator class
    @classmethod  # Instantiates a class method
    def calculate(cls, a, b = None):
        if b is None:               # Conditional statement logic used to overload the method using variable parameter types
            return a * a
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b 
        else:
            raise ValueError('Unsupported data type(s)')

print(calculator.calculate(5))     # Execution of the class method using integer parameter type
print(calculator.calculate(5, 10.987)) # Execution of the class method using various parameter types

## Lesson 6.2: Method Overriding and Duck Typing
### Method Overriding in Python
'''
Allows a subclass to provide a specific implementation of a method already defined in its parent/super class. A method that is already defined in the super class and intended to work a certain way where defined can have a different implementation while in the subclass thus overriding the original implementation of the superclass method as intended.
'''

#- Example of method overriding in Python

class Vehicle: # Instantiation of the superclass
    def fuel(self):
        return 'Fuel type not specified'

class Car(Vehicle): # Instantiation of the subclass
    def fuel(self):
        return 'Petrol'

class Truck(Vehicle): # Instantiation of the subclass 
    def fuel(self):
        return 'Diesel'
    
def vehicle_fuel(vehicle: Vehicle): # Function used to call the fuel method from the Vehicle superclass by one of the subclasses 
    print(vehicle.fuel())


# Instantiation of Vehicle class objects 
car = Car()
truck = Truck()
vehicle_fuel(car)
vehicle_fuel(truck)


#- Example of animal sounds classification system 
'''
The Animal superclass has a Dog and Cat subclass which inherit the makesound method from the superclass however the subclasses override the makesound method thus changing its functionality as they use it
'''
class Animal: # Instantiate super/parent class
    def makesound(self): # Parent class method
        return 'Some generic sound'

class Dog(Animal): # Instatiate subclass
    def makesound(self):
        return 'Bark'

class Cat(Animal): # Instantiate subclass
    def makesound(self):
        return 'Meow'

# Instantiate subclass objects 
a = Animal()
b = Dog()
c = Cat()

# Function creation and generation 
def animal_sound(item):
    if item in [a,b,c]:
        print(item.makesound())
    else:
        print('What the L are you looking?!!')

# Calling the animal_sound function 
animal_sound(a)
animal_sound(b)
animal_sound(c)

#- Example of Genaral Shape superclass with various shape subclasses 

class Shape: # Shape superclass
    def area(self):
        raise NotImplementedError('Shape is a general class no Area found')
    
class Circle(Shape): # Circle subclass of Shape superclass
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius **2
        # return 3.14 * self.radius * self.radius

class Rectangle(Shape): # Rectangle subclass of Shape superclass
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Instantiating area method to the super and subclasses
shape = [Circle(5), Rectangle(4,5), Shape()]
for shapes in shape:
    print(shapes.area())



### Duck Typing and Dynamic Typing
#### Duck Typing 
'''
It is a programming concept where the type or class of an object is determined by its behaviour(methods and properties) and not an explicit type.[If it looks like a duck and it quacks like a duck,it must be a duck]
'''

#- Example using duck typing
'''

'''
class Duck:
    def quack(self):
        return 'Quack!'

class Dog:
    def quack(self):
        return 'Woof, but I can pretend to quack!'
    
def make_it_quack(animal):
    print(animal.quack())

duck = Duck()
dog = Dog()

make_it_quack(duck)
make_it_quack(dog)


#- Example using file like objects 

class File: # Normal general class
    def read(self):
        return 'Reading from File'

class StringIO: # Normal general class
    def read(self):
        return 'Reading from string buffer'

# Creating object instances of the method
fileo = File()
s_io = StringIO()

# Calling the method usisng the created instances
print(fileo.read())
print(s_io.read())


#### Dynamic typing 
'''
Feature in Python where the type of a variable is determined at runtime rather than at compile time. You can assign a value of any type to a variable and change its type dynamically during execution. 
'''

# Example: Simple variable reassignment

def dynamic_typing(): # Calling and creating the function 
    variable = 10
    print(f'We are so lucky there are not {variable} days in a week')

    variable = 'week'
    print(f'Some say if you can\'t handle ten day weaks you are {variable}')

    variable = [1,2,5]
    print(f'{variable[0]} is the number of planets that, {variable[1]} get to meet on and hopefully have {variable[2]} dates on')

dynamic_typing() # Calling the function 

# Example: Function Arguments and Type Handling 
'''
This example takes data of a certain data type and processes it accordingly then diplays the output depending on the type of data that is being processed using a conditional statement to pass on the processing logic.
'''
# Intializing the function 
def process_data(data):
    print('Processing the data...')
    
    # The function logic is carried out using a conditional statement
    if isinstance(data, list):
        print(f'Data is alist: {data}')
        print(f'The list sum is: {sum(data)}')
    elif isinstance(data, str):
        print(f'The data is a string: {data}')
        print(f'Format the string: {data.capitalize()}')
    else:
        print('This data format is unrecognizable')

# Calling the function 
process_data([2,6,8])
process_data('a noisy CaT onCE hAD to gO siLENT for a WEek iT alMoST dieD.')
process_data(True)



# Example: Class Instances and Mixed Types 
# Instantiation of the superclass and the subclasses 
class Animal:
    def sound(self):
        return 'A sound'
class Cat(Animal):
    def sound(self):
        return 'Meow ,meow!!'
class Dog(Animal):
    def sound(self):
        return 'Grrrr!'

# Use of dynamic typing for the variable a 
a = Animal()
print(a.sound())
a = Cat()
print(a.sound())
a = Dog()
print(a.sound())


# Module 7: Special Methods and Operator Overloading
## Lesson 7.1: Special Methods in Python
'''
Magic-methods/ Special-methods provide a way to interact with Python's syntax and functionalities, making user-defined classes more intuitive and Pythonic
'''

## D-Under Methods (__init__, __str__, __repr__, __len__)
'''
Allow Python to implement behaviour for built-in functions and operator. Enable interaction with Python's syntax and functionalities making user-defined classes more intuitive and Pythonic. 
'''

## __str__
'''
This is a special method that allows for an object to be directly printed using the print() statment. The __str__ method takes presidence over the __repr__ method thus when just using a normal print statement it calls the __str__ method but when the __repr__ method can be called using the repr() statement on the object
'''
## __repr__
'''
Intended for developers to provide more detailed string representation of an object, that is ideally unambiguous. Called using the built in repr() function used interactive sessions to display and object(s) information. 
'''

# Example: __str__ and  __repr__

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by "{self.author}"'
    
    def __repr__(self):
        # !r part of the expression places '' around the title
        return f'Book(Title = {self.title!r}), Author = {self.author})'

book = Book('Harry Potter and the Prisoner of Azkaban','J.K. Rowling')

print(book)
print(str(book))
print(repr(book))

## __len__
'''
Allows you to define the behaviour of the built-in len() function used mostly for counting operations. Eg- Getting the number of items in a list or the number of characters in a string..
'''

class ItemCollection:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
collection = ItemCollection(['apple','banana','cherry'])
print(len(collection))

## __getitem__
'''
Your class can support indexing allowing users to access elements with squaare bracket notation Eg: obj[index]. Allows custom container classes to behave similarly to lists or dictionaries.
'''

# Example: __getitem__ 
# Class instantiation
class StudentList:
    # Class constructor initialization
    def  __init__(self, students):
        self.students = students
    # Returns item from specified index within the collection
    def __getitem__(self, index):
        return self.students[index]

# Creation of the object from the class
student = StudentList(['Ronald','Bethwin','Nicholous'])
print(student[0])

## Lesson 7.2: Operator Overloading
### Defining Custom Operator Behavior 
'''
Operator overloading helps define how operators behave with class instances, thus enabling you to create more intuitive interfaces for your classes thus allowing you to use standard operators like [+,-,*], whereby the user doesn't have to call methods explicitly thus allowing users to use familiar syntax thus improving readability and usability.
'''

class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __add__ (self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    
v1 = Vector(1,2)
v2 = Vector(3,4)
v3 = v1 + v2 

print(v1)
print(v2)
print(v3)









