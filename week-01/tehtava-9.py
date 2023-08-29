import pandas as pd

df = pd.read_csv('diabetes.csv')

desc = df.describe()

df2 = df.pivot_table(index = ['Age'], aggfunc = 'size').sort_values(ascending=False)
print(df2)

diabetes = df['Outcome'].value_counts().sort_values(ascending=False)
print(diabetes)
