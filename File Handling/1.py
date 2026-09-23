# file = open("data.txt", "r")
# a = file.read()
# print(a)
# file.close()

# -----------------------------------------------------------

# file = open("data.txt", "r")
# line = file.readline()
# print(line)
# file.close()

# Print: Hello Python

# --------------------------------------------------------------
# print them in list

# file = open("data.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close()

# print: ['Hello Python\n', 'I am learning Python\n', 'Python is powerful\n']

# ---------------------------------------------------------

file = open("data.txt", "w")
file.write("Hello Python.................")
file.close()