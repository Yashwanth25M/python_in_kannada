# constructor(__init__) and self keyword
# briefing about class , attributes ,etc


# creating multiple objects with different attributes

# class Laptop:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#     def show_info(self):
#         print(f"Laptop Brand: {self.brand}, Price: ₹{self.price}")
# laptop1 = Laptop("Dell", 45000)
# laptop2 = Laptop("HP", 55000)#can create as many as laptops as possible
# laptop1.show_info()
# laptop2.show_info()



# Optional parameters in constructors
# class Book:
#     def __init__(self, title, author="Unknown"):
#         self.title = title
#         self.author = author
#     def show_book(self):
#         print(f"Title: {self.title}, Author: {self.author}")
# book1 = Book("Python Programming")#here author is not mentioned 
# # if we doesnot specify :author="Unknown" : 
# # it will be trowing missing argument error
# book2 = Book("Machine Learning", "Andrew Ng")
# book1.show_book()
# book2.show_book()

# similarly it can be used in functions also 



# Homework
# 1.Create a Class with a Constructor:
# Write a class Movie with attributes title and rating using the __init__() constructor.
# Define a method to display the movie’s title and rating.

# class Movie:
#     def __init__( self , title , rating ):
#         self.title = title
#         self.rating = rating

#     def display(self):
#         print(f"The movie {self.title} has gained IMDB ratings of {self.rating} ")

# movie1 = Movie("A" , 5)
# movie2 = Movie("B" , 8)

# movie1.display()
# movie2.display()

# 2.Add Default Parameters:
# Create a class Employee with attributes name, designation, 
# and salary (default value of salary is 30,000).
# Write a method that displays the details of each employee.
# Create multiple Employee objects with different values for name and designation, 
# and test the default salary behavior.

# class Employee:
#     def __init__ (self , name , designation , salary = 30000 ):
#         self.name = name
#         self.designation = designation
#         self.salary = salary

#     def display(self):
#         print(f"The employee {self.name} with designation {self.designation} earns salary of {self.salary}")

# emp1 = Employee("Emp 1" , "CEO" , 100000)        
# emp2 = Employee("Emp 2" , "MANAGER" , 50000)        
# emp3 = Employee("Emp 3" , "INTERN" ) #here intern salary is not specified thus takes default value of 30000

# emp1.display()
# emp2.display()
# emp3.display()