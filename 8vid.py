#dictionaries
#dictionaries is  collection of key-value pair , unordered and mutable 
# Vasulii = { "per1" : 100 , "per2" : 3000 ,[2.1]:23.45,  {"abd"}:365 , (123) : 3.14}
#can contain anything except list[] as charcter(bcz strings are immutable)

# #accessing items of dictionary
# print(Vasulii['per1'])
# # print(Vasulii['per3']) #throws an error as key not present
# print(Vasulii.get('per3'))#does not print anything if no key
# print(Vasulii.get('per3' , "not found"))#prints a default (noot found) which is changeable
# # print(Vasulii.get['per1']) #throws a error

# #functions of dictionary
# #adding key-value to existing dictionary
# print(Vasulii) #before adding
# Vasulii["per4"] = 500
# print(Vasulii) #after adding
# Vasulii["per2"] = 500 #updating values
# # print(Vasulii) #after update
# Vasulii2={ 'per40' : 50000 }
# Vasulii.update(Vasulii2)# adding another dictionary to previous one
# print(Vasulii)
# Vasulii.pop("per2")#removing 'per2'
# print(Vasulii)#after removing
# del Vasulii['per1'] #same as pop
# Vasulii.clear()#clears whole dictionary 

#dictionary methods
# print(Vasulii.keys())#returns keys of dictionary
# print(Vasulii.values())#returns values of dictionary
# print(Vasulii.items())#returns  items of dictionary

# Homework
# 1.Basic Conditions:
# Write a program to check if someone is eligible for a bus pass. 
# If they are below 5 years, the bus pass is free.
#  If they are 60 years or older, they get a senior citizen discount. 
# Otherwise, they pay the full price.
# Answer
# print("Program to check if someone is eligible for a bus pass. ")
# age = int(input("Enter your age: "))
# if(age<5):
#     print("Below 5 years, the bus pass is free.")
# elif(age>=60):
#     print("Congrats!! on  senior citizen discount")
# else:
#     print("Pay the full price.")

# 2.Meal Time Checker:
# Create a program that checks the time of day (24-hour format) 
# and prints whether it's time for breakfast, lunch, or dinner.
# Breakfast: 8 AM (8)
# Lunch: 1 PM (13)
# Dinner: 8 PM (16)
# If none of these times, print "It's not meal time."
# Answer
# print("Meal Time Checker:")
# time = int(input("Enter time in 24hr format:"))
# if(time == 8):
#     print("Breakfast time!!")
# elif(time == 13):
#     print("Lunch_break")
# elif(time == 18):
#     print("Dinner time!!")
# else:
#     print("It's not meal time.")

# 3.Simple Eligibility Check:
# Write a program that checks whether a person is eligible for a library membership.
#  If they are under 18, they get a student membership.
#  If they are 60 or older, they get a senior citizen membership.
#  Otherwise, they get a regular membership.
# Answer
# print("Eligible for a library membership")
# age=int(input("Enter your age:"))
# if(age<=18):
#     print("You are elegible for student membership")
# elif(age>=60):
#     print("You are elegible for senior citizen membership")
# else:
#     print("You are elegible for regular membership")