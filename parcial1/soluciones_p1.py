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

def f4(L):
    total = 0
    for n in L:
        if n > 10:
            digitos = str(n)
            primer_digito = int(digitos[0])
            ultimo_digito  = int(digitos[-1])
            if (primer_digito + ultimo_digito) % 2 == 0:
                total += n
    return total



    