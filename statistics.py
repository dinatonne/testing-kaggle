import pandas as pd

df = pd.read_csv('tallest_people_in_the_world.csv')

# Summary statistics per group
print("Summary statistics by continent:")
print(df.groupby('continent')[['height_cm', 'lifespan', 'weight_kg']].describe())

print('\nCorrolations:')
print(df[['height_cm', 'lifespan', 'weight_kg']].corr())

print('\nOutliers:')
mean_height = df['height_cm'].mean()
std_height = df['height_cm'].std() 

outliers = df[df['height_cm'] > mean_height + 2 * std_height] # Formel 
print('\nHeight outlier:')
print(outliers[['name', 'country', 'height_cm']])

print('\nMean vs Median height by continent:')
print(df.groupby('continent')['height_cm'].agg(['mean', 'median']))

# Tallest and shortest person by continent
print('\nTallest person per continent:')
print(df.loc[df.groupby('continent')['height_cm'].idxmax()][['name', 'continent', 'height_cm']])

print('\nShortest person per continent:')
print(df.loc[df.groupby('continent')['height_cm'].idxmin()][['name', 'continent', 'height_cm']])

# Heaviest person per continent
print('\nHeaviest person per continent:')
print(df.dropna(subset=['weight_kg']).loc[df.dropna(subset=['weight_kg']).groupby('continent')['weight_kg'].idxmax()][['name', 'continent', 'weight_kg']])