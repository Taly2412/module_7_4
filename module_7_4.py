team1 = 'Мастера кода'
team1_num = 5
score_1 = 40
team1_time = 1552.512
team2 = 'Волшебники данных'
team2_num = 6
score_2 = 42
team2_time = 2153.31451
print('В команде %s участников: %s!' % (team1, team1_num))
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
print('Команда {0} решила задач: {1}'.format(team2, score_2))
print('{0} решили задачи за {1}!'.format(team2, team2_time))
print(f'Команды решили {score_1} и {score_2} задач')
if team1_time/score_1 < team2_time/score_2:
    challenge_result = f"Результат битвы: победа команды {team1}!"
elif team1_time/score_1 > team2_time/score_2:
    challenge_result = f'Результат битвы: победа команды {team2}!'
else:
    challenge_result = f"Ничья"
print(challenge_result)
tasks_total = (score_1 + score_2)
time_avg = (team1_time + team2_time)/tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')


