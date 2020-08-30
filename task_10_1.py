"""Создать csv файл с данными. Создать отчетный файл с информацией по количеству
людей входящих в ту или иную возрастную группу: 1-12, 13-18, 19-25, 26-40, 40+."""

import csv

fields = ['firstname', 'lastname', 'age']
rows = [
    ['Max', 'Petrov', 25],
    ['Alex', 'Sidorov', 50],
    ['Piter', 'Ivanov', 16],
    ['Nick', 'Parker', 32],
    ['Tom', 'Soer', 5],
    ['Katya', 'Sokolova', 27],
    ['Helen', 'Sonik', 18],
]

filename = "age_group.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

rows1 = []
with open('age_group.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for line in csvreader:
        rows1.append(line['age'])

b = c = d = h = g = 0
for i in rows1:
    i = int(i)
    if 0 < i <= 13:
        b += 1
    elif 13 < i <= 19:
        c += 1
    elif 19 < i <= 26:
        d += 1
    elif 26 < i <= 40:
        h += 1
    elif i > 40:
        g += 1
    else:
        print('Write right age')


fields1 = ['1-12', ' 13-18', ' 19-25', ' 26-40', ' 40+']
row_num = [str(b), str(c), str(d), str(h), str(g)]

filename = "result_groups.csv"
with open(filename, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(fields1)
    writer.writerow(row_num)


