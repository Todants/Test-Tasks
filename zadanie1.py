def right_declension(num):
	dic = {1 : 'компьютер', 2 : 'компьютера', 3 : 'компьютера', 4 : 'компьютера', 5 : 'компьютеров', 6 : 'компьютеров', 7 : 'компьютеров', 8 : 'компьютеров', 9 : 'компьютеров', 0 : 'компьютеров'}
	if 10 < num % 100 < 20:
		return f'{num} компьютеров'
	return f'{num} {dic[num % 10]}'


if __name__ == '__main__':
	for i in range(0, 30):
		print(right_declension(i))
