"""
ABSTRACT CLASS
Cannot create objects directly - must make child classes
Forces children to implement specific methods
"""

from abc import ABC, abstractmethod  # Import abstract tools

class Vehicle(ABC):  # ABC = Abstract Base Class (cannot make Vehicle objects)
    # Marks as abstract - children MUST implement
    @abstractmethod  
    def go(self):
        pass  
    
    @abstractmethod 
    def stop(self):
        pass
    
    # Regular method (not abstract) - children inherit as-is
    def enter(self):
        print("You entered the car")


class Car(Vehicle):  
    # ✅ Must implement (required by Vehicle)
    def go(self):  
        print("We are going in the car")
    
    def stop(self):  
        print("We stopped the car")



car = Car()
car.enter()  # From Vehicle (inherited)
car.go()     # From Car (implemented)
car.stop()   # From Car (implemented)

# ❌ This would fail:
# vehicle = Vehicle()  # Cannot instantiate abstract class



'''

class Vehicle():

# Just a regular class
@abstractmethod is IGNORED - it's just a normal method
Can create Vehicle() objects even without implementing "abstract" methods

class Vehicle(ABC):

# True abstract class (inherits from ABC)
@abstractmethod is ENFORCED - makes method required
#Cannot create Vehicle() objects - only child classes

'''