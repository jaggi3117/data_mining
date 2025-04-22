import pandas as pd
import numpy as np
def indent():
    print("--"*60)
    return


#to import some data from csv
df = pd.read_csv('./weather-numeric.csv')
print(df)
indent()


y = df['play']
print(y)
indent()

# df.shape -> [number of rows, number of columns], eg. df.shape[0] -> rows df.shape[1] -> columns

#x = df['outlook', 'temperature', 'humidity']
#this is wrong to select a column you should pass list of columns as input 
x = df[['outlook', 'temperature', 'humidity']]
print(x)
indent()

#splitting training and testing data 
# df.index return a list like of indexes 
# df.drop(args) in args we pass indexes 
train_df = df.sample(frac=0.8, random_state=42)
test_df = df.drop(train_df.index)

# to split dataframes
# if the number of entries is not evenly divisible by 5 or n it will result in error
# after split a numpy array will be created where each element is a dataframe
trainsplit = np.split(train_df, 5)
testsplit = np.split(test_df, 5)

counter = 1
for df in trainsplit:
    df.to_csv(f'./train_{counter}.csv')
    counter += 1

counter = 1
for df in testsplit:
    df.to_csv(f'./test_{counter}.csv')
    counter += 1

