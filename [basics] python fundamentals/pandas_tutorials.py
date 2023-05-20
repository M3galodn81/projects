import pandas as pd

# Dataframe = Table
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

# Series is Column
a = [1, 7, 2]

myvar = pd.Series(a)
print(myvar)

# Label is the Index
print(myvar[2])

# Create Labels
myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar["y"])

# Dictonary as a Series
# Keys Becomes Labels
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
print(myvar)

# Get only the some items, use their labels
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)