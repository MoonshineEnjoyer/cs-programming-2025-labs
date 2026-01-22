# 1 Задание
objects = [
    ("Containment Cell A", 4),
    ("Archive Vault", 1),
    ("Bio Lab Sector", 3),
    ("Observation Wing", 2)
]
print(sorted(objects, key=lambda x: x[1]))

# 2 Задание
staff_shifts = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
]
y = list(map(lambda x: x["shift_cost"] * x["shifts"], staff_shifts))
print(y)
print(max(y))

# 3 Задание
personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]
new = list(map(lambda x: {**x, "category": "Restricted" if x["clearance"] == 1 
                  else "Confidential" if 2 <= x["clearance"] <= 3 
                  else "Top Secret"}, personnel))
print(new)

# 4 Задание
zones = [
    {"zone": "Sector-12", "active_from": 8, "active_to": 18},
    {"zone": "Deep Storage", "active_from": 0, "active_to": 24},
    {"zone": "Research Wing", "active_from": 9, "active_to": 17}
]
print(list(filter(lambda x: x["active_from"] <= 8 and x["active_to"] >= 18, zones)))

# 5 Задание
import re
reports = [
    {"author": "Dr. Moss", "text": "Analysis completed. Reference: http://external-archive.net"},
    {"author": "Agent Lee", "text": "Incident resolved without escalation."},
    {"author": "Dr. Patel", "text": "Supplementary data available at https://secure-research.org"},
    {"author": "Supervisor Kane", "text": "No anomalies detected during inspection."},
    {"author": "Researcher Bloom", "text": "Extended observations uploaded to http://research-notes.lab"},
    {"author": "Agent Novak", "text": "Perimeter secured. No external interference observed."},
    {"author": "Dr. Hargreeve", "text": "Full containment log stored at https://internal-db.scp"},
    {"author": "Technician Moore", "text": "Routine maintenance completed successfully."},
    {"author": "Dr. Alvarez", "text": "Cross-reference materials: http://crosslink.foundation"},
    {"author": "Security Officer Tan", "text": "Shift completed without incidents."},
    {"author": "Analyst Wright", "text": "Statistical model published at https://analysis-hub.org"},
    {"author": "Dr. Kowalski", "text": "Behavioral deviations documented internally."},
    {"author": "Agent Fischer", "text": "Additional footage archived: http://video-storage.sec"},
    {"author": "Senior Researcher Hall", "text": "All test results verified and approved."},
    {"author": "Operations Lead Grant", "text": "Emergency protocol draft shared via https://ops-share.scp"}
]
new = list(filter(lambda x: x, [{**y, "text": re.sub(r'https?://\S+', '[ДАННЫЕ УДАЛЕНЫ]', y['text'])} 
     for y in reports]))
print(new)

# 6 Задание
scp_objects = [
    {"scp": "SCP-096", "class": "Euclid"},
    {"scp": "SCP-173", "class": "Euclid"},
    {"scp": "SCP-055", "class": "Keter"},
    {"scp": "SCP-999", "class": "Safe"},
    {"scp": "SCP-3001", "class": "Keter"}
]
print(list(filter(lambda x: x["class"] != "Safe", scp_objects)))

# 7 Задание
incidents = [
    {"id": 101, "staff": 4},
    {"id": 102, "staff": 12},
    {"id": 103, "staff": 7},
    {"id": 104, "staff": 20}
]
print(sorted(incidents, key=lambda x: -x["staff"])[:3])

# 8 Задание
protocols = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
]
print(list(map(lambda x: f"Protocol {x[0]} - Criticality {x[1]}", protocols)))

# 9 Задание
shifts = [6, 12, 8, 24, 10, 4]
print(list(filter(lambda x: 8 <= x <= 12, shifts)))

# 10 Задание
evaluations = [
    {"name": "Agent Cole", "score": 78},
    {"name": "Dr. Weiss", "score": 92},
    {"name": "Technician Moore", "score": 61},
    {"name": "Researcher Lin", "score": 88}
]
best = max(evaluations, key=lambda x: x["score"])
print(f"{best['name']} - {best['score']}")

value1 = int(input('Введите количество времени: '))
from1 = input('Введите единицу измерения введёного времени (s, m, h, d): ')
to1 = input('Введите, в какую единицу измерения времени нужно преобразовать (s, m, h, d): ')
def convert1(value1, from1, to1):
    if from1 == 's':
        seconds = value1
    elif from1 == 'm':
        seconds = value1 * 60
    elif from1 == 'h':
        seconds = value1 * 3600
    elif from1 == 'd':
        seconds = value1 * 86400
    if to1 == 's':
        res = seconds
    elif to1 == 'm':
        res = seconds / 60
    elif to1 == 'h':
        res = seconds / 3600
    elif to1 == 'd':
        res = seconds / 86400
    if res == int(res):
        return int(res)
    else:
        return round(res, 6)
print(convert1(value1, from1, to1), to1)
# 2 Задание
value2 = int(input('Введите сумму вклада (минимально: 30000): '))
time2 = int(input('Введите время вклада (в годах): '))
def convert2(value2, time2):
    if value2 < 30000:
        return 0
    answer2 = 0
    base2 = min(0.003 * (value2 // 10000), 0.05)
    for i2 in range(time2):
        if i2 <= 2:
            rate2 = 0.03
        elif i2 < 6:
            rate2 = 0.05
        else:
            rate2 = 0.02
        percents2 = value2 * ((base2 + rate2))
        answer2 += percents2
        value2 += percents2
    return answer2
print(convert2(value2, time2))
# 3 Задание
try:
    x3 = int(input('Введите число, являющееся началом диапазона: '))
    y3 = int(input('Введите число, являющееся концом диапазона: '))
    if x3 > y3:
        print('Ошибка: начало диапазона больше его конца!')
    else:
        def isprime(x3, y3):
            m3 = []
            for i3 in range(x3, y3 + 1):
                if i3 > 1:
                    is_prime = True
                    for i31 in range(2, int(i3 ** 0.5) + 1):
                        if i3 % i31 == 0:
                            is_prime = False
                            break
                    if is_prime:
                        m3.append(i3)
            return m3
        print(isprime(x3, y3))
except ValueError:
    print('Нужно ввести целое число!')
# 4 Задание
n = int(input('Введите размер n складываемых квадратных матриц n * n: '))
first = [list(map(int, input('Введите строку первой матрицы (числами через пробел): ').split())) for x in range(n)]
second = [list(map(int, input('Введите строку второй матрицы (числами через пробел): ').split())) for x in range(n)]
if any(len(row) != n for row in first + second):
    print("Ошибка: не все введённые матрицы являются квадратными!")
else:
    print('Получившаяся матрица равна: ')
    for i in range(n):
        for j in range(n):
            print(first[i][j] + second[i][j], end=" ")
        print()
# 5 Задание
text5 = input('Введите текст для проверки на палиндром: ')
def check5(text5):
    symb5 = ' !?,.;\\\:"-_'''
    clean5 = ""
    for i5 in text5:
        if i5 not in symb5:
            clean5 += i5.lower()
    return "Да" if clean5 == clean5[::-1] else "Нет"
print(check5(text5))
>>>>>>> 31c54a002a155cbeb817e9d131d55c383ff95d74
