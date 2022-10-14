import math

def sumar(a, b): return a + b

def restar(a, b): return a - b

def doblar(a): return a * 2

def multiplicar(a, b): return a * b

def dividir(a, b): return a / b

def cuadrado(a): return a ** 2

def raiz(a): return math.sqrt(a)

def es_par(a):
    if a % 2 == 0: return 1
    else: return 0

if __name__ == "__main__":
    print(sumar(15, 5))
    print(doblar(5))
    print(es_par(6))
    print(cuadrado(5))
    print(raiz(49))