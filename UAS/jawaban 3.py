#Jelaskan menurut anda apa itu polymorphism dan buatlah contoh codingannya serta capture hasilnya

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

def animal_speak(animal):
    print(animal.speak())

dog = Dog("Fido")
cat = Cat("Whiskers")

animal_speak(dog)  # "Woof woof"
animal_speak(cat)  # "Meow"
