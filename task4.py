def is_power_of_two(n):
	if n == 0:
		return False
	elif n & (n - 1) == 0:
		return True
	else:
		return False


n = int(input())
print(is_power_of_two(n))
