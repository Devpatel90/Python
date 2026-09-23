class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def displaye(self):
        print("Name:-",self.name)
        print("Salary:-",self.salary)
        
class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def displayd(self):
        self.displaye()
        print("Language:-",self.language)
        
dev = Developer("Raj",15000,"Python")
dev.displayd()