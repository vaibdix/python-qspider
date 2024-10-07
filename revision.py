class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        print(f"Starting {self.engine_type} engine.")

class Tire:
    def __init__(self, size):
        self.size = size

    def inflate(self):
        print(f"Inflating {self.size} tires.")

class Car:
    def __init__(self, make, model, engine, tires):
        self.make = make
        self.model = model
        self.engine = engine
        self.tires = tires

    def start(self):
        self.engine.start()
        self.tires.inflate()
        print(f"The {self.make} {self.model} is ready to go!")

engine = Engine("V6")
tires = Tire("18-inch")
my_car = Car("Toyota", "Camry", engine, tires)
my_car.start()