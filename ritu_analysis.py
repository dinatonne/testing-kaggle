import pandas as pd

df = pd.read_csv('/Users/hilde/Desktop/CytoFit/testing_kaggle/rituximab.csv')

# Basic data quality check
print("Dataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())
print("\nBasic statistics:")
print(df.describe())