#looops(while )
# while condition : #executes until condition is true
    #code executes

#break #stops execution of loops
#continue #skips current iteration


# print("Hello")

# #extra (crack a passcode of 4 digit)
# import time
# pin = 3418  # Python interprets 0268 as 268
# cracker = 0
# attempt = 1
# start_time = time.time()  # Start the timer
# while True:
#     if cracker == pin:
#         end_time = time.time()  # Stop the timer
#         elapsed_time = end_time - start_time  # Calculate total time

#         print(f"Pin found at attempt number {attempt}")
#         print(f"The pin is {cracker:04d}")  # Ensures four-digit format
#         print(f"Time taken: {elapsed_time:.4f} seconds")  # Print time taken
#         break
#     elif attempt < 10000:  # 0000 to 9999 range
#         cracker += 1
#         attempt += 1
#     else:
#         print("Pin not found within the expected range.")
#         break




# Homework
# 1.Multiples of 3:
# Write a for loop that prints all multiples of 3 between 1 and 30.
# Answer
# print("Multiples of 3 between 1 and 30.")
# i = 0
# for i in range(0,31):
#     if(i % 3 == 0):
#         print(i)

# 2.Sum of First 10 Numbers:
# Write a program using a for loop that calculates the sum of numbers from 1 to 10.
# sum=0
# for i in range(0,11):
#     sum = sum +i
# print(f"The sum of numbers from 1 to 10 is {sum} ")

# 3.Print Your Name Letter by Letter:
# Write a program that takes your name as input and prints each letter 
# of your name using a for loop.
# Answer
# Name = "Yashwanth"
# for i in Name:
#     print(i)


# 4.Count Vowels in a String:
# # Write a program that counts how many vowels are in a given string using a for loop.
# vowels = "a e  i o u A E I O U"
# string_input = "Arun"
# nm=0
# for a in string_input:
#     if(a in vowels):
#         nm = nm +1
# print(f"The total number of vowels in {string_input} is {nm}")