import pandas as pd
import subprocess


# Load the dataset using pandas
df = pd.read_excel('economic_freedom_index2019_data.xlsx')
print(df.head())

# Execute another Python script and pass 'dataset.csv' as an argument
subprocess.run(["python3", "dpre.py", 'economic_freedom_index2019_data.xlsx'])
