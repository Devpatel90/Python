import pandas as pd

data = {
    "Name" : ["Raj","Het","Tirth","Malay"],
    "Age" : [21, 22, 25, 22],
    "Marks" : [85, 95, 78, 99]
}

df = pd.DataFrame(data)

print(df)