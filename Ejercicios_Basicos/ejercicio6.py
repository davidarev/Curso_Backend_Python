#Imprimir números impares en un rango dado.

def impares(begin, end):
    num = begin
    imp = []
    while num <= end:
        if num % 2 == 1: imp.append(num)
        num += 1
    print(imp)

impares(6, 23)