import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')
df.drop(df.loc[df['PClass']=='*'].index, inplace=True) # poistetaan *
df['Saved'] = df['Survived'].apply(lambda x: 'no' if x == 0 else 'yes')

passenger_count = df.shape[0]

# Pylväskaavio
bins2 = list(range(0,95,5))
    
labels = bins2[1:]
df['age_group'] = pd.cut(df['Age'], bins=bins2, labels=labels, right=False)
df['age_group'] = df['age_group'].astype(int)

cag = df.groupby('age_group')['age_group'].count()
ax = cag.plot(kind='bar')
plt.show()

# Piirakka-kaavio
f_survivors = sum(df.where(df['GenderCode'] == 1)['Survived'] == 1)
m_survivors = sum(df.where(df['GenderCode'] == 0)['Survived'] == 1)

df_survivors = df[df['Survived'] == 1].copy()

gvc = df_survivors['Gender'].value_counts()
gvc.plot(kind='pie', subplots=True, ylabel='Selviytyneet', labels=['naiset', 'miehet'], startangle=270, autopct='%1.1f%%', 
         title=['Matkustajia: {} \n Selviytyneet miehet: {} \n Selviytyneet naiset: {}'.format(passenger_count, m_survivors, f_survivors)])
plt.show()

# Laatikko-jana-kaavio
sns.boxplot(x='PClass', y='Age', hue='Saved', data=df)
plt.show()

# Stripplot naiset
df_females = df.loc[df['Gender'] == 'female']

ax=sns.stripplot(x='PClass', y='Age', hue='Saved', data=df_females)
ax.set_title('females')
plt.show()

# Stripplot miehet
df_males = df.loc[df['Gender'] == 'male']

ax=sns.stripplot(x='PClass', y='Age', hue='Saved', data=df_males)
ax.set_title('males')
plt.show()

