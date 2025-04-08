# strings
# concatenation of string
# first_name = "Siddhu"
# last_name = "moosewala"
# full_name = first_name + " "+  last_name
# print(full_name)


#string replication
# message = "Warning! "
# print(message * 5)


a=" empty text " 
# print(a.lower()) #"lowers every letter"
# print(a.upper()) #"capitalize every character"
# print(a.strip())  #"removes empty spaces while printing  "
# message=" There is a sheep"   
# print(message)
# print(message.replace("sheep","lion")) #"replces word the format must be '.replace(old_word,new_word)"
# print(message.replace("lion","sheep")) #"format is wrong thus word'lion' not found thus returns original string"

#  function of strings
# sample_text="This is a sample text" 
# print(len(sample_text))  # returns length of given string
# print(sample_text.count("a"))   #counts no.of occurences of particular character


# multi-line string
# text = " There lives a monster
# He is 6ft high "                throws an error
# text = """ There lives a monster
# He is 6ft high """     # this doesnt throws an error
# print(text)

# indexing of strings
#  S    I    D    H    A    R    T
#  0    1    2    3    4    5    6
# (-7) (-6) (-5) (-4) (-3) (-2) (-1)

# string manipulations ( index  = position - 1)
# name = "SIDHART"
# print(name[1]) #accessing a particular character from string 
# print(name[-6]) #same as above

# string slicing (string[start:end:step])
# print(name[1:5]) #start from index 1 to 4(5-1)
# print(name[0:7]) #prints whole string
# print(name[0:]) #same as above
# print(name[:7]) #same as above
# print(name[0:7:2]) #maintains step-value/skip-value of 1

# escape sequence
# print(" BEWARE \n Dragon lives here") #moves text to next line
# print("NOt human friendly \t Dont feed") #maintain tab space
# print("Dragon is \"Endangered species\"") #to maintain double quotes("")





# Homework
# 1. Logical Operator Practice: Write a Python program that takes two numbers as input from the user and checks if:
# • Both numbers are greater than 10 (using and).
# • At least one of the numbers is less than 5 (using or).
# • The first number is not greater than the second (using not).
# Answer
# n1=int(input("num1:"))
# n2=int(input("num2:"))
# if( n1 > 10 and n2 > 10):
#     print("Both numbers are greater than 10")
# elif(n1 > 5 or n2 > 5):
#     print("Atleast one number is less than 5")
# elif(n1 < n2):
#     print("The first number is not greater than the second")
# else:
#     print("Something went wrong!!")

# 2.Comparison Operator Challenge: Create a Python program that asks the user for their age and prints:
# "You are an adult" if the age is greater than or equal to 18.
# "You are a minor" if the age is less than 18.
# Use >= and < comparison operators.
# Answer
# age = int(input("Enter your age : "))
# if(age>= 18):
#     print("You are an adult")
# else : 
#     print("You are a minor" )

# 3.Membership Operator Exercise: Write a Python program that:
# Takes a string as input from the user.
# Checks if the letter 'a' is in the string (using in).
# Checks if the string doesn't contain the word "Python" (using not in).
# # Answer
# in_put = input("Enter a string : ")
# if("a" in  in_put):
#     print("Yes letter 'a' is in the string ")
# if("Python" in in_put):
#     print("string  contain the word \"Python\"")
# else :
#     print("string doesn't contain the word \"Python\"")


# 4.Bitwise Operator Task: Given two integers, write a Python program that:
# Prints the result of a & b, a | b, and a ^ b.
# Shifts the bits of a two positions to the left (a << 2).
# Shifts the bits of b one position to the right (b >> 1).
# Answer
# Not intrested