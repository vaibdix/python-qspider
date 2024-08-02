# composition(Has - a relationship)
# composition helps in usng inheritance style code wihtout using inheritace
# inheritance(is - a relationship)

# EG 1
class Test:
    name = "python"
    def spam(self):
        print("Spam Method")

# class Sample:
#     def demo(self):
#         print("demo method")
#         a = Test()
#         print(a.name)
#         a.spam()
#
# # EG 2
# class Car:
#     loc="pune"
#     def __init__(self):
#         print("car class")
#     def M1(self):
#         print("M1 Method")
#
# class Car2:
#     def __init__(self):
#         print("constructor class")
#         self.y=Car()
#         print(self.y.loc)
#         self.y.M1()
# x=Car2


class Qspider:
    def __init__(self, name, batch_code, room_number):
        self.name = name
        self.batch_code = batch_code
        self.room_number = room_number

    def Student_details(self):
        print(f'name is {self.name} is attaining {self.batch_code} from {self.room_number}')



class Pyspider:
    def __init__(self, subject, fee, student_count):
        self.subject = subject
        self.fee = fee
        self.student_count = student_count

        # Correct way to create a Qspider object and call methods
        self.qspider_instance = Qspider(name="Rahul", batch_code="M3", room_number="2")
        self.qspider_instance.student_details()

    def student(self):
        print(f"Pyspider student subject is {self.subject}, fee is {self.fee}, and student count is {self.student_count}")

# Example usage:
pyspider_obj = Pyspider(subject="Python Programming", fee=1000, student_count=20)
pyspider_obj.student()

