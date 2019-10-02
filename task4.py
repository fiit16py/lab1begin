def is_power_of_two(n):
	while(True):
		if n == 2:
			return True
		if n % 2 == 1:
			return False
		n /= 2
	pass

n = int(input())
print(is_power_of_two(n))
