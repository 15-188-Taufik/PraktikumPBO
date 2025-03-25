from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    def __init__(self, name, age):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer.")
        self.__name = name
        self.__age = age

    @abstractmethod
    def make_sound(self):
        pass

    def get_info(self):
        return f"Name: {self.__name}, Age: {self.__age}"

# Derived classes
class Duck(Animal):
    def make_sound(self):
        return "Quack!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Lion(Animal):
    def make_sound(self):
        return "Roar!"

class Bird(Animal):
    def make_sound(self):
        return "cuuit!"

# Zoo Management System
class ZooManagementSystem:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Only objects of type Animal can be added.")
        self.animals.append(animal)

    def show_all_animals(self):
        if not self.animals:
            print("No animals in the zoo.")
        else:
            for animal in self.animals:
                print(animal.get_info())

    def make_all_sounds(self):
        if not self.animals:
            print("No animals to make sounds.")
        else:
            for animal in self.animals:
                print(f"{animal.get_info()} makes sound: {animal.make_sound()}")

# Main program
if __name__ == "__main__":
    zoo = ZooManagementSystem()

    try:
        duck = Duck("Donald", 3)
        cat = Cat("Whiskers", 2)
        lion = Lion("Simba", 5)
        bird = Bird("Tweety", 1)

        zoo.add_animal(duck)
        zoo.add_animal(cat)
        zoo.add_animal(lion)
        zoo.add_animal(bird)

        print("All animals in the zoo:")
        zoo.show_all_animals()

        print("\nAnimal sounds:")
        zoo.make_all_sounds()

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")