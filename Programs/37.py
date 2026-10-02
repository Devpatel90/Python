    # --------------------------Student Record Management System--------------------------
try:
    students = [
        {
            "name" : "raj",
            "roll_no" : 1,
            "marks" : [98,98,78,80,78]
        },
        {
            "name" : "ram",
            "roll_no" : 2,
            "marks" : [96,85,58,40,58]
        },
        {
            "name" : "rahul",
            "roll_no" : 3,
            "marks" : [34,45,58,70,85]
        }
    ]


    def add_stu():
            name = input("Enter Name:- ")
            if name == "":
                print("Please Enter Name it cannot be Empty")
                return

            try:
                roll_no  = int(input("Enter Roll No.:- "))
            except ValueError:
                print("Enter Number Only")
                return

            for stu in students:
                if stu["roll_no"] == roll_no:
                    print("Roll No Already Exists!1")
                    return
            try:
                marks = list(map(int, input("Enter Marks of 5 Subjects:- ").strip().split()))
            except ValueError:
                print("Enter Number Only")
                return
            
            if len(marks) != 5:
                print("Enter 5 Marks")
                return

            for mark in marks:
                if mark < 0 or mark > 100:
                    print("Marks b/w 0 to 100")
                    return
                
            students.append({
                "name" : name,
                "roll_no" : roll_no,
                "marks" : marks
            })
            print("Student Added Successfully")

    def cal_total(marks):
        return sum(marks)

    def cal_per(marks):
        total = sum(marks)
        percen = total / 5
        return percen

    def cal_grade(percentages):

        if percentages >= 90:
            return "A Grade"
        elif percentages >= 80 and percentages < 90:
            return "B Grade"
        elif percentages >= 70 and percentages < 80:
            return "C Grade"
        elif percentages >= 60 and percentages < 70:
            return "D Grade"
        elif percentages >= 50 and percentages < 60:
            return "E Grade"
        else:
            return "Fail"

    def cal_result(marks):
        for mark in marks:
            if mark < 50:
                return "Fail"
        return "Pass"

    def view():

        if students == 0:
            print("Empty")
            return

        for stu in students:
            totals = cal_total(stu["marks"])
            percentages = cal_per(stu["marks"])
            grades = cal_grade(percentages)
            results = cal_result(stu["marks"])

            print("--------Students--------")
            print("\nName: ", stu["name"])
            print("Roll_no: ", stu["roll_no"])
            print("Marks: ", stu["marks"])
            print("Total: ", totals)
            print("Percentage: ", percentages)
            print("Grade: ", grades)

    def search():
        nname = input("\nEnter Name:- ").strip().lower()

        a = False
        for stu in students: 
            if nname == stu["name"].lower():
                totals = cal_total(stu["marks"])
                percentages = cal_per(stu["marks"])
                grades = cal_grade(percentages)
                results = cal_result(stu["marks"])

                print("--------Student--------")
                print("\nName: ", stu["name"])
                print("Roll_no: ", stu["roll_no"])
                print("Marks: ", stu["marks"])
                print("Total: ", totals)
                print("Percentage: ", percentages)
                print("Grade: ", grades)
            a = True

        if not a:
            print("Student Not Found")

    def passed():
        a = False
        for stu in students:

            results = cal_result(stu["marks"])

            if results == "Pass":
                per = cal_per(stu["marks"])
            
                print("\nName:- ", stu["name"])
                print("Percentage:- ", per)
                print("Result:-", results)
        a = True

        if not a:
            print("Student Not Found")

    def statistics():

            if len(students) == 0:
                print("No students Found")
                return

            passed = 0
            fail = 0
            percentage = []

            for stu in students:
                per = cal_per(stu["marks"])
                percentage.append(per)

                if cal_result(stu["marks"]) == "Pass":
                    passed += 1
                else:
                    fail += 1

            minper = min(percentage)
            maxper = max(percentage)
            avg = sum(percentage) / len(percentage)

            print("-----Statistics-----")
            print("Minimum Percentage:- ", minper)
            print("Miximum Percentage:- ", maxper)
            print("Average Percentage:- ", avg)
            print("Passed Students:- ", passed)
            print("Fail Students:- ", fail)

    while True:  
        print("\n-----SMS-----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Students")
        print("4. Passed Students")
        print("5. Class Statistics")
        print("6. Exit")


        choice = input("Choose Number:- ")

        if choice == "1":
                add_stu()

        if choice == "2":
                view()

        if choice == "3":
                search()

        if choice == "4":
                passed()
        
        if choice == "5":
            statistics()

        if choice == "6":
            print("Exited Successfully")
            break

except Exception as e:
    print("Error", e)

finally:
    print("Thank You")