import pandas as pd
import numpy as np

df = pd.read_csv("class4_SavingExporting/titanic.csv")

# Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare

# Creating a new column named test that has 2x the value in fare

df["test"] = df["Fare"] * 2

print(df.head())

# renaming a column in the dataframe
df1 = df.rename(
    columns={
        "Siblings/Spouses Aboard":"Sibling/Spouse",
        "Parents/Children Aboard":"Parent/Child"
    }
)
print(df1.info())

# saving as a new csv file

# df1.to_csv("modified_titanic")

# applying mathematical functions to entire data
# finding avg (mean) age

print(df["Age"].mean())

# prints seperatly
print(df[["Age","Fare"]].mean())

# group by command
# grouping a specific set of rows based on criteria
# grouping age and gender

# Groups (print does not show this grouping)
print(df[["Age","Sex"]].groupby("Sex").head())


# using .mean shows mean age per class  - showing the grouping has been done
df4 = df[["Pclass","Age"]].groupby("Pclass").mean()
print(df4)

# prints the average fare of 1st class female, then male then etc.. through Pclasses
print(df.groupby(["Pclass","Sex"])["Fare"].mean())

# finding count of passengers in each class
print(df["Pclass"].value_counts())

print(df[["Name","Age"]].sort_values("Age",ascending=False))

# changing to only lower cased names

df["newName"] = df["Name"].str.lower()
print(df["newName"])

print(df["Name"].str.split(" ")[:][1])
