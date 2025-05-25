import pandas as pd
df = pd.read_csv('nyc_weather.csv')
# print(df)

# print(df['Temperature'].max())

print(df['EST'][df['Events']== 'Rain'])


