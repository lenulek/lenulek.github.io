'''Среди натуральных чисел, которые были введены, найти наибольшее
    по сумме цифр. Вывести на экран это число и сумму его цифр.'''

def digitsum(num):
    i = 10 ** (len(str(num)) - 1)
    s = 0
    j = 0
    while num > 0:
        j = num // i
        num = num - j * i
        s += j
        i /= 10
    return int(s)

# print(digitsum(4231))

a = int(input('Введите целое число a: '))
b = int(input('Введите целое число b: '))

if digitsum(a) > digitsum(b):
    print(f'Число с наибольшей суммой цифр = {a}')
    print(f'Сумма его цифр = {digitsum(a)}')
elif digitsum(a) == digitsum(b):
    print(f'Сумма цифр у введенных чисел одинаковая = {digitsum(b)}')
else:
    print(f'Число с наибольшей суммой цифр = {b}')
    print(f'Сумма его цифр = {digitsum(b)}')
