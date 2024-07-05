def bubble(ar):
    n = len(ar)
    for i in range(n-1):
        for j in range(n-i-1):
            if ar[j] > ar[j+1] :
                ar[j], ar[j+1] = ar[j+1], ar[j]
    return ar
print(bubble([6,3,2,5]))