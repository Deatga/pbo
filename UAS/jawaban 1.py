#Jelaskan menurut anda apa itu inheritance/kelas turunan dan buatlah contoh codingannya serta capture hasilnya

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

dog = Dog("Fido")
print(dog.speak())  # "Woof woof"

cat = Cat("Whiskers")
print(cat.speak())  # "Meow"
