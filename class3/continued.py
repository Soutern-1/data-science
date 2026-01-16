import pandas as pd
import numpy as np

# loading the csv

df = pd.read_csv("class2-pandas/titanic.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.dtypes)
print(df.describe())

# filtering out rows - e.g all passengers above 35 y.o

dfAge = df[df["Age"] > 35]

print("*****************************")
# print(dfAge["Age"])
print(dfAge.shape)

# filtering out only people in 2nd and 3rd class
# dfClass = df[df["Pclass"].isin([2,3])]

# OR

dfClass=df[(df["Pclass"] == 2) | (df["Pclass"] == 3)]

print(dfClass)


# print(dfClass)
# print(dfClass.shape)

# dfClass = df[df["Pclass"].isin([1])]
# print(dfClass)
# print(dfClass.shape)

dfClassAge = df[["Pclass","Name"]]
# print(dfClassAge)
# print(dfClassAge.dtypes)

dfCA = df[(df["Pclass"] ==1) & (df["Age"] > 35)]
dfCA2 = dfCA[["Pclass","Age"]]
print(dfCA2)

dfFC = df[(df["Sex"] == "female") & (df["Pclass"] == 2)]

print(dfFC[["Name","Sex","Fare","Pclass"]])
print(dfFC["Fare"].max())

# avg fare of all male passengers in 1st class,older than 20
dfMFCA = df[(df["Age"] > 20) &( df["Sex"] == "male") & (df["Pclass"] == 1)]
print(dfMFCA)
print("*******",dfMFCA["Fare"].mean(),"********")
