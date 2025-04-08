# #conditional statements

# # program to find weaher a number is even or odd
# x = 24
# if x % 2 == 0:
#     print(f"{x} is even ")
# elif x % 2 ==1 :
#     print(f"{x} is odd ")
# else :
#     print("An error occured")    


# Homework
# 1.Basic Counting with while Loop:
# Write a program that counts from 1 to 10 using a while loop.
# # Answer
# print("Counting from 1 to 10 \n")
# i=1
# while(i<11):
#     print(i," \n ")
#     i = i + 1

# 2.Odd Numbers Printer:
# Create a program that prints all odd numbers between 1 and 20 using a while loop.
# Answer
# print("Printing odd numbers from 1 to 20 \n")
# i= 0 
# while(i<21):
#     if(i % 2 != 0):
#         print(i,"\n")
#     i = i + 1


# 3.Ticket Booking Simulation:
# Write a program that simulates a bus ticket booking system. The bus has 8 seats. 
# Each time a seat is booked, the available seats decrease. When there are no seats left, 
# the loop stops and displays a message saying "All seats are booked."
# Answer
# seats = 8  # Total number of seats available
# while seats > 0:
#     print(f"Seats available: {seats}")
#     booking = input("Do you want to book a seat? (yes/no): ").strip().lower()
#     if booking == "yes":
#         seats -= 1
#         print("Seat booked successfully!")
#     elif booking == "no":
#         print("Booking canceled.")
#         break
#     else:
#         print("Invalid input. Please type 'yes' or 'no'.")
# if seats == 0:
#     print("All seats are booked.")

# 4.Countdown Timer:
# Write a program that counts down from 10 to 1 using a while loop and prints 
# "Happy New Year!" after the countdown is over.
# # Answer
# import time
# print("starting countdown!!")
# i=10
# while(i>0):
#     print(i)
#     time.sleep(1)
#     i = i - 1
# print("Happy New Year!")