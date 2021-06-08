# Animal - name
# eat() - "{name} is eating"

# Dog - доп. атрибут breed, bark() - "Dog named {name} is barking"
# Cat - доп. атрибутов нет, meow() - "{name} says Meow"
# Frog - доп. атрибутов нет, eat() переопределен таким образом, чтобы "Frog with {name} is eating"
def main():
    class Animal:
        def __init__(self, name):
            self.name = name

        def eat(self):
            print(f"{self.name} is eating")

    class Dog(Animal):
        def __init__(self, name, breed):
            super().__init__(name)
            self.breed = breed

        def bark(self):
            print(f"Dog named {self.name} is barking")

    class Cat(Animal):
        def meow(self):
            print(f"{self.name} says Meow")

    class Frog(Animal):
        def eat(self):
            print(f"Frog with {self.name} is eating")

    charlie = Dog("Charlie", "German Shepherd")
    marquis = Cat("Marquis")
    princess = Frog("Princess")

    charlie.bark()
    print(charlie.breed)
    charlie.eat()
    marquis.meow()
    marquis.eat()
    princess.eat()


if __name__ == "__main__":
    main()
