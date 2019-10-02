def digit_sum(n):
    sum = 0
    while (n > 0):
        n = n / 10
        sum += n
    print sum

print('Введите число')
n = int(input())
print(digit_sum(n))
