"""
Task 22 List Statistics:- Accept comma-separated numbers and display the minimum, maximum, average and second-largest unique value. Handle invalid input.
"""

try:
    nums = input("Enter comma-separated Numbers:- ")

    num = nums.split(",")

    numl = []
    for i in num:
        numl.append(int(i))
        
    minn = min(numl)
    maxn = max(numl)
    average = sum(numl) / len(numl)

    unique = set(numl)
    unique = sorted(set(numl))
    seclar = unique[-2]

    print("Minimum is-", minn)
    print("Maximum is-", maxn)
    print("Average is-", average)
    print("Second Largest is:-", seclar)

except Exception as e:
    print("Error", e)