# input from users
# taking a input from users
# a = input()

# obtaining an output 
# print(a)

# concatenation
# owner=input("Enter Owner name : ")
# employee=input("Enter employee name : ")
# print(employee+" is Working under " +owner)

# formtted string
# print(f"{employee} is Working under {owner}") # is same as print(employee+" is Working under " +owner)

# Taking particular datatype as input
# x1 = int(input("Enter integer number as input : "))
# x2 = float(input("Enter float as input : "))
# x3 = str(input("Enter string as input : "))
# The usage of taking paarticular data-type as input helps to carry out arithmetic operation among same data-types

# To convert negative number to a positive number (abs)
# z=-1 
# print(z)
# m=abs(z) #absolute-value
# print(m)

# different types of comments (single-line and multi-line comments)


#single-line comment


"""This is multiline-comment
   This is multiline-comment""" 

'''This is multiline-comment
   This is multiline-comment'''
    



# HW
# Homework

#  question 1 : Simple Greeting Program: Write a Python program that asks the user and age, then prints a personalized 
# greeting message. Use both the f-strings for output. for their name operator and
# Answer
# name=input("Enter your name : ")
# age=input("Enter your age : ")
# print(f"Hello , {name}! You are {age} years old .")




#  question 2: String Manipulation Exercise: Write a Python program that:Takes a sentence as input from the user.
# • Prints the sentence in all uppercase and lowercase.
# • Replaces all spaces with underscores.
# • Removes leading and trailing whitespace.
# answer
# in_put=input("Input :") #input:   python is awesome!    
# print(f'''uppercase: {in_put.upper()}
# Lowercase: {in_put.lower()}
# Replaced: {in_put.replace(" " , "_")}
# stripped: {in_put.strip()}
#       ''')


# question 3: Character Counter: Write a Python program that:
# • Asks the user for a string.
# • Prints how many characters are in the string, excluding spaces.
# # answer
# str_ing=input("Enter a string")
# print(len(str_ing.replace(" " , "")))



# 4. Escape Sequence Practice: Write a Python program that uses escape sequences to print the following output:
# Example:
# Hello
#     World
# This is a backslash: \
# Answer
# print("Hello\n\tWorld \nThis is a backslash: \\ ")