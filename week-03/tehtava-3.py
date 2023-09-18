import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('emp-dep.csv', dtype={'phone1':str, 'phone':str})

gvc = df['gender'].value_counts()
gvc.plot(kind='pie', ylabel='', labels=['miehet', 'naiset'], startangle=270, autopct='%1.1f%%')
plt.show()

cag = df.groupby(['age_group', 'gender']).size().unstack()
ax = cag.plot(kind='bar')
ax.legend(['miehet', 'naiset'])
plt.title('Työntekijät ikäryhmittäin')
plt.ylabel('Lukumäärä')
plt.xlabel('Ikäryhmä')
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(1))
plt.show()

