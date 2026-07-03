"""
01-first-chart: Basic real-world data pull and visualization.
Pulls country population data via REST API, aggregates by region, and saves a bar chart.
Early experiment in using Python (requests + pandas + matplotlib) for data exploration.
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt

# Pull real country data from the REST Countries API
url = "https://restcountries.com/v3.1/all?fields=name,population,region"
response = requests.get(url)
print(f"API status code: {response.status_code}")

data = response.json()

# Load into a pandas DataFrame
df = pd.DataFrame([
    {
        "Country": item["name"]["common"],
        "Population": item["population"],
        "Region": item["region"]
    }
    for item in data
])

# Group by region and sum population
region_pop = df.groupby("Region")["Population"].sum().sort_values(ascending=True)

# Print the data
print("\nWorld Population by Region:")
for region, pop in region_pop.items():
    print(f"  {region}: {pop:,.0f}")

# Make a chart
plt.figure(figsize=(10, 6))
region_pop.plot(kind='barh', color='steelblue')
plt.title("World Population by Region")
plt.xlabel("Population (Billions)")
plt.ylabel("")
plt.tight_layout()
plt.savefig("world_population.png")
print("\nChart saved as world_population.png")
