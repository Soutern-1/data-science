import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

# import plotly 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Ask the user to input a country name.
# Filter the dataset for that country.
# Convert Date_reported to datetime.
# Plot:
# Line chart of Cumulative cases
# Line chart of Cumulative deaths

df = pd.read_csv("class8/WHO-COVID-19-global-data.csv")

chosen_country = str(input("What country would you like to search for?: "))

df["DateReported"] = pd.to_datetime(df["DateReported"])
# print(df["DateReported"], type(df["DateReported"]))

df_new = df[df["Country"] == chosen_country]
print(df_new)

if len(df_new) == 0:
    print("Enter a valid country")
else:
    chosen_country_cumu_cases = px.line(
        y=df_new['Cumulative_cases'],
        x=df_new["DateReported"]
    )
    chosen_country_cumu_cases.write_html("chosen_country_cumu_cases.html",auto_open = True)

