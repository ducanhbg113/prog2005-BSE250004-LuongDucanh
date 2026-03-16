class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("sua")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("gau")
dog = Dog("gg")
print(dog.name)