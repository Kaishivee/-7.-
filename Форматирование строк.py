team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 18
challenge_result = None
tasks_total = 100
time_avg = 160
print('В команде Мастера кода участников: %s!' % (team1_num))
print('В команде Мастера кода участников: %s и %s!' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {0:d}!'.format(score_2))
print('Волшебники данных решили задачи за {0:f} с'.format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода'
    print(challenge_result)
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных'
    print(challenge_result)
else:
    print('Ничья')
