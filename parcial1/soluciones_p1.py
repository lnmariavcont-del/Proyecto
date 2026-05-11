def f1(func, a, b):
    total = 0
    for i in range(a, b + 1):
        total += func(i) * i
    return total

def f2(L):
    def f(x):
        total = 0
        for i in range(len(L)):
            total += L[i]+(x**i)
        return total
    return f 
    