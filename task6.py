def get_largest_perimiter(arr):
	maxi = 0
	n = len(arr) 
	for i in range(n - 2): 
		for j in range(i + 1, n - 1): 
			for k in range(j + 1, n): 
				a = arr[i] 
				b = arr[j] 
				c = arr[k] 
				if(a < b + c and b < a + c and c < a + b): 
					maxi = max(maxi, a + b + c) 

	if(maxi == 0): 
		return "Triangle formation is not possible"
	else: 
		return "Maximum Perimeter is: "+ str(maxi) 

L = list(map(int, input().split()))
print(get_largest_perimiter(L))
