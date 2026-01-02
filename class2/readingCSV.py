import pandas as pd
import numpy as np

# loading the csv

df = pd.read_csv("class2-pandas/titanic.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.dtypes)

# filtering out rows - e.g all passengers above 35 y.o

dfAge = df[df["Age"] > 35]

print(dfAge["Age"])
print(dfAge.shape)

# filtering out only people in 2nd and 3rd class
dfClass = df[df["Pclass"].isin([2,3])]
print(dfClass)
print(dfClass.shape)

dfClass = df[df["Pclass"].isin([1])]
print(dfClass)
print(dfClass.shape)

