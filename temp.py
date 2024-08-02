
class Doctors:
	def __init__(self):
		self.name = 'Doctor'
		self.den = self.Dentist()
		self.car = self.Cardiologist()

	def show(self):
		print('In outer class')
		print('Name:', self.name)


	class Dentist:
		def __init__(self):
			self.name = 'Dr. Savita'
			self.degree = 'BDS'

		def display(self):
			print("Name:", self.name)
			print("Degree:", self.degree)

	class Cardiologist:
		def __init__(self):
			self.name = 'Dr. Amit'
			self.degree = 'DM'

		def display(self):
			print("Name:", self.name)
			print("Degree:", self.degree)


# create a object
# of outer class
outer = Doctors()
outer.show()

# create a object
# of 1st inner class
d1 = outer.den

# create a object
# of 2nd inner class
d2 = outer.car
print()
d1.display()
print()
d2.display()


class Test:
    def A(self):
        print("A Class")
    class Sample:
        def B(self):
            print("B CLass")
        class Demo:
            def C(self):
                print("C Class")
x=Test()
y=x.Sample()
z=y.Demo()
x.A()
y.B()




###################
# Quesition perform nested class using nested constructor
# ###################
