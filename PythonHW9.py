import pandas as pd

#40

df = pd.read_csv('sample_data/california_housing_train.csv')
filtered_df = df[(df['population'] >= 0) & (df['population'] <= 500)]
mean_price = filtered_df['median_house_value'].mean()
print(f'Средняя стоимость дома с кол-вом людей от 0 до 500: {mean_price}')

#42

df = pd.read_csv('sample_data/california_housing_train.csv')
min_population = df['population'].min()
filtered_df = df[df['population'] == min_population]
max_households = filtered_df['households'].max()
print(f'Максимальное кол-во households в зоне с мин значением population: {max_households}')