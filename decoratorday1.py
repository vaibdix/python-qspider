# IMP QUESTION
# pramater dec
# delay decor
# exec decor





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








# 1.write a decorator function that prints "HELLO EVERYONE" message before execute any function
# def hello_decorator(func):
#     def wrapper():
#         print("HELLO EVERYONE")
#         func()
#     return wrapper
#
# @hello_decorator
# def my_function():
#     print("Function is executing...")
#
# my_function()






# 2.write a decorator function to print main function name before executing any decorator function

# def print_name(func):
#     def wrapper(*args):
#         print(f"Main function name: {func.__name__}")
#         return func(*args)
#     return wrapper
#
# @print_name
# def my_function():
#     print("Function is executing...")
#
# my_function()



# 3.write a decorator which inputs 5 seconds of delay before executing any decorator function
# import time
#
# def delay_decorator(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(5)
#         return func(*args, **kwargs)
#     return wrapper
#
# @delay_decorator
# def my_function():
#     print("Function is executing...")
#
# my_function()


# 4.write a decorator function calculate the execution time of any function
# import time

#
# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Execution time: {end - start} seconds")
#         return result
#     return wrapper
#
# @time_decorator
# def my_function():
#     time.sleep(2)
#
# my_function()






# 5.wadf to check if the 1st arguments is lesser than 2nd argument if then swap them and perform division
# but the condition is you should not modify the original function

# def divide_decorator(func):
#     def wrapper(*args, **kwargs):
#         if len(args) >= 2:
#             a, b = args[0], args[1]
#             if a < b:
#                 args = (b, a) + args[2:]
#         return func(*args, **kwargs)
#     return wrapper

# @divide_decorator
# def divide(a, b):
#     return a / b

# print(divide(2, 4))  # Output: 0.5
# print(divide(4, 2))  # Output: 2.0






# 6.wadf to add 2 numbers and display the message before "i am doing addition operation" after performing print the message "addition operation is done"
#
# o/p--->i am doing addition operation"
#        value
#      "addition operation is done


# def operation_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("I am doing addition operation")
#         result = func(*args, **kwargs)
#         print("Addition operation is done")
#         return result
#     return wrapper
#
# @operation_decorator
# def add_numbers(a, b):
#     return a + b
#
#
# num1 = 5
# num2 = 7
# result = add_numbers(num1, num2)
#
# print(result)







# 7.create a decorator to return only positive out from any subtraction
# def positive_subtraction(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return abs(result)
#     return wrapper
#
# @positive_subtraction
# def subtract(a, b):
#     return a - b
#
# print(subtract(10, 5))  # Output: 5
# print(subtract(5, 10))  # Output: 5







# 8.create a decorator which counts the number of function calls


# def count_calls(func):
#     def wrapper(*args, **kwargs):
#         wrapper.call_count += 1
#         print(f"Function {func.__name__} has been called {wrapper.call_count} times.")
#         return func(*args, **kwargs)
#     wrapper.call_count = 0
#     return wrapper
#
# @count_calls
# def my_function():
#     print("This is my function.")
#
# my_function()
# my_function()
# my_function()






# 9.wap to sum of the positional arguments and get the length of the keywords arguments
# def sum_and_count_args(*args, **kwargs):
#     positional_sum = sum(args)
#     keyword_count = len(kwargs)
#     return positional_sum, keyword_count
# result = sum_and_count_args(1, 2, 3, name="John", age=30)
# print(result)




# 10.write a decorator function to print the type of datatype before performing the action

# def print_types(func):
#     def wrapper(*args, **kwargs):
#         print("Argument types:")
#         for arg in args:
#             print(f"- {type(arg)}")
#         for key, value in kwargs.items():
#             print(f"- {key}: {type(value)}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @print_types
# def my_function(a, b, name="John", age=30):
#     print(f"a + b = {a + b}")
#     print(f"Name: {name}, Age: {age}")
#
# my_function(10, 20, name="Alice", age=25)





























# count no of times function got called
#######################################
# import time
# x = 0
# def outer(func):
#     def inner(*args, **kwargs):
#         global x
#         start = time.time()
#
#         func(*args, **kwargs)
#         print(f"{func.__name__} done")
#
#         end = time.time()
#         execution_time = end - start
#         print(execution_time)
#         x += 1
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
# add(3, 5)
# add(4, 5)
# add(5, 5)
# sub(2, 5)
# mul(2, 6)
# print(x)



