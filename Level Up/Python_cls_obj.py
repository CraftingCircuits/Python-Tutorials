# Python is a object oriented programming language, it allows us to create classes and objects.
# class is a blueprint for creating objects, and an object is an instance of a class.


class person:
    def __init__(
        self, name, age
    ):  # __ini__() is a constructor, it is called when an object id created. and there is also two underscores.
        self.name = name
        self.age = age


p1 = person("John", 21)
print(p1.name)


# str function is used to return a string representation of an object.
class person:
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."


p1 = person("John", 21)
print(p1)


# object can also contain methods, which are functions that belong to the object.
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFun(self):
        print(f"{self.name} is {self.age} years old.")


p1 = person("John", 21)
p1.myFun()
# Now modifying object's properties
p1.age = 22
p1.myFun()
# Now deleting object's properties
del p1.age


# p1.myFun() this will raise an error because age property is deleted
# let's try with more parameters in the constructor, also with diff names and values
class person:
    def __init__(self, fav_col, fav_food, fav_num, fav_game, fav_brand, fav_movie):
        self.fav_col = fav_col
        self.fav_food = fav_food
        self.fav_num = fav_num
        self.fav_game = fav_game
        self.fav_brand = fav_brand
        self.fav_movie = fav_movie

    def myFun(self):
        print(f"Favourite color is {self.fav_col}, Favourite food is {self.fav_food}")


favourites = person("Blue", "Pizza", 7, "Cricket", "Nike", "Lootera")
favourites.myFun()
# according to chatGpt, here self is a must to write in the constructor, it is a refrence to the current instance of the class.
# from deleting object's properties to deleting the object itself
del favourites


# now, favourites object will make an error if we try to access it
# if we have nothing for class's content, then we can pass a pass statement
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFun(self):
        pass
