# understanding inheritance in Python
# Inheritance in Python allows a class (called a child or derived class)
# to inherit attributes and methods from another class (called a parent or base class).
# syntax :
# class parent:
#     def parent_method(self):
#         print("This is a method from the parent class.")
# class child(parent):
#     def child_method(self):
#         print("This is a method from the child class.")


class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic animal sound"


class dog(animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof Woof"


class cat(animal):
    def __init__(self, name, breed):
        super().__init__(name, "Cat")
        self.breed = breed

    def make_sound(self):
        return "meow meow "


d = dog("Buddy", "Golden Retriever")
c = cat("Whiskers", "siamese")
print(f"{d.name} is a {d.species} of breed {d.breed} and says {d.make_sound()}")
print(f"{c.name} is a {c.species} of breed {c.breed} and says {c.make_sound()}")
