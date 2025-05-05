# Getters and setters

# class Student:
#     def __init__(self ,  name , age ):
#         self.name = name
#         self.age = age
 
# s1 = Student( "Abd" , 6)
# s1.name="abd2"
# print(s1.name)#name changed to abd 2 but it can also be controlled through 
# private variable(by using"__" before variable)

# class Student:
#     def __init__(self ,  name , age ):
#         self.__name = name
#         self.__age = age
 
# s1 = Student( "Abd" , 6)
# s1.name="abd2"
# print(s1.__name)#throws an error as its private , it cannot be accesed

# This private variables can be accesed by getter and setter

# class Student:
#     def __init__(self ,  name , age ):
#         self.__name = name
#         self.__age = age
    
#     def get_name(self):#getter
#         return self.__name
    
#     def set_name(self ,  name):#setter
#         if isinstance(name , str):# isinstance allows only mentioned datatype
#             self.__name = name
#         else:
#             print("Can only pass strings")
#         #just creating a function to acces and manipulate and checking 
 
# s1 = Student( "Abd" , 6)
# ##print(Student.__name) #throws an error as its private
# print("Before setter\n",s1.get_name())
# s1.set_name("abd2")
# print("After setter\n",s1.get_name())
# s1.set_name(222)


# Method overloading
# This concept varies on different languages but in python simple
# Method overloading is the ability to define multiple methods 
# with the same name but different parameters.

# class Calculator:
#     def calcu(self,a,b,c=0):
#         print(a + b + c)

# cal = Calculator()
# cal.calcu(3,4,5)
# cal.calcu(3,4)

# Method Overridding:Method overriding allows a child class to provide a specific 
# implementation for a method that is already defined in its parent class.
# Purpose: It enables a child class to alter or extend the behavior of a parent class method.

# class Animal:#parent
#     def make_sound(self):
#         print("Animal is making sound") #overrided by class Dog(Animal)
    
# class Dog(Animal):#child
#     def make_sound(self):
#         print("Bark") 

# a1 = Dog()
# a1.make_sound()



#Super
# Definition: The super() function is used in child classes to call a method from the parent class,
#  enabling access to inherited methods or attributes.
# Purpose: It ensures that the parent class's method is executed alongside any additional functionality 
# added in the child class, useful when overriding methods but still needing 
# to incorporate the parent’s behavior.

# class Animal:#parent

#     def make_sound(self):
#         print("Animal is making sound")
    
# class Dog(Animal):#child
        
#         def __init__(self,  name):
#             self.name = name

#         def make_sound(self):
#             super().make_sound()
#             print(f"{self.name } is  Barking") 
        
#         def get_angry(self):
#              self.make_sound()
#              print(f"{self.name } is  Angry!!") 

# A = Dog("kaalu")

# A.make_sound()

# A.get_angry()



# Abstract classes

# from abc import ABC , abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
# class motor(Vehicle):
        
#         def __init__(self , name):
#              self.name = name

#         def start_engine(self):
#              print("Engine started")

# a=motor("a")
# a.start_engine()




# Homework

# 1.Getters and Setters:
# Create a class BankAccount with a private attribute balance.
# Write a getter method to retrieve the balance and a setter method to update it,
#  ensuring the balance never goes below zero.

# class bankAccount:
#     def __init__(self , balance ):
#         self.__balance = balance

#     def get_balance(self):
#         print(f"Balance:{self.__balance}")

#     def set_balance(self,update_balance):
#         if update_balance < 0:
#             print("ERROR,Balance connot reach negative")
#             return

#         self.__balance = update_balance
#         print(f"Balance:{self.__balance}")

# a = bankAccount(100)
# a.get_balance()
# a.set_balance(10000)
# a.get_balance()
# a.set_balance(-10000)
        


# 2.Method Overloading:
# Write a class Calculator with a method multiply(). Allow it to take either two or three arguments 
# to multiply two or three numbers.

# class calculator:
#      def multiply(self,a,b,c=1):
#             print(f"Result:{a * b * c}")
       
# cadsw = calculator()
# cadsw.multiply(2,1)
# cadsw.multiply(2,1,4)


# 3.Method Overriding:
# Create a parent class Shape with a method draw() that prints "Drawing shape".
# Create a child class Circle that overrides draw() to print "Drawing circle".

# class shape:
#     def draw(self):
#         print("Drawing shape")
# class Circle(shape):
#     def draw(self):
#         print("Drawing circle")

# c = Circle()
# c.draw()


# 4.Abstract Classes:
# Define an abstract class Employee with an abstract method calculate_salary().
# Create a subclass Manager that implements calculate_salary() based on working hours 
# and rate per hour.

# from abc import ABC , abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calc_salary(self):
#         pass

# class manager(Employee):
#     def calc_salary(self):
#         print("Manager salary is calculated")