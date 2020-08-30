""" Создать csv с данными о ежедневной погоде. Структура: Дата, место, градусы, скорость ветра.
Найдём среднюю погоду(скорость ветра и градусы) для Минска за последние 7 дней"""

import  csv

fields = ['Дата', 'Место', 'Градусы', 'Скорость ветра']
rows = [
    ['1.08', 'Минск', '+25', 7],
    ['2.08', 'Минск', '+19', 10],
    ['3.08', 'Минск', '+28', 10],
    ['4.08', 'Минск', '+29', 3],
    ['5.08', 'Минск', '+32', 4],
    ['6.08', 'Минск', '+30', 2],
    ['7.08', 'Минск', '+25', 5],
    ['8.08', 'Минск', '+22', 5]
]

with open('weather.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

rows1 = []
rows2 = []
with open('weather.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for line in csvreader:
        rows1.append(line['Градусы'])
        rows2.append(line['Скорость ветра'])
#print(rows1)
#print(rows2)

sum_t = 0
for i in range(-7, 0):
    first_simbol = rows1[i][0]
    digital_t = rows1[i][1:]
    if first_simbol == '+':
        sum_t += int(digital_t)
    elif first_simbol == '-':
        sum_t -= int(digital_t)

middle_t = round((sum_t / 7), 1)
if middle_t > 0:
    middle_t = '+' + str(middle_t)

sum_wind = 0
for i in range(-7, 0):
    sum_wind += int(rows2[i])
middle_wind = round((sum_wind / 7), 1)

dict_middle = {'Средняя температура 7 дней': middle_t, ' Средняя скорость ветра 7 дней': middle_wind}

with open('weather.csv', 'a') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=dict_middle)
    csvwriter.writeheader()
    csvwriter.writerow(dict_middle)
