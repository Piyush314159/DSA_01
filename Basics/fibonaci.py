def fibonaci(n):
    res = [0,1]
    for i in range(n-2):
        res.append(res[-1] + res[-2])
    return res

print(fibonaci(8))