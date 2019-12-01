print('Шуточный стишок')
print()
found_coins = 20
print('''Я по улице шёл
И монетки нашёл.
Сколько их будет в кармане теперь бряцать?
-  %s ''' % found_coins)
print()
print('/пошёл домой с монетками/')
print()
magic_coins = 10
print('''Что в подвале спрятал дед?
Что за агрегат такой?
Он как принтер 3D.
Вдруг и монетки он удвоит???''')
print()
print('/положил монетки в агрегат/')
print()
print('''Эх... не вдвое, ну и что ж?!
Этот результат тоже хорош!
Так за раз монеток %s
Можно много их наделать!''' % magic_coins)
days_in_week = 7
magcoins_inweek = magic_coins * days_in_week
print('''Дней в неделе целых %s
Рад я этому совсем!
За неделю агрегат
Даст мне прибыль в %s''' % (days_in_week, magcoins_inweek))
print()
print('/улыбается/')
print()
print('/в воскресенье прилетает ворона/')
print()
stolen_coins = 3
print('''Ай-я-яй! Ты посмотри:
Эта гадкая ворона
Прилетела из-за забора
И утащила монетки %s''' % stolen_coins)
print()
print('''Раз в неделю так таскать,
Сколько ж можно потерять?
Посчитаю наперёд,
Сколько минусов за год.''')
print()
coins = found_coins
for week in range (1, 53):
    coins = coins + magcoins_inweek - stolen_coins
    print('Неделя %s = %s денежек' % (week, coins))
print()
print('''Если б чучело поставить,
Чтоб ворону напугать.
Заработал бы я больше.
Сколько? - Надо посчитать!''')
print()
coins = found_coins
for week in range (1, 53):
    coins = coins + magcoins_inweek
    print('Неделя %s = %s денежек' % (week, coins))

print()
print('''Вот так был бы я богат,
Если бы не этот гад.''')
