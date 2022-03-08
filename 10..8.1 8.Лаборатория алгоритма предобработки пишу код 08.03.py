# импортируйте библиотеку pandas
import pandas as pd
# считайте csv-файл 'music_log.csv' в переменную df
df = pd.read_csv('music_log.csv')
# переименуйте названия столбцов df
df.rename(columns = {'  user_id' : 'user_id',
                     'total play' : 'total_play',
                     'Artist' : 'artist'}, inplace = True)
# объявите список columns_to_replace с названиями столбцов track, artist, genre
columns_to_replace =  ['track', 'artist', 'genre']
# заполните отсутствующие значения столбцов из списка columns_to_replace значением 'unknown' в цикле
for column in columns_to_replace:
    df[column] = df[column].fillna('unknown')
# удалите строки-дубликаты из датафрейма df
df = df.drop_duplicates().reset_index(drop=True)
# выведите на экран первые 20 строчек обновлённого набора данных df
print(df.head(20))