import pandas as pd

l=[1,2,3,4,5]
x=pd.Series(l)
# print(x)
name=["abc","cbv","ddf", "adcad", "sdsfv"]
area=["pune", "mumbai", "banglore", "noida", "kolkata"]
math=[12,24,46,67,87]
english=[54,23,76,86,87]
science=[35,75,98,34,36]
details={"Name":name,"Area": area, "Math": math, "English": english, "Science": science}

data=pd.DataFrame(details)
# print(data)
# print(data.head(4))

# print(data['Area']) # use key name rather than data name
# print(data[['Name', 'Area']])

# slicing
# print(data[0:3:1])

# iterrows
# for i in data.iterrows():
#     print(i)

# print(data.describe())
# print(data.shape)