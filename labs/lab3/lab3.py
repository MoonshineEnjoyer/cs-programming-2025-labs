# Задание 1
name = input("Введи имя: ")
age = input("Введи возраст: ")
for i1 in range(10):
    print("Меня зовут", name, "и мне", age, "лет")
# Задание 2
chislo2 = int(input("Введи число от 1 до 9: "))
if chislo2 <= 1 and chislo2 >= 9:
    print("Число должно быть от 1 до 9!")
elif chislo2 >= 1 and chislo2 <= 9:
    for i2 in range(1, 10):
        print(chislo2, "*", i2, "=", chislo2 * i2)
# Задание 3
for b5 in range(0, 101, 3):
    print(b5)
# Задание 4
chislo4 = int(input("Введи любое целое неотрицательное число: "))
if chislo4 < 0:
    print("Факториал отрицательного числа определить невозможно!")
elif chislo4 > 0:
    for i4 in range(1, chislo4):
        chislo4 *= i4
    print("Факториал введённого числа равен", chislo4)
# Задание 5
chislo5 = 21
while chislo5 > 0:
    chislo5 -= 1
    print(chislo5)
# Задание 6
chislo6 = int(input("Введите любое неотрицательное число: "))
if chislo6 < 0:
    print("Число должно быть неотрицательным!")
elif chislo6 > 0:
    print("Числа Фибоначчи до числа", chislo6)
    a6 = 0
    b6 = 1
    while a6 <= chislo6:
        print(a6)
        a6, b6 = b6, a6 + b6
# Задание 7
stroka7 = input("Введи любую строку: ")
result7 = ''
for i7 in range(len(stroka7)):
    result7 += stroka7[i7] + str(i7 + 1)
print(result7)
# Задание 8
while True:
    chislo8 = input("Введите два числа через пробел: ")
    chislo81, chislo82 = chislo8.split()
    chislo81 = int(chislo81)
    chislo82 = int(chislo82)
    result8 = chislo81 + chislo82
    print("Сумма равна: ", result8)

