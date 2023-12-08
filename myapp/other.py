import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)

# weather_data ={
#     'day':['1/1/2014','1/2/2023','1/3/2019','1/4/2020'],
#     'temperature':[12,23,34,45,],
#     'windspeed' : ['rain','sunny','snow','Rain']
# }
# df = pd.DataFrame(weather_data)
# print(df[['day','temperature']][df.temperature==df['temperature'].max()])

file_path = '/Desktop/Kolkata_weather_data.csv'
df = pd.read_csv(file_path,header=0, index_col=0)
df.dropna(axis = 'rows', inplace = True)
print(df.head())