# @property -- used as getter method
#           -- same method name need for getter when using @property
# @property.setter -- used as setter method
# @property,deleter -- used as deleter method

# protected used when we want multiple values
# for single val we can use public
# while callling check notes

class Student:
    def __init__(self, loc, product, price):
        self._loc = loc
        self._product = product
        self._price = price

    @property
    def location(self):
        """Getter method for location, product, and price."""
        print("Getting value")
        return self._loc, self._product, self._price

    @location.setter
    def location(self, values):  # here we are taking values as single value argument
        """Setter method for location, product, and price."""
        if len(values) != 3:
            raise ValueError("Expected a tuple with three values: (location, product, price)")
        print("Setting value")
        self._loc, self._product, self._price = values

    @location.deleter
    def location(self):
        """Deleter method for location, product, and price."""
        print("Deleting values")
        del self._loc
        del self._product
        del self._price

# Example usage
student = Student("pune", "laptop", 30000)
# here variables acts like a property

print(student.location)  # Output: Getting value \n ('pune', 'laptop', 30000)

student.location = ("mumbai", "mobile", 25000)  # Output: Setting value

print(student.location)  # Output: Getting value \n ('mumbai', 'mobile', 25000)

del student.location  # Output: Deleting values

