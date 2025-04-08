# list
items=['bru' , ' sugar ' , ' milk ','milk',[1,2,3]] # list is a collection of  ordered items, mutable(changeable) , allow duplication 
# print(type(items))
empty_list = []# This is empty list

# another way of creating list
# s1 = list(( 1 , 2 , 3))
# print(type(s1))

# list operations
# print(items[4][2]) 'accesing a second element of list under a list 
# items.pop() 'removes last element
# items.pop(2) 'removes index 2 element
# items.append("apple") 'adds item to last
# items.remove(' sugar ') 'removes particular element
# items.insert(2,'apple') 'adds item to index 2
# items[0]='kotas' 'replcement'
# list[start:stop:step]
# print(items[0:5]) print(items[0:]) print(items[:5])' all  print whole list'
# print(items[0:4]) 'print only from index 0 to 3
# print(items[0:4:3]) 'prints items from index 0 to 3 with stepvalue of 3 (meaning skips 2 items)'
# print(items)

# list function
# print(len(items)) 'counts no.of items in list'
numbers=[1,2,3,45,30,55,7,1]
# numbers.sort() 'sorts number in ascending order'
# print(sorted(numbers)) ' same as above'
# numbers.sort(reverse = True)'sorts number in ascending order'
# print(sorted(numbers,reverse = True)) #' same as above'
# print(sum(numbers)) 'performs sum operation on items  '
# if other than int,float contains show unsupported operand type(s)
# print(numbers.index(3)) 'returns index of particular item'
# print(numbers.count(1)) 'returns no.of occurences'
# print(numbers)
# numbers.reverse() 'reverses a list'
# print(numbers)

# nested list 
matrix=[[ 1 , 2 ] , [ 3 , 4 ] ,[ 5 , 6 ]]
# print(matrix[0][1]) 'to access a second lement of first list'

# Homework
# 1.Tuple Operations:
# Create a tuple with 5 elements.
# Try to modify one of the elements. What happens?
# Perform slicing on the tuple to extract the second and third elements.
# Concatenate the tuple with another tuple.
# Answer
# tup_le = ( 1 ,2 , 3 , 4 , 5 )
# # tup_le.append(3) as tuple is immutable 
# tup1= tup_le[2:4]
# print(tup1)
# tup3 = tup_le + tup1
# print(tup3)

# 2.Set Operations:
# Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
# Find the union, intersection, and difference between the two sets.
# Add a new fruit to your set.
# Remove a fruit from your set using both remove() and discard().
#  What happens when the fruit doesn’t exist?
# Answer
# a = { "Apple" , "Banana" , "Tomato" , "Jackfruit"}
# print(a)
# b = { "Kiwi" , "Mosambi" , "watermelon" , "Orange"}
# a.add("Orange")
# print(a)
# a.remove("Apple") #in remove if item not exit throws an error
# print(a)
# a.discard("Orange")#in discard if item not exit throws an error
# print(a)

# 3.Tuple and Set Comparison:
# Create a list of elements and convert it into both a tuple and a set.
# Print both the tuple and the set.
# Try to add new elements to the tuple and set. What differences do you observe?
# Answer
# li = [1 , 2 , 3]
# print(type(li))
# print(li)
# tu=tuple(li)
# print(type(tu))
# print(tu)
# se=set(li)
# print(type(se))
# print(se)
# Tuple is immutable , whereas set is mutable .
# Thus elements can be inserted into sets but not tuple.