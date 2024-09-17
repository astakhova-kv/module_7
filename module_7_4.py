name1 = "Мастера кода"
name2 = "Волшебники данных"
team1_num = int(input('Введите количество участников команды 1: '))
team2_num = int(input('Введите количество участников команды 2: '))
score_1 = int(input('Количество задач решенных командой 1: '))
score_2 = int(input('Количество задач решенных командой 2: '))
team1_time = float(input('Время за которое команда 1 решила задачи: '))
team2_time = float(input('Время за которое команда 2 решила задачи: '))
tasks_total = score_1 + score_2
time_avg = round(((team1_time + team2_time) / tasks_total), 1)

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'победа команды Волшебники Данных!'
else:
    challenge_result = 'ничья!'

print('В команде Мастера кода участников: %s !' % team1_num)
print('В команде Волшебники данных участников: %s !' % team2_num)
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print('Команда {0} решила задач: {1} !'.format(name1, score_1))
print('Команда {0} решила задач: {1} !'.format(name2, score_2))
print("{} решили задачи за {} с !".format(name1, team1_time))
print("{} решили задачи за {} с !".format(name2, team2_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")
