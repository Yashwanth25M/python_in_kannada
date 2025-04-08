# assignment_operators
a=10
a+=10 # is same as a=a+10 
a-=10 # is same as a=a-10 
a*=10 # is same as a=a*10 
a/=10 # is same as a=a/10

# compsarison_operators(used to compare the values)
a = 10 
b =20
a==b #used to check weather a is equal to b
a<b #used to check weather a is lesser than  b
a>b #used to check weather a is greater than  b
a<=b #used to check weather a is lesser than or equal to b
a>=b #used to check weather a is greater than or equal  to b
a!=b #used to check weather a is  not equal to  b

#logical_operator(AND,OR,NOT)

'''
a  b AND OR       a NOT       1=TRUE
0  0  0   0       1 0         0=FALSE
1  0  0   1       0 1
0  1  0   1
1  1  1   1 
'''
# print( 0 and 0) #And operation
# print( 0 or 0) #OR operation
# print(not(0)) #NOT operation
# print(not(1)) #NOT operation
# print(not(True)) #NOT operation
# print(not(False)) #NOT operation

# Membership_operator
# a = "Name"
# print("N" in a) #used to check weather a particular character present is a string
# print("Name" in a) #used to check weather a particular character present is a string
# print("n" in a) #because py is case sensetive
# print("n" not in a) #because py is case sensetive



# Homework
# 1.List Manipulation Exercise:
# Create a list of 5 items (strings or numbers).
# Add a new item to the end of the list and another at the second position.
# Remove the third item from the list.
# Print the list after each operation.
# Answer
# li = ["a" , "b" , "c" , "d" , "e"]
# print(li)
# li.append("e")
# print(li)
# li.insert(2 , "w")
# print(li)
# li.pop(3)
# print(li)

# 2.Reverse and Sort a List: Create a list of numbers and:
# Sort it in descending order.
# Reverse the sorted list and print it.
# li1 = [1 , 2 ,3 ,4 ,5]
# print(li1)
# li1.sort(reverse = True)
# print(li1)
# li1.reverse()
# print(li1)