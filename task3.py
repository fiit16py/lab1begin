def digit_sum(n):
    sum = 0
    l = list(str(n))
    for i in l:
        sum += int(i)
    return sum

def is_beautiful(n):
	return n % digit_sum(n) == 0

n = int(input())
print(is_beautiful(n))
