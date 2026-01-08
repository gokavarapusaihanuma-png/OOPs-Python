'''
"Duck typing" = Another way to achieve polymorphism besides Inheritance
        Object must have the minimum necessary attributes/methods
        "If it looks like a duck and quacks like a duck, it must be a duck."
'''

class Animal:
    is_alive=True
class Dog(Animal):
    def speak(self):
        print("Boow!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:  #  NOT an Animal (no inheritance)
    is_alive = False  # But has same attribute
    def speak(self):  # And has same method
        print("Vroom Vroom!")

# DUCK TYPING IN ACTION:
# List contains different types, but all have speak() and is_alive
animals = [Dog(), Cat(), Car()]

for obj in animals:  # Python doesn't check type, only checks methods
    obj.speak()      #  All have speak() method
    print(obj.is_alive)  #  All have is_alive attribute

'''
Python's mindset:
    "I don't care if you're a Dog, Cat, or Car...
    If you have a speak() method, you're good enough for me!"
'''
