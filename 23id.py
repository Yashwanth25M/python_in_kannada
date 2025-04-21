# Object oriented programming
#refer(https://github.com/chandansgowda/learn-python-in-kannada/blob/main/notes/15.md)

# class Car:
#     # Attributes
#     def __init__(self, brand, model):
#         self.brand = brand  # Instance variable
#         self.model = model  # Instance variable

#     # Method
#     def display_info(self):
#         print(f"Car Brand: {self.brand}, Model: {self.model}")

# # Creating an object of the class
# my_car = Car("Toyota", "Corolla")
# my_car.display_info()


# Car Brand: Toyota, Model: Corolla

# Car is the class.
# my_car is an object of the Car class.
# brand and model are attributes of the object.
# display_info() is a method that displays the car's details.






# class Human:#edu class
#     def __init__(self,name):
#         self.name = name#edu attribute
    
#     def walk(self):
#         print(f"{self.name} is walking")#edu method

# Chandan = Human("Chandan")#edu objects
# Darshan = Human("Darshan")

# Chandan.walk()



# Homework
# 1.Create a Class:
# Write a class Mobile with attributes brand and price.
# Create two objects of the class and display their attributes using a method.

# class  Mobile:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price

#     def display_info(self):
#         print(f"Brand: {self.brand}, price: {self.price}")

#         # Creating an object of the class
# mobile = Mobile("IQOO", "32,000")
# mobile.display_info()



# 2.Method Definition:
# Define a class Student with attributes name and marks.
# Write a method display_info() that prints the student's name and marks.
# Create multiple objects of the Student class and call the method on each.

# class Student:#class
#     def __init__(self,name,marks):#attribute(behaviour)
#         self.name=name
#         self.marks = marks

#     def display_info(self):#method
#         print(f"Name:{self.name} \nMarks:{self.marks}")

# Student = Student("A",100)#object
# Student.display_info()