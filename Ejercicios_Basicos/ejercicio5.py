#N numeros de la serie de Fibonacci:

def Fibonacci(N):
    numeros = []
    num1 = 0
    num2 = 1
    cont = 0
    while cont < N:
        num3 = num1 + num2
        numeros.append(num3)
        num1 = num2
        num2 = num3
        cont += 1
    print(numeros)


Fibonacci(8)
