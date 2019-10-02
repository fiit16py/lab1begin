def is_triangle(a, b, c):
        if a + b > c and a + c > b and c + b > a:
                return True
        else:
                return False

        
def get_largest_perimiter(L):
        largest_p = 0
        for a in L:
                for b in L:
                        for c in L:
                                if is_triangle(a, b, c):
                                        p = (a + b + c) / 2
                                        if p > largest_p:
                                                largest_p = p
        return largest_p

L = map(int, input().split())
print(get_largest_perimiter(L))
