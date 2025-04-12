#only 11 videos remaining
#Function-advanced concepts

#   variable length argument(method to insert any no.of inputs to a function)

# def add(a):#only one variable is passed
    # print(a)
# add(1)#if multiple variables passed throws an error

# def add(*a):#(by using "*" multiple can be passed)
#     print(a)
# add(1, 2 , 3)

# def add(*numbers):
#     return sum(numbers)
# print(add(1,2,3,4))

# def mul(*numbers):
#     n=1
#     for nam in numbers:
#         n = n * nam 
#     return n
# print(mul(1,2,3,4))

# use * for tuples , where ** used for dictionaries 

# def student_info(**details):#key words arguments
#     for key, value in details.items():
#         print(f"{key}: {value}")
# student_info(name="Anand", age=22, course="Python")

# def total_sum(*numbers):
#     result = 0
#     for num in numbers:
#         result += num
#     return result
# print(total_sum(1, 2, 3, 4))

# Lambda function(A lambda function is a small anonymous function 
# that can take any number of arguments but has only one expression.)

# def add(a,b):
#     return a+b
# print(add(3,4))

# add = lambda a , b : a + b #shortcut of above function
# print(add(1,2))  

# double = lambda x : print(f"The double of {x} is {x*2}")
# double(2)


# use case of lambda

# students =[
#     {"name" : "a" , "age" : 3},
#     {"name" : "b" , "age" : 5},
#     {"name" : "c" , "age" : 4}
# ]
# students.sort(key = lambda x : x["age"])# age is only used to compare
# students.sort(key = lambda x : x["age"],reverse = True)# sort in decending order
# print(students)




# def get_age(student):#here two functions are used to sort a same list of dictionaries
#     return student["age"]
# def sort_students_by_age(students):
#     students.sort(key=get_age) 
#     return students
# students = [
#     {"name": "a", "age": 3},
#     {"name": "b", "age": 5},
#     {"name": "c", "age": 4}
# ]
# sort_students_by_age(students)
# print(students)



# Recursion(function calling it self again and again)
# used in calculating factorial of a number
# 4! = 4 X 3 X 2 X 1
# def fact(n):
#     if(n == 1):
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(3))

# def fact2(number):#normal method to find factorial without recursion function
#     # a=[]
#     for i in range(1 , number+1):
#         a.append(i)
#     return(fact3(a))
# def fact3(a):
#     n=1
#     for nam in a:
#         n = n * nam 
#     return n
# print(fact2(3))

# nested function
# def outer_function(name):
#     def inner_function():
#         print(f"Hello, {name}!")
#     inner_function()
# outer_function("Anand")

# def calculate(a,b):
#     def sum():
#         print(f"The sum is {a+b}")
#     def sub():
#         print(f"The sub is {a-b}")
#     def mul():
#         print(f"The mul is {a*b}")
#     sum()
#     sub()
#     mul()
# calculate(10,5)

# Homework

# 1.Lambda Function: Write a lambda function that multiplies two numbers.
# mul =  lambda  a , b : print(a*b) 
# mul(3,4)

# 2.Recursive Function: Write a recursive function that calculates the sum of
#  the first n numbers.
# def call(n):
#     if n==1 :
#         return 1
#     return n + call(n-1)
# print(call(5))

# 3.Variable-Length Arguments: Write a function that accepts
# any number of arguments  and returns their average.
# def avg1(*numbers):
#     a=[]
#     for n in numbers:
#         a.append(n)
#     return(sum(a)/len(a))
# print(avg1(1,2,3,4))