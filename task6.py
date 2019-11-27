def get_largest_perimiter(L):
        pmax = 0
        for i in range(len(L)-2):
            for j in range(i,len(L)-1):
                for q in range(j,len(L)):
                    if L[i] + L[j] + L[q] > pmax:
                        pmax = L[i] + L[j] + L[q]
        return pmax
if __name__ == '__main__':
        L = list(map(int, input().split()))
        print(get_largest_perimiter(L))
