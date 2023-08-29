import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes.csv')

desc = df.describe()

df[['Pregnancies', 'Glucose', 'BloodPressure']].hist()
plt.show()

diabetes = df['Outcome'].value_counts()

corr = df.corr()

sns.heatmap(corr, annot=True)
plt.show()
