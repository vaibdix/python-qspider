# Constructor --> __init__()
# has two types -- predefined/default Constructor
#               -- Userdefined Constructor --- with parameter Constructor
#                                          --- without parameter Constructor

class Student:
    def __init__(self):
        print("day 1 class")
x = Student()

class Test:
    def __init__(self):
        print("hi")
    def spam(self):
        print("spam")
# Calling by object
t = Test()
t.spam()
# Calling by classname
Test.__init__(t)
Test.spam(t)

