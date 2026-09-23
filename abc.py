# n = int(input("Enter Number:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*", end="")

#     print()        
    
    
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()
    
    
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()
    
    
# for i in range(n,0,-1):
#         for j in range(n-i):
#             print(" ", end="")
#         for j in range(2 * i - 1):
#             print("*", end="")
#         print()

# fruits = ["apple", "banana", "mango", "orange"]
    
# fruits.append("Rahul")
# fruits.remove("apple")

# for fruit in fruits:
#     print(fruit)

# numbers = [10, 20, 30, 40, 50]

# numbers[2] = 100
# print(numbers)


# student = ("Dev", 22, "IT", 85)

# for stu in student:
#     print(stu)
    
# print(student[0])
# print(student[3])


# numbers = {10, 20, 10, 30, 20, 40}
# numbers.add(50)
# numbers.remove(20)
# for number in numbers:
#     print(number) 


# skills = {"Python", "Java", "C++", "JavaScript"}

# skill = input("Enter Skill:- ")

# if skill in skills:
#     print("Exists")
# else:
#     print("Errorrr")


# student = {
#     "name": "Dev",
#     "age": 22,
#     "marks": 85
# }

# print(student["name"])
# student["marks"] = 90
# student["city"] = "Ahmedabad"
# del student["age"]
# print(student)



# fact = 1
# for i in range(1, n + 1):
#     fact *= i

# print(fact)

# a = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         a += 1 

# if a == 2:
#     print("prime")
# else:
#     print("not prime")
    
# a = 0
# b = 1
# for i in range(1,n+1):
#     print(a, end="")
#     c= a+b
#     a = b
#     b = c

# stri = input("Enter Str:- ")

# rev = stri[::-1]

# if stri == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
    
    
# for i in range(n+1):
#     for j in range(n):
#         print("*", end=" ")
    
#     print()

# for i in range(n+1):
#     for j in range(i):
#         print("*", end=" ")
        
#     print()


# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
        
#     print()



# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print() 
    
    
    
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print() 

# for i in range(n, 0, -1):
#     for j in range(1,i+1):
#         print(j, end=" ")
    # print() 
    
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()
    

# for i in range(n, 0, -1):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()


# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()


# a = int("20", 4)
# print(a)              (2 * 4 + 0)


# word = "India"
# print(word[-4:-1])


# lis = ["learning","abc","rapp"]

# largest = lis[0]

# for num in lis:
#     if len(num) > len(largest):
#         largest = num       
        
# print(largest)


# numbers = [10,40,35,45,56,78976,435,34] 

# largest = numbers[0]

# for num in numbers:
#       if num > largest:
#         largest = num 
    
# print(largest)       


# numbers = [10,20,10,20,30,40,50,50,40,30,50]

# largest = float("-inf")
# sec_largest = float("-inf")

# for num in numbers:
#     if num > largest:
#         sec_largest = largest
#         largest = num
    
#     elif  num > sec_largest and num != largest:
#         sec_largest = num
        
# print("Largest", largest)
# print("Second Largest", sec_largest)



# numbers = [1,3,4,0,7,6,0,7,9,0,0,7,8,0,1,3,1,0,32,0,44]

# res = []
# count = 0

# for num in numbers:
#     if num == 0:
#         count += 1
        
#     else:
#         res.append(num)
        
# for i in range(count):
#     res.append(0)
    
# print(res)


# numbers = [1,3,4,0,7,6,67,78,97,100]

# rev = []
# for i in range(len(numbers) - 1, -1, -1):
#     rev.append(numbers[i])
    
# print(rev)

a = int("2", 4)
print(a)     