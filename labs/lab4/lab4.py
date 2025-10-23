# 1 Задание
temp = int(input("Ввод температуры для кондиционера: "))
if temp >= 20:
    print("Кондиционер выключен")
else:
    print("Кондиционер включен")
# 2 Задание
inp2 = int(input("Введите номер месяца: "))
if inp2 == 1 or inp2 == 2 or inp2 == 12:
    print("Это зима")
if inp2 == 3 or inp2 == 4 or inp2 == 5:
    print("Это весна")
if inp2 == 6 or inp2 == 7 or inp2 == 8:
    print("Это лето")
if inp2 == 9 or inp2 == 10 or inp2 == 11:
    print("Это осень")
# 3 Задание
inp3 = input("Введите возраст собаки (в годах): ")
try:
    if int(inp3) == 1:
        print("Возраст собаки в человеческих годах: 10.5")
    elif int(inp3) > 1 and int(inp3) <= 22:
        age3 = (10.5 * 2) + ((int(inp3) - 2) * 4)
        print("Возраст собаки в человеческих годах:", age3)
    elif int(inp3) < 1:
        print("Ошибка: число должно быть не меньше 1")
    elif int(inp3) > 22:
        print("Ошибка: число должно быть не больше 22")
    else:
        print("Ошибка: введите число")
except ValueError:
    print("Ошибка: введите число")
# Задание 4
inp4 = input("Введите число: ")
last41 = inp4[-1]
cifri = [int(cifra) for cifra in inp4]
sumc = sum(cifri)
if int(last41) % 2 == 0 and int(sumc) % 3 == 0:
    print("Введённое число делится на 3")
else:
    print("Введённое число не делится на 3")
# Задание 5
inp5 = input("Введите пароль: ")
errors = []
if len(inp5) < 8: errors.append("длина менее 8 символов")
if not any(c.isupper() for c in inp5): errors.append("отсутствуют заглавные буквы")
if not any(c.islower() for c in inp5): errors.append("отсутствуют строчные буквы")
if not any(c.isdigit() for c in inp5): errors.append("отсутствуют числа")
if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?`~" for c in inp5): errors.append("отсутствуют специальные символы")
if errors:
    print("Пароль ненадежный: ", ", ".join(errors))
else:
    print("Пароль надежный!")
# Задание 6
inp6 = int(input("Введите год: "))
if (inp6 % 4 == 0 and inp6 % 100 != 0) or (inp6 % 400 == 0):
    print(inp6, '- високосный год')
else:
    print(inp6, '- не високосный год')
# Задание 7
chislo1, chislo2, chislo3 = map(int, input("Введите три числа: ").split())
if chislo1 <= chislo2 and chislo1 <= chislo3:
    menshee = chislo1
if chislo2 <= chislo1 and chislo2 <= chislo3:
    menshee = chislo2
if chislo3 <= chislo1 and chislo3 <= chislo2:
    menshee = chislo3
print("Наименьшее число: ", menshee)
# Задание 8
inp8 = int(input("Введите сумму покупки: "))
if inp8 < 1000:
    print("Ваша скидка: 0%")
    print("К оплате: ", (inp8 * 1))
if inp8 >= 1000 and inp8 <= 4999:
    print("Ваша скидка: 5%")
    print("К оплате: ", (inp8 * 0.95))
if inp8 >= 5000 and inp8 <= 9999:
    print("Ваша скидка: 10%")
    print("К оплате: ", (inp8 * 0.9))
if inp8 > 10000:
    print("Ваша скидка: 15%")
    print("К оплате: ", (inp8 * 0.85))
# Задание 9
inp9 = int(input("Введите час (0-23): "))
if inp9 >= 0 and inp9 <= 5:
    print("Сейчас ночь")
if inp9 >= 6 and inp9 <= 11:
    print("Сейчас утро")
if inp9 >= 12 and inp9 <= 17:
    print("Сейчас день")
if inp9 >= 18 and inp9 <= 23:
    print("Сейчас вечер")
# Задание 10


