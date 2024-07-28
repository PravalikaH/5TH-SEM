import pandas as pd                          
import numpy as np

# Read the data
df = pd.read_csv('auto_mpg.csv')

# 1. Fuel efficient cars
fuel_efficient = df[(df['mpg'] > 29) & (df['horsepower'] < 93.5) & (df['weight'] < 2500)]
print("Number of fuel efficient cars:", len(fuel_efficient))

# 2. Muscle cars
muscle_cars = df[(df['displacement'] > 262) & (df['horsepower'] > 126) & 
                 (df['weight'] >= 2800) & (df['weight'] <= 3600)]
print("Number of muscle cars:", len(muscle_cars))

# 3. SUVs
suvs = df[(df['horsepower'] > 140) & (df['weight'] > 4500)]
print("Number of SUVs:", len(suvs))

# 4. Racecars
racecars = df[(df['weight'] < 2223) & (df['acceleration'] > 17)]
print("Number of racecars:", len(racecars))

# 5. Sort by number of cylinders
sorted_by_cylinders = df.sort_values(by='cylinders')
print("\nCars sorted by number of cylinders:")
print(sorted_by_cylinders[['cylinders', 'name']].head())

# 6. Cars with lowest acceleration and higher horsepower
lowest_acceleration = df.sort_values('acceleration').head()
print("\nCars with lowest acceleration and their horsepower:")
print(lowest_acceleration[['name', 'acceleration', 'horsepower']])

# 7. Statistics of numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns
stats = df[numerical_cols].agg(['min', 'max', 'sum', 'mean', 'median'])
print("\nStatistics of numerical columns:")
print(stats)

# 8. Number of cars manufactured each year
cars_per_year = df['model_year'].value_counts().sort_index()
print("\nNumber of cars manufactured each year:")
print(cars_per_year)

# 9. Relationship between model year and acceleration
year_acceleration = df.groupby('model_year')['acceleration'].mean()
print("\nAverage acceleration by model year:")
print(year_acceleration)

# 10. Distribution of cylinders across years
cylinder_distribution = pd.crosstab(df['model_year'], df['cylinders'])
print("\nDistribution of cylinders across years:")
print(cylinder_distribution)

# 11. Mean of numerical attributes for each year
mean_attributes = df.groupby('model_year')[numerical_cols].mean()
print("\nMean of numerical attributes for each year:")
print(mean_attributes)
