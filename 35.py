class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name:-",self.name)
        print("Age:-",self.age)
        
class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks = marks
        
    def displays(self):
        self.display()
        print("Marks:-",self.marks)
        
stu = Student("Dev",99,67)
stu.displays()