import pandas as pd
import matplotlib.pyplot as plt
df.read_csv('tallest_people_in_the_world.csv')

df['height_cm'].hist()
plt.title('Height Distribution')
plt.show()

df.groupby('continent')['lifespan'].mean().plot(kind=bar)
plt.title('Average Lifespan by Continent')
plt.show()

df.plot.scatter(x='height_cm', y='lifespan')
plt.title('Height vs. Lifespan')
plt.show()

df.groupby('country')['weight_kg'].mean().plot(kind=bar)
plt.title('Average Weight (kg) by Country')
plt.show()

df['medical_condition'].value_counts().plot(kind=bar)
plt.title('The Most Common Medical Conditions')
plt.xsticks(rotation=45) # Rotates labels on x axis 45 degrees so they are readable vertically 
plt.show() 
plt.show() 

df.boxplot(column='height_cm', by='continent')
plt.title('Height Distribution by Continent')
plt.suptitle('')
plt.xticks(rotation=45)
plt.show()

df.groupby('birth_year')['height_cm']mean.plot(kind=line)
plt.title('Average Height Over Time')
plt.xlabel('Birth year')
plt.ylabel('Height (cm)')
plt.show()
