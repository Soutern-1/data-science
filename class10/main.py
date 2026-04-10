import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

# import plotly 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


name = ["age","work","fnlwgt","edu","edu.num","mar.stat","occ","family","race","sex","cgain","closs","hpw","origin","income"]

df = pd.read_csv("/Users/sutirthrajesh/Documents/vs/data science/datasets/adult.csv", names=name,header=None)
# or df.columns = name
# Plot

print(len(df))
print(df.info())

# Scatter plot of fnlwgt vs edunum

fnlwgt_scatter = px.scatter(
    x=df["edu.num"],
    y=df["fnlwgt"],
    title= "Education level vs Financial weight"
)

# fnlwgt_scatter.write_html("financialweightage.html",auto_open = True) 

# male/fm - education level, occupation, hpw -> income


df2 = df[df["sex"] == " Male"]
df2=df2[["sex","edu.num"]]
print(df2.head(20))

sexVedunum = px.histogram(
    x=df2["edu.num"]

)
sexVedunum.write_html("graph2.html",auto_open = True) 
