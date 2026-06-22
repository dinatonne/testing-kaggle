import pandas as pd

df = pd.read_csv('tallest_people_in_the_world.csv')

# Summary statistics per group
print("Summary statistics by continent:")
print(df.groupby('continent')[['height_cm', 'lifespan', 'weight_kg']].describe())

print('n\Corrolations:')
print(df[['height_cm', 'lifespan', 'weight_kg']].corr())

print('n\Outliers:')
mean_height = df['height_cm'].mean()
std_height = df['height_cm'].std() 

outliers = df[df['heigh_cm'] > mean_height + 2 * std_height] # Formel 
print('n\Height outlier:')
print(outliers[['name', 'country', 'height_cm']])
