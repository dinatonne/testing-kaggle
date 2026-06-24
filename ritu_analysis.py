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

# Flagging outlier cells 
mean_fsc = df['FSC.H'].mean()
std_fsc = df['FSC.H'].std()

outliers = df[(df['FSC.H'] > mean_fsc + 3 * std_fsc) | 
              (df['FSC.H'] < mean_fsc - 3 * std_fsc)]

print(f"Total cells: {len(df)}")
print(f"Outlier cells: {len(outliers)}")
print(f"Outlier percentage: {(len(outliers)/len(df)*100).round(2)}%")

# Comparing gate populations 
for gate in sorted(df['Gate'].unique()):
    subset = df[df['Gate'] == gate]
    print(f"\nGate {gate} ({len(subset)} cells):")
    print(f"  Mean FSC: {subset['FSC.H'].mean().round(1)}")
    print(f"  Mean SSC: {subset['SSC.H'].mean().round(1)}")
    print(f"  Mean FL1: {subset['FL1.H'].mean().round(1)}")