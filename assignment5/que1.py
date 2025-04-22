import pandas as pd

data = [
    [2022001, 'Abhijeet', 65, 65, 69, 81],
    [2022002, 'Ajeet',    75, 75, 90, 81],
    [2022003, 'Amit',     75,  5, 69, 87],
    [2022004, 'Ranjeet',  55, 65, 79, 91],
    [2022005, 'Santosh',  85, 85, 60, 61],
    [2022006, 'Satyam',   73, 75, 68, 51],
    [2022007, 'Shivam',   85, 85, 50, 40],
    [2022009, 'Shyam',    75, 65, 69, 81],
    [2022010, 'Yash',     85, 75, 89, 61]
]

df = pd.DataFrame(data, columns = ['Reg_no', 'Name', 'Subject1', 'Subject2', 'Subject3', 'Subject4']
)
print(df)
print("---"*45)

df['total'] = None

for index, row in df.iterrows():
    df.at[index, 'total'] = df.at[index, 'Subject1'] + df.at[index, 'Subject2'] + df.at[index, 'Subject3'] + df.at[index, 'Subject4']

print(df)
print("---"*45)

df['grade'] = None

# here index is the index of row and row is series like ['total':290, 'grade':'A'...] etc.
# we can also check values like row['total'] >= 290 types
for index, row in df.iterrows():
    if df.at[index, 'total'] >= 290:
        df.at[index, 'grade'] = 'A'
    elif df.at[index, 'total'] >= 280:
        df.at[index, 'grade'] = 'B'
    elif df.at[index, 'total'] >= 270:
        df.at[index, 'grade'] = 'C'
    elif df.at[index, 'total'] >= 240:
        df.at[index, 'grade'] = 'D'
    else:
        df.at[index, 'grade'] = 'F'

print(df)
print("--"*70)

# to create a subset out of existing dataframe
#if columns dont exist then it will give error
subset = df[['Reg_no', 'Name', 'grade']]

print(subset)
print("--" * 70)


# new_df = df[df['grade'] = 'A'] it will return all rows where grade = A and create a new dataframe
# for grade in df['grade'].unique(): to iterate in dataframe with column grade as unique values like A,B,C,D not like A,A,A,B,B,C

for grade in df['grade'].unique():
    new_df = df[df['grade'] == grade]
    new_df.to_csv(f'students_{grade}.csv')

