import pandas as pd

df = pd.read_excel('weather_data.xlsx')
print(df) 

# print(df.to_csv('new.csv'))
# df.to_excel('new.xlsx',sheet_name='weather_data') 


# temperature_df = pd.DataFrame({
#     "city": ["mumbai","delhi","banglore", 'hyderabad'],
#     "temperature": [32,45,30,40]})
# temperature_df

# humidity_df = pd.DataFrame({
#     "city": ["delhi","mumbai","banglore"],
#     "humidity": [68, 65, 75]})
# humidity_df


# df = pd.merge(temperature_df,humidity_df, on='city',how='outer')
# print(df)

df = pd.DataFrame([1,2,3,4,5,6,7,8,9,19],index=[49,48,47,46,45,1,2,3,4,5])
print(df.loc[45]) #print accoridng to index wise
print(df.iloc[4]) #print according to row wise
