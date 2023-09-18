import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('emp-dep.csv', dtype={'phone1':str, 'phone':str})

avg = round(df['salary'].mean(), 2)

plt.scatter(x=df['age'], y=df['salary'])
plt.title('Työntekijät ja palkat')
plt.xlabel(f'Keskipalkka {avg}, n: {df.shape[0]}')
plt.show()

df_counts = pd.DataFrame(df['dname'].value_counts().reset_index())

sns.barplot(x='dname', y='count', data=df_counts)
plt.show()

sns.barplot(x='count', y='dname', data=df_counts)
plt.show()

