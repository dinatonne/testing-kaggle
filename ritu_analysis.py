import pandas as pd

df = pd.read_csv('/Users/hilde/Desktop/CytoFit/testing_kaggle/rituximab.csv')

# Basic data quality check
print("Dataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())
print("\nBasic statistics:")
print(df.describe())

# Cell population breakdown 
gate_counts = df['Gate'].value_counts()
gate_pct = (gate_counts / len(df) * 100).round(2)
print("Cells per gate:")
print(gate_counts)
print("\nPercentage per gate:")
print(gate_pct)