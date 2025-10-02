# 1 zadanie
print('1 zadanie--------------')
first = 25
second = 2.5
third = 'Строка'
fourth = False

# 2 zadanie
print('2 zadanie--------------')
myname = 'Danil'
myage = 18
print(myname, myage)

# 3 zadanie
print('3 zadanie--------------')
perv = 342
vtor = 56.2
tret = '43'
summa = perv + vtor + int(tret)
print(summa)

# 4 zadanie
print('4 zadanie--------------')
a = 3
b = 8
ab = (a + 4 * b) * (a - 3 * b) + a**2
print(ab)

# 5 zadanie
print('5 zadanie--------------')
dlina = float(input('Длина: '))
shirina = float(input('Ширина: '))
plos = dlina * shirina
perim = 2 * (dlina + shirina)
print('Площадь: ', plos)
print('Периметр: ', perim)
# 6 zadanie
print('6 zadanie--------------')
print('*', '', '', '*', '', '', '*')
print('', '*', '*', '*', '*', '')
print('', '', '*', '', '*', '', '')

# 7 zadanie
print('7 zadanie--------------')
x = 10
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)
print(x == y)
print(x != y)
print(x < y)
print(x > y)
print(x <= y)
print(x >= y)

# 8 zadanie
print('8 zadanie--------------')
nm = 'Данил'
ag = '18'
print('Меня зовут ', nm, ', мне ', ag, ' лет', sep='')

# 9 zadanie
print('9 zadanie--------------')
c1 = 'Съешь '
c2 = 'ещё '
c3 = 'этих '
c4 = 'мягких '
c5 = 'французских '
c6 = 'булок, '
c7 = 'да '
c8 = 'выпей '
c9 = 'чаю '
c10 = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9
print(c10)

# 10 zadanie
print('10 zadanie--------------')
s1 = 'Нет! Да! '
print(s1 * 4)

# 11 zadanie
print('11 zadanie--------------')
inp1 = input('Ввод трёх чисел чрез запятую: ')
chisla = inp1.split(',')
if len(chisla) != 3:
    print('Нужно ввести ровно три числа!')
else:
    chislo1 = int(chisla[0])
    chislo2 = int(chisla[1])
    chislo3 = int(chisla[2])
    res = (chislo1 + chislo2) // chislo3
    print('Результат вычисления: ', res, ".", sep='')

# 12 zadanie
print('12 zadanie--------------')
inpt = input('Ввод слова с не менее 10 символами: ')
if len(inpt) <= 10:
    print('В введённом слове менее 10 символов.')
else:
    print(inpt[:4])
    print(inpt[-2:])
    print(inpt[4:8])
    print(inpt[::-1])

