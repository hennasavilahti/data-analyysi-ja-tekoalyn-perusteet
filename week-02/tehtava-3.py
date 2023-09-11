import pandas as pd

df_titanic_names = pd.read_csv('Titanic_names.csv')
df_titanic_data= pd.read_csv('Titanic_data.csv')

print(df_titanic_data.info())
print(df_titanic_data.describe())
print(df_titanic_names.info())
print(df_titanic_names.describe())

hist_data = df_titanic_data.hist(bins=4)

df = pd.merge(df_titanic_data, df_titanic_names, how='inner', on='id')

passenger_count = df.shape[0]

m_count = sum(df.GenderCode== 0)
f_count = sum(df.GenderCode== 1)

passenger_age_mean = df.Age.mean()
passenger_aged_zero = sum(df.Age == 0)

new_passenger_age_mean = df.Age.where(df['Age'] != 0).mean()

df.loc[df['Age'] == 0, 'Age'] = new_passenger_age_mean

print(df['PClass'].unique())

pclass_star = df.loc[df['PClass'] == '*']

count_survivors = sum(df['Survived'] == 1)
count_losses = sum(df['Survived'] == 0)

surv_pros = round(count_survivors / passenger_count * 100, 1)
loss_pros = round(count_losses / passenger_count * 100, 1)
print("Survivors: {}% Losses: {}%".format(surv_pros, loss_pros))

count_survivors_f = sum(df.where(df['GenderCode'] == 1)['Survived'] == 1)
count_losses_f = sum(df.where(df['GenderCode'] == 1)['Survived'] == 0)
count_survivors_m = sum(df.where(df['GenderCode'] == 0)['Survived'] == 1)
count_losses_m = sum(df.where(df['GenderCode'] == 0)['Survived'] == 0)

