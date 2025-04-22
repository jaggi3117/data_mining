import pandas as pd
import numpy as np
import math
k = 3

df = pd.read_csv('./page-blocks_csv.csv')
print(df)

# when i write like this df[df['class']] here df['class'] is a pandas list of class attributes values at each index 
# like df['class'] = [1,3,4,2,1,1,1,1,5 ... etc]
# when i write like this df['class'] == 1 it is pandas list comparision so it compares every value with 1 and return list of trues and falses 
# df[df['class'] == 1] it will select all rows where inside condition is true so all those index where true is present those will get selected 
# if i write df[[true, true, true, false, ... for all rows]] it will select rows where true is present 
# df[df['class']] -> error because inside of df[] is not a bool mask it will only accept a  kind of array which is bool 

class_1 = df[df['class'] == 1] 
class_2 = df[df['class'] == 2]
class_3 = df[df['class'] == 3]
class_4 = df[df['class'] == 4]
class_5 = df[df['class'] == 5]

notclass_1 = df[df['class'] != 1]
notclass_2 = df[df['class'] != 2]
notclass_3 = df[df['class'] != 3]
notclass_4 = df[df['class'] != 4]
notclass_5 = df[df['class'] != 5]

# we calculate fischer score for 2 class types mainly either 1,2 1,3 1,4 2,3 2,4 3,4 types. or either 1 vs not 1 2 vs not 2 and so on.. choosing second method for fischer score

# df.columns -> return the labels of columns {index object}
# df.index -> returns the labels of rows 0,1,2 .. etc. {index object}
# df['columnlabel'].mean() -> return mean value
# df['columnlabel'].std() -> return standard deviation value
fischer_score = []

mapper_dict = {}

for column in class_1.columns:
    if column == 'class':
        continue
    _mean = class_1[column].mean()
    _std = class_1[column].std()
    _notmean = notclass_1[column].mean()
    _notstd = notclass_1[column].std()
    fischer_value = ((_mean  - _notmean) ** 2)/(_std ** 2 + _notstd ** 2)
    fischer_score.append(fischer_value)
    mapper_dict[fischer_value] = column
# do this procedure for class 2 vs all , class 3 vs all and so on ... 

sorted_fischer_score = sorted(fischer_score, reverse=True)
print("--"*50)
print(f'to {k} fischer score attributes')
for i in range(k):
    print(sorted_fischer_score[i], ' attribute ->', mapper_dict[sorted_fischer_score[i]])

print("--"*50)
print(f'all attributes with their fischer score and rank')
for i in range(len(sorted_fischer_score)):
    print(f'rank {i+1} -> fischer score {sorted_fischer_score[i]} -> attribute {mapper_dict[sorted_fischer_score[i]]}')
    





