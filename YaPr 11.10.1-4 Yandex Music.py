import pandas as pd
df = pd.read_csv('music_log_upd.csv')
df.tail()
df.tail().groupby('user_id')
#print(df) #провека работает
df.tail().groupby('user_id').sum() 
current_engagement = df.tail().groupby('user_id').sum().median()
print(current_engagement) #выходит ошибка при выводе

