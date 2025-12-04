# 1 Задание
task1 = [10, 52, 131, 332, 3, 547, 343, 3212, 23234, 443]
check1 = 0
for subtask1 in task1:
    check1 += 1
    if subtask1 == 3:
        task1[check1 - 1] = 30
        print(task1)
# 2 Задание
task2 = [50, 20, 10, 25, 30]
otvet2 = []
for subtask2 in task2:
    subtask2 = subtask2**2
    otvet2.append(subtask2)
print(otvet2)
# 3 Задание
task3 = [2424, 2103, 2320, 2, 74, 85, 36, 4421, 424, 5]
max3 = max(task3)
delit3 = len(task3)
otvet3 = max3 / delit3
print(otvet3)
# 4 Задание
try:
    task4 = (3, 1, 2, "adada")
    print(tuple(sorted(task4)))
except TypeError:
    print(task4)
# 5 Задание
task5 = {"Предмет1": 560, "Предмет2": 10, "Предмет3": 40}
maxstr5 = max(task5, key=task5.get)
maxint5 = task5[maxstr5]
minstr5 = min(task5, key=task5.get)
minint5 = task5[minstr5]
print("Самый дорогой предмет:", maxstr5, "-", maxint5)
print("Самый дешёвый предмет:", minstr5, "-", minint5)
# 6 Задание
task6 = ['a', 'b', 'c', 'd', 'e']
task6dict = {key: key for key in task6}
print(task6dict)
# 7 Задание
task7 = {'Ассистент': 'Assistant', 'Станция': 'Station', 'Клоун': 'Clown', 'Предатель': 'Traitor'}
inp7 = input('Введите слово на русском с большой буквы для перевода на английский: ')
if inp7 in task7:
    print('Перевод', inp7, 'на английский -', task7[inp7])
else:
    print('К сожалению, перевода для данного слова нет!')
# 8 Задание
import random

inp8list = ["камень", "ножницы", "бумага", "ящерица", "спок"]
rules8 = {
    "камень": ["ножницы", "ящерица"],
    "ножницы": ["бумага", "ящерица"],
    "бумага": ["камень", "спок"],
    "ящерица": ["спок", "бумага"],
    "спок": ["ножницы", "камень"],
}
inp8 = input("Введите свой выбор: 'камень', 'ножницы', 'бумага', 'ящерица', 'спок': ")
randinp8 = random.choice(inp8list)
if inp8 == randinp8:
    print("Ничья. Ваш выбор: ", inp8, "; выбор компьютера: ", randinp8, sep="")
elif randinp8 in rules8[inp8]:
    print("Вы победили. Ваш выбор: ", inp8, "; выбор компьютера: ", randinp8, sep="")
else:
    print("Вы проиграли. Ваш выбор: ", inp8, "; выбор компьютера: ", randinp8, sep="")
# 9 Задание
list9 = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]
dict9 = {}
for a9 in list9:
    letter9 = a9[:1]
    if letter9 not in dict9:
        dict9[letter9] = []
    dict9[letter9].append(a9)
print(dict9)
# 10 Задание
task10 = [
    ("Анна", [5, 4, 5, 4, 3]),
    ("Иван", [3, 4, 4, 2, 5]),
    ("Мария", [5, 3, 5, 2, 4]),
]
dict10 = {}
for tpls10 in task10:
    name10 = tpls10[0]
    marks10 = tpls10[1]
    avgmarks10 = sum(marks10) / len(marks10)
    dict10[name10] = avgmarks10
    highmarks10 = max(dict10, key=dict10.get)
print(highmarks10, "имеет наивысший средний балл:", dict10[highmarks10])
