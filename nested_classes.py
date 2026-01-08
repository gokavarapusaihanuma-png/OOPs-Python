'''
Nested class = A class defined within another class

class Outer:
    class Inner:

Benefits: Allows you to logically group classes that are closely related  
Encapsulates private details that aren't relevant outside of the outer class  
Keeps the namespace clean; reduces the possibility of naming conflicts
'''

class Company:
    class Employee:
        def __init__(self,name,position):
            self.name=name
            self.position=position
        def get_details(self):
            return f"{self.name}'s positon is {self.position}"

    def __init__(self,comp_name):
        self.comp_name=comp_name
        self.list_of_emp=[]
    
    def add(self,name,position):
        new_emp=self.Employee(name,position)
        self.list_of_emp.append(new_emp)
    
    def show(self):
        return [emp.get_details() for emp in self.list_of_emp]

company=Company("SHV")
company.add("Hanuma","ceo")
company.add("Sai","chairman")
company.add("Venkatesh","founder")
print(company.show())
    

'''
Cannot access directly from outside
employee = Employee("Name", "Job")  -> ERROR

Must access through outer class
employee = company.Employee("Test", "Intern") ->  Works
'''