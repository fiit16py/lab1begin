def is_power_of_two(n):
	while n%2==0:
		if n//2==1:
			return 'true'
		n=n/2
	return 'false'

n = int(input())
print(is_power_of_two(n))
