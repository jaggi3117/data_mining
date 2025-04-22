import pandas as pd
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

