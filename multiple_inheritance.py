"""
MULTIPLE INHERITANCE IN PYTHON
A class can inherit from more than one parent class
Syntax: class ChildClass(Parent1, Parent2, ...)
"""

# PARENT CLASS 1: Pray animals (those that run from predators)
class Pray:
    def flee(self):
        print("This animal is fleeing from predators")


# PARENT CLASS 2: Predator animals (those that hunt prey)
class Predator:
    def hunt(self):
        print("This animal is hunting for prey")



# Rabbits can only flee (they are prey, not predators)
class Rabbit(Pray):
    pass 

# Hawks can only hunt (they are predators, not prey)
class Hawk(Predator):
    pass  


# Some fish can both hunt and be hunted (like sharks)
class Fish(Pray, Predator):
    pass  



print("RABBIT BEHAVIOR (Pray only):")

rabbit = Rabbit()
rabbit.flee()  
# rabbit.hunt()  # Would cause ERROR: Rabbits don't have hunt() method


print("HAWK BEHAVIOR (Predator only):")

hawk = Hawk()
# hawk.flee()   # Would cause ERROR: Hawks don't have flee() method
hawk.hunt()    


print("FISH BEHAVIOR (Both Pray AND Predator):")
#This is the multiple inheritance
fish = Fish()
fish.hunt()  
fish.flee() 




