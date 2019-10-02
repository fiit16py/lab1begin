def is_power_of_two(n):
	while True:
		if n % 2 != 0:
			return False
		if n == 1:
			break
		n = n / 2
	return True
n = int(input())
print(is_power_of_two(n))
