import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import subprocess


df = pd.read_excel('economic_freedom_index2019_data.xlsx')

numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
corr_matrix = df[numeric_columns].corr()

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")

# Add title
plt.title('Correlation Heatmap')

# Save the plot as a PNG file
plt.savefig('vis.png')

plt.show()
subprocess.run(["python3", "model.py", 'economic_freedom_index2019_data.xlsx'])
