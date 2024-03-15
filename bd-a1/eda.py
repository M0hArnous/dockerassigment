import pandas as pd
import subprocess
# prompt: Conduct exploratory data analysis, generating at least 3 insights without
# visualizations. Save these insights as text files named eda-in-1.txt, eda-in-2.txt,
# and so on.
df = pd.read_excel('economic_freedom_index2019_data.xlsx')

# Insight 1: Summary Statistics
summary_stats = df.describe()
summary_stats_file = "eda-in-1.txt"
summary_stats.to_csv(summary_stats_file, sep='\t')

# Insight 2: Categorical Analysis
unique_countries = df['Country Name'].nunique()
unique_regions = df['Region'].nunique()
unique_webnames = df['WEBNAME'].nunique()
countries_count = df['Country Name'].value_counts().head(10)
regions_count = df['Region'].value_counts().head(10)
categorical_analysis = f"Unique Countries: {unique_countries}\nUnique Regions: {unique_regions}\nUnique Web Names: {unique_webnames}\n\nTop 10 Countries:\n{countries_count}\n\nTop 10 Regions:\n{regions_count}"
categorical_analysis_file = "eda-in-2.txt"
with open(categorical_analysis_file, 'w') as file:
    file.write(categorical_analysis)

# Insight 3: Correlation Analysis
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
correlation = df[numeric_columns].corr()
correlation_file = "eda-in-3.txt"
correlation.to_csv(correlation_file, sep='\t')

print("Exploratory Data Analysis completed. Insights saved as text files.")
subprocess.run(["python3", "vis.py", 'economic_freedom_index2019_data.xlsx'])

