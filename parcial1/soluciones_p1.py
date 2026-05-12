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
def f3(x0, y0):
    def recta(x):
        return 2 * x - 2 * x0 + y0
    def paralela(x):
       return 2 * x - 1
    return recta, paralela

    