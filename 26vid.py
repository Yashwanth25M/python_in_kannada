#Inheritance
# Inheritance allows a class to inherit attributes and methods from another class, facilitating reuse.
# class Family:
#     def __init__(self, surname):
#         self.surname = surname

# class Child(Family):
#     def __init__(self, surname, name):
#         super().__init__(surname)
#         self.name = name

# child = Child("Gowda", "Ajay")
# print(f"{child.name} {child.surname}")  # Inherits surname from Family



# polymorphism
# Polymorphism allows objects of different classes to be 
# treated as objects of a common superclass, but they can behave differently depending on the object type.

# class Animal:
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Bark")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow")

# animals = [Dog(), Cat()]
# for animal in animals:
#     animal.make_sound()


# Homework

# 1.Inheritance:
# Create a base class Vehicle with a start method. Then create a subclass Bike with an additional ride() 
# method.
# Demonstrate how the Bike can use both start and ride.

# class Vehicle:
#     def start(self):
#         print("Vehicle started.")

# class Bike(Vehicle):
#     def ride(self):
#         print("Riding the bike.")

# my_bike = Bike()
# my_bike.start()
# my_bike.ride()


# 2.Polymorphism:
# Implement a Shape class and derive Circle and Rectangle classes with a method calculate_area.
#  Each class should calculate area differently based on its shape.
# Create a loop to calculate areas for both Circle and Rectangle objects.

# class Shape:
#     def calculate_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.14 * self.radius * self.radius

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height

# shapes = [Circle(5), Rectangle(4, 6)]

# for shape in shapes:
#     print("Area:", shape.calculate_area())