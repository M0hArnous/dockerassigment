import pandas as pd 
import numpy as n
import subprocess
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# prompt: This file should perform Data Cleaning, Data Transformation, Data
# Reduction, and Data Discretization steps. In each step apply minimum 2 tasks.
# Save the resulting data frame as a new CSV file named res_dpre.csv
df = pd.read_excel('economic_freedom_index2019_data.xlsx')
# prompt: This file should perform Data Cleaning, Data Transformation, Data
# Reduction, and Data Discretization steps. In each step apply minimum 2 tasks.
# Save the resulting data frame as a new CSV file named res_dpre.csv.

# Data Cleaning
df.dropna(subset=['Country'], inplace=True)

# Data Transformation
df['Total_score'] = df[['Property Rights', 'Judical Effectiveness', 'Government Integrity', 'Tax Burden', 'Gov Spending', 'Investment Freedom', 'Financial Freedom', 'Trade Freedom', 'Labor Freedom']].sum(axis=1)
df['Region'] = df['Country'] + ', ' + df['Region']

# Data Reduction
df = df.drop(['Country Name', 'GDP Growth Rate (%)', 'Unemployment (%)'], axis=1)

# Data Discretization
bins = [0, 50, 60, 70, 80, 90, 100]
labels = ['Very Low', 'Low', 'Medium', 'High', 'Very High', 'Extremely High']
df['Total_score_discretized'] = pd.cut(df['Total_score'], bins=bins, labels=labels)

# Save the resulting data frame
df.to_csv('res_dpre.csv', index=False)
subprocess.run(["python3", "eda.py", 'economic_freedom_index2019_data.xlsx'])
