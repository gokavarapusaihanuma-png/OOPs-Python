# Class variable: shared by all objects of the class
# Defined outside the constructor

class Student:
    year = 2025   # class variable
    num_of_students=0
    def __init__(self, name, grade):
        self.name = name      
        self.grade = grade    
        Student.num_of_students+=1  #accesing the class variable in constructor

# Creating objects
student1 = Student("Hanuma", "S")
student2 = Student("Venkatesh", "A")

# Accessing instance variables
print(f"{student1.name}'s grade is {student1.grade}")
print(f"{student2.name}'s grade is {student2.grade}")

# Accessing class variable
print(f"{student1.name} passed out in year {student1.year}")   # using object
print(f"{student2.name} passed out in year {Student.year}")    # preferred way

print(f"Total no.of students in the year {Student.year} is {Student.num_of_students}")
