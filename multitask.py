# multitasking -- process based
#              -- thread based
# PVM creates main thread

import threading
# does thread take entire core of cpu
# parallelism vs concurrecy




# from threading import *

# print(threading.current_thread()) # gives thread data
# print(threading.current_thread().name) # gives thread name
# print(threading.current_thread().ident) # shows thread num
# threading.current_thread().setName("AASD")
# print(threading.current_thread().getName())
#
# # with depricated methods
# threading.currentThread().setName("py")
# print(threading.current_thread().getName())







import threading
import time
from threading import *

# class Mainclass(Thread):
#     def run(self):  # MANDATORY TO USE "RUN" AS FXN NM
#         for i in range(4):
#             print("python class", threading.current_thread())
# t = Mainclass()
# t.start()
# in mainclass obj first argu is target which points to fxn ie run


# for i in range(4):
#     print("webtechclass", threading.current_thread())



# without argu
# def without_run():  # MANDATORY TO USE "RUN" AS FXN NM
#     for i in range(4):
#         print("python class", threading.current_thread())
#
# t=Thread(target=without_run())
# t.start()


# with argu



# def spam(n, **kwargs):
#     for i in range(n):
#         print(threading.current_thread())
#         print(n, kwargs)
#
# # Correct usage of the kwargs parameter: use a dictionary
# t = Thread(target=spam, kwargs={'a': 1, 'g': 2}, args=(5,))
# t.start()



import time
from threading import Thread

def print_numbers():
    for i in range(5):
        print(i)

def print_letters():
    for letter in 'abcde':
        print(letter)

print("active thread count", active_count())

# Create thread instances
thread1 = Thread(target=print_numbers)
thread2 = Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print("is it Deamon",)

print("active thread count", active_count())
time.sleep(3)
print("active thread count", active_count())
print("Both threads have finished.")






# example 2

# def spam():
#     print(current_thread().name, "stat")
#     time.sleep(2)
#     print(current_thread().name, "ended")

# print("total active", active_count())

# a = Thread(target=spam, name="first")
# a1 = Thread(target=spam, name="second")

# a.start()
# a1.start()

# a.join()
# a1.join()

# print("active thread are", a.is_alive())
# print("active thread are", a1.is_alive())
#
# print("active thread are", active_count())
# time.sleep(3)
# print("count num is", active_count())

# print("active thread are", a.is_alive())
# print("active thread are", a1.is_alive())