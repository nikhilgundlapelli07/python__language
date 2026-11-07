import pandas as pd
import numpy as np

# s = pd.Series([10, 20, 30, 40])
# print(s)

# s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# print(s)

# s = pd.Series({'a': 100, 'b': 200, 'c': 300})
# print(s)

# df = pd.DataFrame({
#     'Name': ['Rakesh', 'Adhithya', 'Ram', 'Shyam'],
#     'Age': [25, 30, 22, 28],
#     'City': ['Hyderabad', 'Delhi', 'Mumbai', 'Chennai'],
#     'Salary': [30000, 45000, 25000, 40000]
# })
# print(df)


# df = pd.DataFrame(
#     {'Marks': [80, 90, 75]},
#     index=['A', 'B', 'C']
# )
# print(df)

# df = pd.DataFrame(
#     [['Rakesh', 25], ['Adhithya', 30]],
#     columns=['Name', 'Age']
# )
# print(df)







# df = pd.DataFrame({
#     'Name': ['Rakesh', 'Adhithya', 'Ram'],
#     'Age': [25, 30, 22]
# })

# s = pd.Series([10, 20, 30])

# print(df.shape)
# print(s.shape)

# print(df.index)
# print(s.index)

# print(df.columns)

# s = pd.Series([10, 20, 30], name='Marks')
# print(s.name)

# print(df.axes)
# print(s.axes)

# print(df.values)
# print(s.values)

# print(df.keys())
# print(s.keys())


# print(df.dtypes)
# print(s.dtype)

# print(df.size)
# print(s.size)

# print(df.ndim)
# print(s.ndim)















# df = pd.DataFrame({
#     'Name': ['Rakesh', 'Adhithya', 'Ram'],
#     'Age': [25, 30, 22],
#     'Marks': [85, 90, 95]
# })

# s = pd.Series([10, 20, 30, 40, 50], name='Values')

# df.info()

# print(df.describe())
# print(s.describe())
# print(df.describe(include='all'))

# print(df.head())
# print(df.head(2))
# print(s.head(3))

# print(df.tail(2))
# print(s.tail(2))

# print(df.sample(2))
# print(s.sample(3))

# print(df.nunique())
# print(s.nunique())

# print(df.count())
# print(s.count())








# df = pd.DataFrame({
#     'Name': ['Rakesh', 'Adhithya', 'Ram', 'Shyam'],
#     'Age': [25, 30, 22, 28],
#     'Salary': [30000, 45000, 25000, 40000]
# }, index=['A', 'B', 'C', 'D'])

# print(df['Name'])
# print(df[['Name', 'Salary']])
# print(df[0])   

# print(df.loc['A'])
# print(df.loc['A':'C'])  
# print(df.iloc[0])
# print(df.iloc[0:2])    

# print(df.loc['A', 'Name'])
# print(df.iloc[1, 0])

# print(df.loc['A':'B', ['Name', 'Age']])
# print(df.loc['A':'B', 'Name':'Salary'])
# print(df.iloc[0:3, 0:2])

# print(df.at['B', 'Name'])
# print(df.iat[1, 0])








# df = pd.DataFrame({
#     'Name': ['Rakesh', 'Adhithya', 'Ram', 'Shyam'],
#     'Age': [25, 30, 22, 28],
#     'Salary': [30000, 45000, 25000, 40000]
# })

# print(df['Age'] > 25) 

# print(df[df['Age'] > 25])

# print(df[df['Salary'] >= 30000])

# print(df[(df['Age'] > 23) & (df['Salary'] < 40000)])







df = pd.DataFrame({
    'Name': ['Rakesh', 'Adhithya', None, 'Shyam'],
    'Age': [25, np.nan, 22, 28],
    'Salary': [30000, 45000, np.nan, 40000]
})

# print(df.isna())
# print()
# print(df.isnull())
# print()
# print(df.isna().sum())
# print()
# print(df.isna().sum().sum())

# print()
# print(df.dropna())
# print()
# print(df.dropna(how='all'))
# print()
# print(df.dropna(subset=['Age'])) 
# print()



# print(df.fillna(0))
# print()
# df['Age'] = df['Age'].fillna(df['Age'].mean())
# df['Salary'] = df['Salary'].fillna(df['Salary'].median())
# df['Name'] = df['Name'].fillna('Unknown')
# print(df)


























df = pd.DataFrame({
    'Name': ['Rakesh', 'Adhithya', 'Ram'],
    'Age': [25, 30, 22],
    'Marks': [85, 90, 95]
})

df.to_csv('students.csv', index=False)

df_csv = pd.read_csv('students.csv')
print(df_csv)

df.to_excel('students.xlsx', index=False)

df_excel = pd.read_excel('students.xlsx')
print(df_excel)