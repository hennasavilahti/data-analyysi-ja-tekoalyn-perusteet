import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('emp-dep.csv', dtype={'phone1':str, 'phone':str})

agc = df['age_group'].value_counts().sort_index()
agc.plot(kind='bar')

max_count = range(agc.max() + 1)

plt.gca().yaxis.set_major_locator(plt.MultipleLocator(1))
plt.show()
