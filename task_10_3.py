"""Из файла, содержащего даты (число, месяц, год), найти самую раннюю дату"""

import csv

fields = ['day', 'month', 'year']

rows = [
    ['01', '08', '1973'],
    ['14', '09', '1957'],
    ['15', '10', '1996'],
    ['03', '03', '2010'],
    ['16', '06', '1988'],
    ['05', '11', '2003'],
    ['17', '12', '1997'],
    ['06', '07', '1967'],
]

with open('my_dates.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

array_days = []
array_months = []
array_years = []
with open('my_dates.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for line in csvreader:
        array_days.append(line['day'])
        array_months.append(line['month'])
        array_years.append(line['year'])

import datetime
import time

date_seconds = []
for i in range(len(array_years)):
    my_date = datetime.date(int(array_years[i]), int(array_months[i]), int(array_days[i]))
    d = time.mktime(my_date.timetuple())
    date_seconds.append(int(d))
#print(min(date_seconds))
#print(datetime.datetime.fromtimestamp(min(date_seconds)))
print('Look file "my_date.csv"')

early_date = {'Earliest date:': datetime.datetime.fromtimestamp(min(date_seconds))}

with open('my_dates.csv', 'a') as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=early_date)
    csvwriter.writeheader()
    csvwriter.writerow(early_date)
