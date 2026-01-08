'''
COMPOSITION = "Owns-a" relationship
Parts cannot exist independently of the whole
Whole creates and destroys its parts
'''

# Parts (Engine, Wheels) - created INSIDE Car
class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheels:
    def __init__(self, size):
        self.size = size

# Whole (Car) - CREATES its parts
class Car:
    def __init__(self, model, horse_power, size):
        self.model = model
        # COMPOSITION: Car CREATES its Engine
        self.engine = Engine(horse_power)  # Engine born with Car
        
        # COMPOSITION: Car CREATES its Wheels  
        self.wheels = [Wheels(size) for _ in range(4)]  # Wheels born with Car

# When Car is created, parts are created too
car1 = Car("Ford", 50, 8)
car2 = Car("BMW", 69, 10)

# Parts belong ONLY to this car
print(f"{car1.model}: Engine {car1.engine.horse_power}hp")
print(f"{car2.model}: Engine {car2.engine.horse_power}hp")

#  Engine can't exist without Car
# engine = Engine(50)  # Possible but not the relationship's intent

'''
Same code with aggregation:

AGGREGATION = "Has-a" relationship  
Parts exist independently


class Engine:
    def __init__(self, hp):
        self.hp = hp

class Car:
    def __init__(self, model, engine):  # Takes EXISTING Engine
        self.model = model
        self.engine = engine  #  AGGREGATION: Uses existing Engine

# Engine exists first (independent)
engine1 = Engine(150)
engine2 = Engine(200)

# Cars use existing engines
car1 = Car("Ford", engine1)  # Same engine could be in multiple cars
car2 = Car("BMW", engine2)

# Engine still exists even if car is destroyed
'''