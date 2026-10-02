numbers = [2,4,6]

mean = sum(numbers) / len(numbers)

a = []

for x in numbers:
    diff = x - mean
    power = diff ** 2
    a.append(power)
    
variance = sum(a) / len(numbers)

print(round(variance, 2))