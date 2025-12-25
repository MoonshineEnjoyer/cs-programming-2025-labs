# 1 Задание
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