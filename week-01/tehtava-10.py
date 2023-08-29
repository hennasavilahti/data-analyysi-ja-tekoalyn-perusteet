import pandas as pd

df = pd.read_csv('diabetes.csv')

desc = df.describe()

df2 = df.isnull().sum()
print(df2)
