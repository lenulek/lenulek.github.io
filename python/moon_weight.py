import sys
def moon_weight():
	print('What is your weight?')
	weight = int(sys.stdin.readline())
	print('What is your average weight change per year?')
	wyearly_change = float(sys.stdin.readline())
	print('How many years do you want to count?')
	years_qty = int(sys.stdin.readline())
	year = 2019
	for i in range(0,years_qty):
		my_moonweight = (weight + wyearly_change) * 0.165
		print('my weight in %s on the moon = %s' %(year, my_moonweight))
		year = year + 1
		weight = weight + 1
moon_weight()
