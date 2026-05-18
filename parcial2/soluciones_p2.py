def G1():
    a, b, c = 1, 1, 1
    yield a
    yield b
    yield c
    while True:
        nuevo = a + b + c
        yield nuevo
        a = b
        b = c
        c = nuevo

def tresfibonacci(n):
    a,b,c = 1, 1, 1
    for i in range(n):
        yield a
        nuevo = a+b+c
        a=b
        b=c
        c= nuevo
