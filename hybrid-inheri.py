# class GrandPa:
#     def __init__(self):
#         print("Grand Pa")
#
# class Father(GrandPa):
#     def __init__(self):
#         print('f', super())
#         super().__init__()
#         print("Father")
#
# class Mother(GrandPa):
#     def __init__(self):
#         print('m', super())
#         super().__init__()
#         print("Mother")
#
#
# class child(Father, Mother):
#     def __init__(self):
#         print('c', super())
#         super().__init__()
#         print("Child")
#
# c = child()







# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
class Flyable:
    def __init__(self, name):
        self.name = name
    
    def fly(self):
        pass

class Bird(Animal, Flyable):
    def speak(self):
        return f"{self.name} says Chirp!"

    def fly(self):
        return f"{self.name} flies in the sky!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Robin")

print(dog.speak()) 
print(cat.speak())  
print(bird.speak()) 
print(bird.fly())  
