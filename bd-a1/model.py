import pandas as pd
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
import subprocess


df = pd.read_csv('res_dpre.csv')

# Select columns for K-means clustering
columns_for_clustering = ['Population (Millions)', 'GDP (Billions, PPP)', '5 Year GDP Growth Rate (%)', 'GDP per Capita (PPP)', 'Inflation (%)']
# Preprocess the data
for column in columns_for_clustering:
    # Replace non-numeric characters with NaN
    df[column] = pd.to_numeric(df[column].astype(str).str.replace('[^\d.]', ''), errors='coerce')

    # Impute missing values with the mean
    imputer = SimpleImputer(strategy='mean')
    df[column] = imputer.fit_transform(df[column].values.reshape(-1, 1))

# Apply K-means algorithm
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[columns_for_clustering])

# Count records in each cluster
cluster_counts = df['Cluster'].value_counts()

# Save results to a text file
cluster_counts.to_csv('k.txt', header=True, index=True)

print("Number of records in each cluster saved to k.txt.")

subprocess.run(["bash", "final.sh"], check=True)

