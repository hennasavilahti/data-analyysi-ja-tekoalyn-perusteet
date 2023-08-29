import pandas as pd

df = pd.read_csv('diabetes.csv')

desc = df.describe()

print(f'{df["Pregnancies"].max()}')
print(f'{df["Pregnancies"].count()}')

df.hist()
