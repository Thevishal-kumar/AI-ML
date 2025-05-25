import pandas as pd

df = pd.read_csv("weather_data.csv")
# print(df)

# print(df.shape)
# print(df.head(3))
# print(df.tail(3))

# print(df[['day','temperature']])

# print(df.temperature.max())

# print(df.temperature,df.day)

# print(df.day[df.temperature == df.temperature.max()])
print(df[df.temperature == df.temperature.max()])