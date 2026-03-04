import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# read dataset into a pandas DataFrame
df = pd.read_csv('Cleaned_Samsung_5G_Dataset.csv')

df.info()
df.head()
df.columns
    
df["5G_capability"].value_counts()
df["units_sold"].describe()

# Analyze the relationship between 5G capability and units sold
df.groupby("5G_capability")["units_sold"].agg(["count", "mean", "median", "std"])

# Calculate the difference in overall mean units sold between 5G and non-5G phones
mean_values = df.groupby("5G_capability")["units_sold"].mean()
    
difference = mean_values["Yes"] - mean_values["No"]
percent_increase = (difference / mean_values["No"]) * 100
difference, percent_increase

# Calculate the regional difference in units sold for 5G and non-5G phones
df.groupby(["region", "5G_capability"])["units_sold"].mean().unstack()

region_summary = (
    df.groupby(["region", "5G_capability"])["units_sold"]
    .mean()
    .reset_index()
    
)
region_summary.head().unstack()
    
columns = ['release_year', '5G_capability', 'units_sold', 'region']

# Figure 1: Average units sold by region for 5G vs non-5G phones 
plt.figure(figsize=(12,6))
sns.barplot(
    data=region_summary,
    x="region",
    y="units_sold",
    hue="5G_capability"
)
plt.title("Average Units Sold by Region: 5G vs Non-5G")
plt.xlabel("Region")
plt.ylabel("Average Units Sold")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()

plt.show()

# Calculate the overall mean units sold for 5G and non-5G phones
overall_means = df.groupby("5G_capability")["units_sold"].mean().reset_index()

overall_means

#figure 2: Overall average units sold for 5G vs non-5G phones
plt.figure(figsize=(8,6))
sns.barplot(
    data=overall_means,
    x="5G_capability",
    y="units_sold",
    hue="5G_capability"
)

plt.title("Average Units Sold (Globally): 5G vs Non-5G")
plt.xlabel("5G Capability")
plt.ylabel("Average Units Sold")
plt.tight_layout()

plt.show()

# Figure 3: Boxplot of units sold distribution for 5G vs non-5G phones
plt.figure(figsize=(8,6))

sns.boxplot(
    data=df,
    x="5G_capability",
    y="units_sold",
    hue="5G_capability",
)

plt.title("Distribution of Units Sold: 5G vs Non-5G Phones")
plt.xlabel("5G Capability")
plt.ylabel("Units Sold")
plt.tight_layout()

plt.show()

# EXTRA - Figure 4:scatterplot to analyze the relationship between regional 5G coverage and units sold
plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="regional_5g_coverage_percent",
    y="units_sold",
    hue="5G_capability",
    s=80,          # larger points
    alpha=0.7      # transparency so overlaps are visible
)

plt.title("Relationship Between 5G Coverage and Units Sold")
plt.xlabel("Regional 5G Coverage (%)")
plt.ylabel("Units Sold")

plt.show()
