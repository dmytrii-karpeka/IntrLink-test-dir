import csv

start_array = []
with open('acme_worksheet.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        start_array.append(row) # Утворення двовимірного масиву

start_array = start_array[1:] # прибрав headers інформації, адже у вихідному файлі вони будуть іншими

names = []
dates = []
for info in start_array:
    # Помітив, що на кожну дату є однакова кількість записів про робочі години робітників.
    # Тому при першому проходженню по масиву інформації я виділив імена які зустрічаються в перший день
    # (та зустрічатимуться в тому ж порядку в усі наступні дні)
    if info[1] == start_array[0][1]:
        names.append(info[0])
    dates.append(info[1])


dates = list(set(dates)) # Зібрано унікальні дати. Вони будуть headers таблиці

# Починаємо формувати таблицю
end_array = [["Employee Name/Date"] + dates]

for name in names:
    list = [name]
    for date in dates:
        for info in start_array:
            if name == info[0] and date == info[1]:
                list.append(info[2])

    end_array.append(list)

with open('result.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(end_array)
