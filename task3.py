def is_beautiful(n):
        s=0
        e=n
        while n>0:
                a=n%10
                s=s+a
                n//=10
        if e%s==0:
                print('true')
        else: print('false')
n = int(input())
print(is_beautiful(n))
