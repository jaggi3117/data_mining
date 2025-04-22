import pandas as pd
import numpy as np
import math

# has to calculate entropy of total data set then of each attribute and then finally information gain

df = pd.read_csv('./Buy_Computer.csv')
print(df)

# to take log result = math.log(x, base)

def total_entropy(df):
    target_class = df.columns[-1]
    #target_data = df[[target_class]] this is wrong it will create a new dataframe we need a numpy array
    target_data = df[target_class] # this will series of target_class values like series
    total = len(target_data)

    probs = []
    for value in target_data.unique():
        count = 0
        for v in target_data:
            if v == value:
                count += 1
        fract = count/total
        probs.append(fract)
    sum = 0
    for prob in probs:
        sum += (-1)*(prob)*(math.log(prob,2))
    return sum

entropy = total_entropy(df)
print(entropy)


