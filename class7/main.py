# Create a 3-plot horizontal dashboard:
# Histogram: Alcohol content (colored by quality)
# Scatter: Alcohol vs Density (size = sulphates, color = quality)
# Scatter: Density vs 
# Add:
# Shared theme
# Dashboard title

import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

# import plotly 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("class7/winequality-red.csv")

# data preprocessing
# print(df.info())
# print(df.shape)

print(df[df.isin(["?"," ","/","-"]).any(axis=1)])

print(df.describe())

figure = px.histogram(
    df,     
    x=df["alcohol"],
    color = df["quality"],
    title = "Quality of wines"
)

figure.write_html("quality.html",auto_open = True)

figure = px.scatter(
    df,
    x=df["alcohol"],
    y= df["density"],
    color = df["quality"],
    title="Density vs Alcohol content, colored by quantity"
)

figure.write_html("density.html",auto_open = True)

df1 = df[["alcohol","quality"]].groupby("alcohol")

figure = px.scatter(
    df,
    y=
)
