def is_power_of_two(n):
	while n > 2:
		if n % 2 == 0:
			n = n / 2
		else:
			return 'false'
	return 'true'
n = int(input())
print(is_power_of_two(n))
