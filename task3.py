def is_beautiful(n):
	cash = n
	s = 0
	while n > 0:
		s = s + n % 10
		n = n // 10
	if cash % s == 0:
		return 'true'
	else: 
		return 'false'
n = int(input())
print(is_beautiful(n))
