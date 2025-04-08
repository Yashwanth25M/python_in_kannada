#for loop
# for i in range (1,101,3) : # prints a number from 1 to 100 with step of 3
#     print(i)


# city=["bengaluru" , "Newdelhi" , "Mumbai"] # print individual city
# for item in city  :
#     print(item)


# str = "Bengaluru" # printing each alphabet
# for items in str:
#     print(items,end=" ")


# str = "Bengaluru" # printing each alphabet with index
# for items in enumerate(str):
#     print(items,end=" ")


# str = "Bengaluru"#else part is not executed as "a " is not printed
# for items in str:
#     print(items)
#     if(items == 'a'):
#         break
# else:
#     print ("all are printed")


# str = "Bengaluru"#else part is  executed as "x " is not found
# for items in str:
#     print(items)
#     if(items == 'x'):
#         break
# else:
#     print ("all are printed")

# dict1 = { ' name ' : "A" , "age" : 21 , "occ" : "add"}#adds in tuple
# print(dict1.items())
# #output     dict_items([(' name ', 'A'), ('age', 21), ('occ', 'add')])


# dict = { ' name ' : "A" , "age" : 21 , "occ" : "add"}
# for key, value in dict.items():
#     print(key , "" , value)


#nested for loop
#multiplication table
# num = 2
# for i in range(1,11):
#     print(f"{num} X {i} = {num*2}") # single multiplication table


# multiple multiplication table
# for i in range(1,5):
#     print(f" \n printing {i} table \n")
#     for j in range(1,11):
#         print(f"{i} X {j} = {i * j}")

# Homework
# 1.List Manipulation:
# Create a list of Kannada foods. Use list comprehension to create a new list 
# where each food name is in uppercase.
# food=["idli", "dosa", 'bath']
# u_foods=[ items.title() for items in food] #.upper makes every letter capital 
# print(u_foods)#whereas .title makes first alphabet only capital 

# 2.Sum of Prices:
# Create a dictionary of 5 items with their prices. 
# Write a program that calculates the total price of all items using a for loop.
# Answer
# menu = {"A" : 10 , "B" : 20 , "C" : 100}
# price =  0
# for  key , values in menu.items():
#     price = price + values
# print(f"The total price is {price}")
# print(sum(list(menu.values())))#simple single line solution


# 3.List of Squares:
# Create a list of numbers from 1 to 10. 
# Use list comprehension to generate a list of their squares.
# li = [ nm*nm for nm in range(0,11)]
# print(li)

# 4.Student Data Task:
# Create a list of 3 dictionaries, where each dictionary contains the name, age, 
# and marks of a student. Loop through the list and print each student's information.
# li = [ { "name" : "a" ,"age " : 12 , "marks": 100},
#        { "name" : "b" ,"age " : 2 , "marks": 100},
#        { "name" : "c" ,"age " : 122 , "marks": 100}]
# for student in li:
#     print(student["name"],"----",student["marks"])

# 5.Dictionary Comprehension:
# Create a dictionary where the keys are Kannada cities, 
# and the values are their populations. Use dictionary 
# comprehension to filter out cities with populations
#  below 10 lakhs.
# Answer
# dict1 ={"a" : 12 , "b":33 , "c": 55 , "d":1 , "e": 4}
# dict2 ={items1:key1 for items1,key1 in dict1.items() if key1 >10}
# print(dict2)

# 6.Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:
# Prints the entire matrix row by row.
# Prints the sum of each row in the matrix.
# matrix = [
    # [1, 2, 3],
    # [4, 5, 6],
    # [7, 8, 9]
# ]
# Answer(ond churu thale kedsuthe)(..)

# rows = int(input("Enter number of rows: "))
# columns = int(input("Enter number of columns: "))
# matrix = []
# for i in range(rows):
#     row = []
#     for j in range(columns):
#         x = int(input(f"Enter element for row {i+1}, column {j+1}: "))
#         row.append(x)
#     matrix.append(row)
# print("\nMatrix:")
# print(matrix)
