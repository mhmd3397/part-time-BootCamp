'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
This module is for assignment Users with Zoo in Coding Dojo
Mohammed Eleyan
19-05-2023
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


# Imagine a game where you can create a zoo and start raising different types of animals.
# Say that for each zoo you create can have several different animals.
# Start by creating an Animal class,
# and then at least 3 specific animal classes that inherit from Animal. (Maybe lions and tigers and bears, oh my!)
# Each animal should at least have a name, an age, a health level, and happiness level.
# The Animal class should have a display_info method that shows the animal's name, health, and happiness.
# It should also have a feed method that increases health and happiness by 10.
# In at least one of the Animal child classes you've created, add at least one unique attribute.
# Give each animal different default levels of health and happiness.
# The animals should also respond to the feed method with varying levels of changes to health and happiness.


class Animal:
    def __init__(self, name, age, health_level=50, happiness_level=50):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def display_info(self):
        print(f"I'm {self.name} my age is {self.age} my health level is {self.health_level} and my happiness level is {self.happiness_level}")

    def feed(self):
        self.health_level += 10
        self.happiness_level += 10
        return self


class Lion(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, health_level=50, happiness_level=50)
        self.color = color


class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health_level=40, happiness_level=40)


class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health_level=30, happiness_level=30)


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name, age, color):
        self.animals.append(Lion(name, age, color))

    def add_tiger(self, name, age):
        self.animals.append(Tiger(name, age))

    def add_beer(self, name, age):
        self.animals.append(Bear(name, age))

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 25, "brown")
zoo1.add_lion("Simba", 22, "white")
zoo1.add_tiger("Rajah", 13)
zoo1.add_tiger("Shere Khan", 11)
zoo1.add_beer("panda", 13)
zoo1.add_beer("panda1", 11)
zoo1.print_all_info()
