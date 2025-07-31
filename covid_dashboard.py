import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
df = pd.read_csv("covid_data.csv")

# Static Time Series Plot
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Confirmed"], label="Confirmed", marker='o')
plt.plot(df["Date"], df["Recovered"], label="Recovered", marker='s')
plt.plot(df["Date"], df["Deaths"], label="Deaths", marker='^')
plt.title("COVID-19 Time Series")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("covid_timeseries.png")
plt.show()

# Pie Chart (Latest Stats)
latest = df.iloc[-1]
pie_df = pd.DataFrame({
    "Category": ["Confirmed", "Recovered", "Deaths"],
    "Count": [latest["Confirmed"], latest["Recovered"], latest["Deaths"]]
})
fig = px.pie(pie_df, names="Category", values="Count", title="Latest COVID-19 Status")
fig.show()
