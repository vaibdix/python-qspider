def spam():
    print("spam")

spam()
print(spam)

display=spam
print(display)
spam()
display()


class Test:
    def __init__(self, x):
        self.x=x

    def get_data(self):
        print("taking data from source code")

    def f1(self):
        self.get_data()

    def f2(self):
        self.get_data()
y=Test(100)
y.get_data()
y.f1()
y.f2()

def new_get_data(self):
    print("data from test class")

# Here happends monkey patching
# modify data without touching original code
# below syntax is as follows:
#   classname.method = new_method
Test.get_data=new_get_data
y.f1()
y.f2()
