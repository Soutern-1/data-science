import pandas as pd
import numpy

# Dataframe
# Creating a dataframe from a dict

df = pd.DataFrame(
    {"Name":["a","b","c","d"],
      "Age":[14,13,15,16],
      "Grade":[8,7,9,10],
      "Score":[51,60,70,80]}
      )

print("print as table")
print(df)


print("print first 2 and last 2 rows")

print(df.head(2))
print(df.tail(2))

print("************************")
print("Information about it (not data)")
print(df.info())

# number of rows and columns
print(df.shape)

print("\nPrinting statistics of it")
print(df.describe())

print("\n Printing specific columns")
print(df["Age"])

print("\n printing 2 columns")
print(df[["Name","Score"]])

# finding highest value in a column (filtering) and printing it

print(df["Score"].max())
print(df["Score"].min())

print("************************")

NameAndAges = df[["Score","Age"]]
print(NameAndAges)
