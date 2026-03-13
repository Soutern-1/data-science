
import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

# import plotly 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("class8/WHO-COVID-19-global-data.csv")

# df.describe()
# df.info()
# print(df.shape)

df.fillna(value="",inplace=True)


# total global confirmed cases

global_confirmed1 = df[["DateReported","Cumulative_cases"]].groupby("DateReported")
global_confirmed = global_confirmed1.sum()
print(global_confirmed.head(20))

bar_global_cases = px.bar(
    x=df["DateReported"],
    y=df["Cumulative_cases"],
    title="Global confirmed cases over time"
)

bar_global_cases.write_html("global_cases.html",auto_open = True)

# top 10 confirmed cases by countries

country_cases = df[["Country","Cumulative_cases"]].groupby("Country")
country_cases = country_cases.sum()
country_cases = country_cases.sort_values("Cumulative_cases",ascending=False)
# print(country_cases.head())

country_cases_bar = px.bar(
    x=df["Country"].head(10),
    y=df["Cumulative_cases"].head(10),
    title="Countries with highest total cases"
)

country_cases_bar.write_html("global_countries.html",auto_open = True)
