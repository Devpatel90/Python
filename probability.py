# import random

# coin = random.choice(["Heads", "Tails"])

# print(coin)

# ----------------------------------------------------

# import random

# dice = random.randint(1,6)

# print(dice)

# ----------------------------------------------------

import random

heads = 0
tails = 0

for i in range(1000):
    data = random.choice(["Heads", "Tails"])

    if data == "Heads":
        heads += 1
    else:
        tails += 1
        
print("Heads", heads)
print("Tails", tails)