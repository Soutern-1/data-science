import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import plotly 
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv("class6_datapreprocessing/covid_data.csv")


# selecting required columns, skipping unnesecary

df = df[['Province_State',"Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]
df = df.rename(
    columns={
        "Province_State":"State",
        "Country_Region":"Country",
        "Last_Update":"Updated"        
    }
)

print(df.head())
print(df.dtypes,df.shape,df.describe())

print(df.info(),df.shape)

# handling missing values
df["State"].fillna(value="",inplace=True)
df["Lat"].fillna(value="",inplace=True)
df["Long_"].fillna(value="",inplace=True)

print(df.info(),df.shape)
print(df["State"])


top_10_confirmed_countries = df.groupby("Country")["Confirmed"].sum().nlargest(10).sort_values(ascending=True)
print(top_10_confirmed_countries.head(10))

figure = px.scatter(top_10_confirmed_countries,
                    x=top_10_confirmed_countries.index,
                    y="Confirmed",
                    title="Countries with highest confirmed Covid cases",
                    size="Confirmed",
                    color=top_10_confirmed_countries.index,
                    size_max=100
                
)

figure.write_html("confirmed_covid_countries.html",auto_open = True)

# ------------------------------------------------------------------

highest_death = df.groupby("Country")["Deaths"].sum().nlargest(10).sort_values(ascending=False)

figure = px.bar(highest_death,
                y=highest_death.index,
                x="Deaths",
                title="Countries with highest death count due to Covid",
                color = "Deaths",
                orientation="h",
                color_continuous_scale=["Grey","Red"]
                )


figure.write_html("highest_death_count.html",auto_open=True)

# ------------------------------------------------------------------

# Group data by country
country_data = df.groupby("Country")[["Recovered"]].sum()

# Get top 10 countries by total recovered cases
top_10_recovered = country_data["Recovered"].nlargest(10).sort_values(ascending=True)

print(top_10_recovered)

# Create bar chart
figure = px.bar(
    top_10_recovered,
    y=top_10_recovered.index,
    x="Recovered",
    title="Top 10 Countries with Highest Total Recoveries",
    orientation="h",
    color="Recovered",
    color_continuous_scale=["LightGreen", "Green"]
)

figure.write_html("highest_total_recoveries.html", auto_open=True)
