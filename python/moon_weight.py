import sys
def moon_weight():
	print('Введите ваш нынешний земной вес')
	weight = int(sys.stdin.readline())
	print('Введите ежегодный прирост вашего веса')
	wyearly_change = float(sys.stdin.readline())
	print('Введите количество лет для расчёта')
	years_qty = int(sys.stdin.readline())
	year = 2019
	for i in range(0,years_qty):
		my_moonweight = (weight + wyearly_change) * 0.165
		print('my weight in %s on the moon = %s' %(year, my_moonweight))
		year = year + 1
		weight = weight + 1
moon_weight()
