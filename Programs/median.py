# numbers = [10,20,30,40,50]

# numbers.sort()

# middle = len(numbers) // 2

# median = numbers[middle]

# print(median)

# ------------------------------------------------------

number = [10,20,30,40]

n = len(number)

middle = n // 2

median = (number[middle - 1] + number[middle]) // 2

print(median)