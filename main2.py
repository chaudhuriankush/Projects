import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 1. Load Data - Fixed filename space
try:
    df = pd.read_excel('analysis1 .xlsx') 
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'analysis1.xlsx' not found. Check the filename.")

# 2. Data Cleaning
df.drop_duplicates(inplace=True)
# Fill missing bedrooms if they exist (common in this dataset)
df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())

# 3. Feature Engineering
df['rooms_per_household'] = df['total_rooms'] / df['households']
df['bedrooms_per_room'] = df['total_bedrooms'] / df['total_rooms']
df['population_per_household'] = df['population'] / df['households']

# 4. Visualizations - Histograms
numerical_features = ['median_house_value', 'median_income', 'housing_median_age', 'total_rooms', 'population']
plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_features):
    plt.subplot(2, 3, i + 1)
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# 6. Geographical Plot - Fixed Redundancy and Colorbar
plt.figure(figsize=(10, 7))
# Using standard matplotlib scatter for easier colorbar handling
plt_scatter = plt.scatter(df['longitude'], df['latitude'], 
                          c=df['median_house_value'], cmap='viridis', 
                          s=df['population']/100, alpha=0.5)
plt.colorbar(plt_scatter, label='Median House Value')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('California Housing Prices by Location')
plt.show()