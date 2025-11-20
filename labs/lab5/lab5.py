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
