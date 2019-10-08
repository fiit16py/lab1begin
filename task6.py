def check_triangle(a, b, c):
        if a + b > c and a + c > b and b + c > a:
                return True
        else:
                return False

def get_largest_perimiter(L):
        l = list(L)
        P = 0
        for a in range(len(l)):
                for b in range(a + 1, len(l)):
                        for c in range(b + 1, len(l)):
                                if check_triangle(l[a], l[b], l[c]):
                                        if P < (l[a] + l[b] + l[c]):
                                                P = l[a] + l[b] + l[c]
        return P

L = map(int, input().split())
print(get_largest_perimiter(L))
