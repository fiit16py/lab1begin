def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	elif n % 2 == 0:
		return False
	else:
		s = 2
		while s < n:
			if n % s == 0:
				return False
			s += 1
		return True


n = int(input())
print(is_prime(n))
