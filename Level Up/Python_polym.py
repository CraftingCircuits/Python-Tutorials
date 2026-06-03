# understanding Python polymorphism, polymorphism allows us to define methods in a child class that have the same name as methods in the parent class
# funtcion polymorphism, len() function, for A string first
x = "Hello Myra. How are you?"
print(len(x))
# for a list
y = [12, 23, 34, 45, 56]
print(len(y))
# for a tuple
z = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(z))
# for a set
a = {"one", "two", "three", "four", "five"}
print(len(a))
# for a dictionary
b = {"name": "Myra", "age": 21, "city": "New York"}
print(len(b))


# class polymorphism:
# polymorphism is often used in class methods,  where we can have multiple classes with the same methods name
# Class polymorphism
print("\n")


class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        print("Driving a car!")


class bike:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        print("Driving a bike!")


class bus:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        print("Driving a bus!")


car = car("Toyota", "Corollo", 2020)
bike = bike("Yamaha", "FZ", 2019)
bus = bus("Volvo", "B7R", 2020)

for x in (car, bike, bus):
    x.move()


# inheritance polymorphism, where we can have a parent class with a method and child classes that override that method
# Inheritance class polymorphism
print("\n")


class vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def move(self):
        print("Moving vehicle!")


class car(vehicle):
    def move(self):
        print("Driving a car!")


class bike(vehicle):
    def move(self):
        print("Driving a bike!")


class bus(vehicle):
    def move(self):
        print("Driving a bus!")


car = car("Thar", "T1", 2018)
bike = bike("Splender", "S1", 2020)
bus = bus("Luxury", "L1", 2021)

for x in (car, bike, bus):
    x.move()
