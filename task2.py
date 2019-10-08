def digit_sum(n):
    a=0
    while n!=0:
        a=a+n%10
        n=n/10
    return a

print('Введите число')
n = int(input())
print(digit_sum(n))
