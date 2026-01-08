"""
MULTILEVEL INHERITANCE
A class inherits from a parent that itself inherits from another parent
C(B) <- B(A) <- A
"""

# LEVEL 1: Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

# LEVEL 2: Child of Animal (inherits eat, sleep)
class Pray(Animal):  
    def flee(self):
        print(f"{self.name} is fleeing")

# LEVEL 2: Child of Animal (inherits eat, sleep)
class Predator(Animal):  
    def hunt(self):
        print(f"{self.name} is hunting")

# LEVEL 3: Child of Pray (inherits flee + eat/sleep from Animal)
class Rabbit(Pray):  # Gets: flee() from Pray, eat/sleep from Animal
    pass

# LEVEL 3: Child of Predator (inherits hunt + eat/sleep from Animal)
class Hawk(Predator):  # Gets: hunt() from Predator, eat/sleep from Animal
    pass

# MULTIPLE INHERITANCE: Child of BOTH Pray AND Predator
class Fish(Pray, Predator):  # Gets: flee() + hunt() + eat/sleep from Animal
    pass

# Test the inheritance chain
rabbit = Rabbit("Chikoo")
print("Rabbit (Animal → Pray → Rabbit):")
rabbit.flee()   # From Pray
rabbit.eat()    # From Animal via Pray
rabbit.sleep()  # From Animal via Pray

hawk = Hawk("Bunty")
print("\nHawk (Animal → Predator → Hawk):")
hawk.hunt()     # From Predator
hawk.eat()      # From Animal via Predator
hawk.sleep()    # From Animal via Predator

fish = Fish("Nemo")
print("\nFish (Animal → Pray + Predator → Fish):")
fish.hunt()     # From Predator
fish.flee()     # From Pray  
fish.eat()      # From Animal via Pray/Predator
fish.sleep()    # From Animal via Pray/Predator