def is_beautiful(n):
    s=0
    a=n
    while(n//10>0):
        s=s+n%10
        n=n//10
    s=s+n
    if(a%s==0):
        return True
    else:
        return False

n = int(input())
print(is_beautiful(n))
