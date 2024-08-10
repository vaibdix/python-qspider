# import time
# def outer(func):                         # ----------> Address ( Main function ie add )
#     def inner(*args, **kwargs):          # ----------> main function parameters
#         time.sleep(5)
#         print("from inner func")
#         func(*args, **kwargs)
#         print("addition done")
#     return inner
#
# @outer
# def add(a, b):
#     time.sleep(5)
#     print(a+b)
#
# add(2,5)








###############################
# SINGLE DECORATORE
###############################

import time
# def outer(add):                         # ----------> Address ( Main function ie add )
#     def inner(*args, **kwargs):         # ----------> main function parameters can pass a , b aswell
#         time.sleep(5)
#         print("from inner func")
#         add(*args, **kwargs)            # ----------> a, b can be passed aswell
#         print("addition done")
#     return inner
#
# @outer
# def add(a, b):
#     time.sleep(5)
#     print(a+b)
#
# add(2,5)



###############################
# MULTIPLE DECORATORE
###############################

# decorator fucntion to calculate execution time of program
# import time
#
# def outer(func):
#     def inner(*args, **kwargs):
#
#         start = time.time()
#
#         func(*args, **kwargs)
#         print(f"{func.__name__} done")     # __name__ prints function names in execution
#
#         end = time.time()
#         execution_time = end - start
#         print(execution_time)
#     return inner
#
# @outer
# def add(a, b):
#     time.sleep(5)
#     print(f"Addition: {a + b}")
#
# @outer
# def sub(a, b):
#     time.sleep(5)
#     print(f"Subtraction: {a - b}")
#
# @outer
# def mul(a, b):
#     time.sleep(5)
#     print(f"Multiplication: {a * b}")
#
# add(2, 5)
# sub(2, 5)
# mul(2, 6)





#############################################
# using multiple decorator run outer function
#############################################


# def outer(func):
#     def inner():
#         print("qspider")
#         func()
#     return inner
# def outer_most(func):
#     def wrapper():
#         print("pypider")
#         func()
#     return wrapper

# @outer_most
# @outer
# def welcome():
#     print("hello there")

# welcome()








# write a program to create decortor to which
# prints the name of called function along with it should check if number is even or odd





# def even_or_odd_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         number = args[0] if len(args) > 0 else kwargs.get('number')
#         if isinstance(number, int):
#             print(f"Function {func.__name__} called with number {number}")
#             if number % 2 == 0:
#                 print(f"{number} is even")
#             else:
#                 print(f"{number} is odd")
#         return result
#     return wrapper
#
# @even_or_odd_decorator
# def print_number(number):
#     return number
#
# @even_or_odd_decorator
# def add_numbers(a, b):
#     return a + b
#
# print_number(15)
# add_numbers(5, 7)
# print_number(8)











# V@V2V2V2V2V2V2V2V2V2VV2V2V2V2V2
#################################
#
# def check_even_odd(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         result = func(*args, **kwargs)
#         if args and isinstance(args[0], int):
#             number = args[0]
#             if number % 2 == 0:
#                 print(f"The number {number} is even.")
#             else:
#                 print(f"The number {number} is odd.")
#         else:
#             print("The first argument is not an integer or no arguments were provided.")
#         return result
#     return wrapper
#
# @check_even_odd
# def print_number(number):
#     print(f"Number: {number}")
#
# @check_even_odd
# def multiply_number(number, multiplier):
#     print(f"Result: {number * multiplier}")

# print_number(4)
# multiply_number(7, 3)











# create a decorator to return only positive output from any substraction

# def positive_output_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, (int, float)):
#             if result < 0:
#                 return -result
#         return result
#     return wrapper
#
# @positive_output_decorator
# def subtract(a, b):
#     return a - b
#
# print(subtract(5, 7))
# print(subtract(3, 6))
# print(subtract(10, 2))





# Meta progrmamming -- data from one goes to another for processing



