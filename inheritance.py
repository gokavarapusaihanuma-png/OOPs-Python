"""
INHERITANCE IN PYTHON
Allows a class to inherit attributes and methods from another class
Promotes code reusability and extensibility
Syntax: class ChildClass(ParentClass):
"""

# BASE CLASS (Parent Class)
class Animal:
    # Constructor - runs when creating a new Animal object
    def __init__(self, name, breed):
        # Instance attributes - each Animal object will have these
        self.name = name      
        self.breed = breed    
        self.is_alive = True  # Default value for all animals
        
    # Instance methods
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")


# CHILD CLASSES inherits everything from Animal

class Dog(Animal):
    # 'pass' means Dog has no additional methods/attributes
    # It automatically gets all Animal's methods: __init__, eat(), sleep()
    pass

class Cat(Animal):
    # Cat has everything from Animal PLUS this new method
    def sounds(self):
        return "Meow!"


# CREATING OBJECTS (Instances)

cat = Cat("Doremon", "electric raccoon")  
dog = Dog("Dhruv Rathee", "German Shepherd")  

# All attributes come from Animal class via inheritance
print(f"{cat.name}'s breed is {cat.breed} and it says {cat.sounds()}")
print(f"{dog.name}'s breed is {dog.breed}")

# You can also use inherited methods:
cat.eat()    
dog.sleep()  

# Check default attribute from Animal class:
print(f"Is the cat alive? {cat.is_alive}")  
print(f"Is the dog alive? {dog.is_alive}")  