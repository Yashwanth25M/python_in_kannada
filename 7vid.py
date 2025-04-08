# Tuples and sets
# Tuples( Tuples are  collection of ordered items , that are immutable (cannot change)  )
a = ( " a " , 1 , 3.14 , 3.14) 
b = (  )  #empty tuple
c = ( 1 , 2 ,3 ,("abd")) #nested tuple

# print(a) #prints a tuple
# print(type(a))
# print(len(a))

# accesing_Elements
# print(a[0:4])

# Tuples_methods or function
# a[0]=' b ' #throws an error bcz tuple is immutable
# appending or inserting elements to tuple is not possible
# its achived through x = a + (32)
# or through converting tuple to list , apppend element to list ,them convert list to tuple
# l  = ( 1 , 2, 3 )
# print(l) #printing original tuple
# l_list = list(l) #conversion of tuple to list
# print(l_list)
# num = 4
# l_list.append(num) #appendinf element to list
# print(l_list)
# l = tuple(l_list) #converting list to tuple
# print(l)

# #Tuple_concatenation 
# t1 = ( 1 , 2 , 3)
# t2 = ( 4 , 5)
# t3 = t1+ t2
# print(t3)

# #Tuple_replication
# repeat = (1 , 2)
# print( repeat *2)

# #Checking membership
# mem = ( 1 , 2 , 3)
# print( 1 in mem)

#obtaining a index
# obt = ( 1 , 2 ,3 )
# print( obt.index(2))

#count
# num = ( 1 ,2 ,1)
# print(num.count(1))

# Advantages
# immutable(cannot change)
# faster than list due to its immutablility
# can be used as a keys in dictoniary

# sets (do not allow duplication of items , mutable(allow changes) , unindexed , unordered)
# set={ 1 , 2 , 3 }
# print(set)
# unordered = { 20 , 1 ,2 , 100 ,4} #prints  {1, 2, 100, 4, 20}
# print(unordered)

# another way of creating set
# s1 = set(( 1 , 2 , 3))
# print(type(s1))

# # empty set 
# s2 = set(())
# print(type(s2))

# cannot access items through indexing 

# # operations on sets
# s1 = {1, 2 , 3}
# s2 = { 3 , 4, 5}
# # print(s1 | s2 ) #union
# # print(s1 & s2 ) #intersection
# # print(s1 - s2 ) #difference

# s1.add(20)
# s1.remove(20)
# s1.remove(200) # raises an error 
# s1.discard(200) #unlike s1.remove(200) which raiuses error whn an elemnt is not present , it performs check if present only remove 
# s1.pop()#removes an random element
# s1.clear() #removes all elements

# Homework
# 1.Basic Dictionary Operations:
# Create a dictionary to store information about 5 cities in Karnataka and 
# their famous dishes.
# Add a new city and its dish to the dictionary.
# Update the dish for Bengaluru.
# Remove one city from the dictionary.
# Use the keys() method to print all city names in the dictionary.
# Use the values() method to print all dishes in the dictionary.
# Answer
# ci_fo = {"bengaluru" : "A" , "Mysuru" : "Pak" , "Shivamogga" : "Dosa"}
# ci_fo["bengaluru"] = "a"
# print(ci_fo)
# ci_fo["Bengaluru"] = "b"
# print(ci_fo)
# ci_fo.pop("Mysuru") #del.ci_fo["Mysuru"]
# print(ci_fo)
# print(ci_fo.keys())
# print(ci_fo.values())

# 2.Nested Dictionary Practice (Simple for now):
# Create a dictionary to store details of two of your friends, including their names, 
# favorite subject, and favorite food.
# Access and print the favorite food of one friend.
# Answer
# frend = { "friend1" :{"Name" : "A" , "Fav_sub" : "Maths" ,"Food" : "Chicken"},
#          "friend2":{"Name" : "B" , "Fav_sub" : "Science" ,"Food" : "Biriyani"} }
# print(frend["friend1"]["Food"])