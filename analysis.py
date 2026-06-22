import pandas as pd

df = pd.read_csv('tallest_people_in_the_world.csv')

print(df.head())
print('                                         ')
print(df.tail())
print('                                         ')
print(df.info())
print('                                         ')
print(df.describe())
print('                                         ')

# Prints the top 10 tallest people in the world
print('                                         ')
print('      Top 10 Tallest People in the World       ')
print('-----------------------------------------------')
print(df.sort_values('height_cm', ascending=False).head(10))

# Prints the 10 longest lived tallest people in the worlds
print('                                         ')
print('   Top 10 Longest Lived Tallest People in the World   ')
print('------------------------------------------------------')
print(df.sort_values('lifespan', ascending=False).head(10))

# Prints the 10 tallest people in Europe
print('                                         ')
print('      Top 10 Tallest People in Europe       ')
print('--------------------------------------------')
print(df.loc[df['continent'] == 'Europe'].sort_values('height_cm', ascending=False).head(10))

# Prints the average heigh by continent
print('                                         ')
print('      Average Height By Continent       ')
print('----------------------------------------')
print(df.groupby('continent')['height_cm'].mean())

# Prints the average weight by continent
print('                                         ')
print('      Average Weight by Continent       ')
print('----------------------------------------')
print(df.groupby('continent')['weight_kg'].mean())

# Prints most represented countries
print('                                         ')
print('      Most Represented Countries       ')
print('---------------------------------------')
print(df['country'].value_counts())

# Prints most common medical conditions
print('                                         ')
print('     Most Common Medical Conditions      ')
print('-----------------------------------------')
print(df['medical_condition'].value_counts())

# Correlation between height, lifespan and weight
print('                                         ')
print('Does Height Affect Lifespan?')
print('-----------------------------------------')
print(df[["height_cm", "lifespan", "weight_kg"]].corr())