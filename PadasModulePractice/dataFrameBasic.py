import pandas as pd 

# So we can import the data from csv
#df = pd.read_csv('nyc_weather.csv')


# we can create data frame from dictionary
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}

# load the dintionary in dataframe
df = pd.DataFrame(weather_data)

# Print the data frame
print(df)

# print the shape of data frame
print(df.shape)

# print head from data frame 
# print(df.head()) #print few rows from start
print(df.head(2)) # print only rows rows
print(df.tail(2)) # print only last two rows

# print row between 2 and 5 (5 is exculed)
print(df[2:5])

# print the number of columns
print(df.columns)

#print specific column 
print(df.day)
print(df['event']) #same as above

# print type of columns
print(type(df['day']))

# print only few columns
print(df[['day','temperature']])

# Print max
max_temp = df['temperature'].max()
print(max_temp)


# use describe to get all details such as min max avg std
print(df.describe())

# Conditionally select the data from dataFrame

# 1- select the all rows very temperature is greater then equal 32
print(df[df.temperature >= 32])
 
# 2- Give the row were temperature is maximium
print(df[df.temperature == df.temperature.max()])

# 3- give the day and temperature where temperature was max
print(df[['day','temperature']][df.temperature == df.temperature.max()])

# Set Index functionalityd value
print(df.index)

# change index from default to some column in dataframe
print(df.set_index('day',inplace =True))
#df = df.set_index('day')

# Find value from index
print(df.loc['1/4/2017'])

# Reset the index
df.reset_index(inplace = True)

print(df)