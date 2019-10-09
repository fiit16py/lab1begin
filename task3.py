def is_beautiful(n):
	summ=0
	r=n
	while r!=0:
		summ=summ+r%10
		r=r//10
	if n%summ==0:
		return 'true'
	else:
		return 'false'

n = int(input())
print(is_beautiful(n))
