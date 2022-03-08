import pandas as pd
df = pd.read_csv('music_log_upd.csv')
#print(df) # проверка

#Применим последовательную фильтрацию
#Для начала отсеим значения строк с жанром pop
pop_music = df[df['genre_name'] == 'pop']
#print(pop_music) - проверка

#Исключим треки с нулевыми значениями и выводим на экран
pop_music = pop_music[pop_music['total_play_seconds'] != 0]
#print(pop_music)
#Самый прослушиваемый трек, длина
pop_music_max_total_play = pop_music['total_play_seconds'].max()
#print(pop_music_max_total_play)
#Строка - Самый прослушиваемый трек
pop_music_max_info = pop_music[pop_music['total_play_seconds'] == pop_music_max_total_play]
print(pop_music_max_info)