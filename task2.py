def digit_sum(n):
    sum = 0
    l = list(str(n))
    for i in n:
        sum += int(i)
    return sum

print('Введите число')
n = int(input())
print(digit_sum(n))
