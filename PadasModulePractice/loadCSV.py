import pandas as pd 

df = pd.read_csv('nyc_weather.csv')
#print the dataframe
print(df) 

#get the max temperature
max_temp = df['Temperature'].max()
print("Max Temperature : {}".format(max_temp)) 
print('--------------------------------')

#Get all the days when it rain's
days_when_rain = df['EST'][df['Events']=='Rain']
print('------------------Days when it rained------------------- ')
print(days_when_rain)

#average windSpeed
df.fillna(0, inplace =True)
print(df)
average_windSpeed = df['WindSpeedMPH'].mean()
print('average wind speed : {}'.format(average_windSpeed))
print('--------------------------------')