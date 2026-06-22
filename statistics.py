import pandas as pd

df = pd.read_csv('tallest_people_in_the_world.csv')

# Summary statistics per group
print("Summary statistics by continent:")
print(df.groupby('continent')[['height_cm', 'lifespan', 'weight_kg']].describe())