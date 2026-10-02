"""
Task 23 Student Class and Constructor
Create a Student class with an __init__ constructor for name, roll number and marks. Add methods to
calculate the average, determine the grade and display the result.

"""

try:
    class Student:
        def __init__(self,name,rollno,marks):
            self.name = name
            self.rollno = rollno
            self.marks = marks
            
        def avg(self):
            avg = sum(self.marks) / len(self.marks)
            print("Average is:- ", avg)
        
        def grade(self):
            avg = sum(self.marks) / len(self.marks)
            if avg >=90 and avg <= 100:
                print("Grade:- A")
            elif avg >=80 and avg < 90:
                print("Grade:- B")
            elif avg >=70 and avg < 80:
                print("Grade:- C")
            elif avg >=60 and avg < 70:
                print("Grade:- D")
            else:
                print("Fail!!")
            
        def display(self):
            print("Name:-", self.name)
            print("Roll Number:-", self.rollno)
            print("Marks:-", self.marks)
            self.avg()
            self.grade()
            
    student1 = Student("Raj", 101, [80, 40, 75])

    student1.display()
    
except Exception as e:
    print("Error", e)