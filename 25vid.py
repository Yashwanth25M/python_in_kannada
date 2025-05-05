# The four pillars of OOP( homework pending)
# 1.Abstraction(hide mechanism)
# 2.Encapsulation(hide data manipulation)
# 3.inheritence(inherit some charcter)
# 4.Polymorphism

# Abstraction
#Definition: Abstraction hides the complex inner workings of an object, 
# exposing only the essential parts for interaction.
# Real-World Example: Think about driving a car. You use the steering wheel
#  and pedals to control the car, without needing to know the engine mechanics
#  or braking systems.

# class Car:
#     def start_engine(self):
#         print("Engine started")

#     def accelerate(self):
#         print("Car accelerating")

#     def brake(self):
#         print("Car stopping")

# car = Car()
# car.start_engine()  # Abstracts complex internal workings
# car.accelerate()
# car.brake()


# l = [ 1 ,  2 , 3 ]
# l.append(5)#we know append insert element to last of list but not aware of mechanism 


# Encapsulation

# Definition: Encapsulation involves wrapping data and methods that operate on that data 
# within one unit, such as a class. This protects the data from external interference and 
# misuse, improving security and maintainability.
# Real-World Example: Imagine an ATM machine—you interact with a limited interface 
# (e.g., withdraw, deposit, check balance) but do not have access to the inner mechanics 


# class ATM:
#     def __init__(self, balance):
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"Deposited {amount}. New balance: {self.__balance}")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.__balance}")
#         else:
#             print("Insufficient balance")

# atm = ATM(1000)
# atm.deposit(500)
# atm.withdraw(300)




# Homework

# 1.Encapsulation:
# Create a BankAccount class with private attributes for account_number and balance.
# Add methods to check balance, deposit, and withdraw funds.
# Try accessing the balance directly and observe the result.

# class Bankaccount:
#     def __init__(self , balance , accountnumber):
#         self.__balance =  balance
#         self.__accountnumber = accountnumber

#     def deposit(self,amount):
#         self.__balance += amount
#         print(f"The amount of {amount} was succesfully deposited \n Total balance:{self.__balance}")

#     def withdraw(self,amount):
#         if(amount <= self.__balance):
#             self.__balance -= amount
#             print(f"Collect yor cash \n Balance {self.__balance}")
#         else:
#             print(f"Insufficient balance . Balance:{self.__balance}")

# p1=Bankaccount(39000,1234)
# p1.deposit(200)
# p1.withdraw(39000)
# p1.withdraw(3900)


# 2.Abstraction:

# Design a Phone class with methods to call_contact and take_picture. Abstract away any internal processing details 
# and focus on creating a user-friendly interface.

# import time
# class phone:

#     def __init__(self):
#         pass

#     def call_contact(contact):
#         for i in range(0,3):
#             print("ringing")
#             time.sleep(1)
#         print(f"calling {contact}")
    
#     def take_picture():
#         print(f"Smile please")
#         for i in range(0,3):
#             print(i,"\n")
#             time.sleep(1)
#         print("Photo captured")

# phone.call_contact("ramesh")
# time.sleep(4)
# phone.take_picture()
