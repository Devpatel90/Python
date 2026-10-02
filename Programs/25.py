"""
Task 25 Employee Payroll with Inheritance:- Create an Employee base class and Developer and Manager child classes. Use constructors, super(),
method overriding and polymorphism to calculate and display salary and bonus.

"""

try:
    class Employee:
        def __init__(self,name,id,salary):
            self.name = name
            self.id = id
            self.salary = salary
            
        def cal_sal(self):
            return self.salary
    
        def cal_bonus(self,b):
            return self.salary * b /100
                
        def display(self):
            print("Name:", self.name)
            print("ID:", self.id)
            print("Salary:", self.salary)
            print("Bonus:", self.cal_bonus(10))


    class Developer(Employee):
        def __init__(self,name,id,salary,lan):
            super().__init__(name,id,salary)
            self.lan = lan
            
        def cal_bonus(self, c):
            return self.salary * c / 100
        
        def display(self):
            print("--------------Developer----------------")
            print("Name:", self.name)
            print("ID:", self.id)
            print("Salary:", self.salary)
            print("Language:", self.lan)
            print("Bonus:", self.cal_bonus(15))


    class Manager(Employee):
        def __init__(self, name, id, salary, team):
            super().__init__(name, id, salary)
            self.team = team
            
        def cal_bonus(self,d):
            return self.salary * d / 100
        
        def display(self):
            print("------------------Manager--------------")
            print("Name:", self.name)
            print("ID:", self.id)
            print("Salary:", self.salary)
            print("Team M:", self.team)
            print("Bonus:", self.cal_bonus(20))
            
    employee = Employee("Dev", 101, 30000)
    # employee.cal_bonus(10)

    developer = Developer("Rahul", 102, 50000, "Python")
    # developer.cal_bonus(15)

    manager = Manager("Yash", 103, 80000, 10)
    # manager.cal_bonus(20)

    employees = [employee, developer, manager]

    for i in employees:
        i.display()
        
except Exception as e:
    print("Error", e)