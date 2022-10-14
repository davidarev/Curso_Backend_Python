#Cuenta regresiva hasta cero a partir de un número dado, def cuenta_atras(num)

def cuenta_atras(num):
    while num >= 0:
        print(num, end = ", ")
        num -= 1
    print("BOOOOM!!!")

cuenta_atras(10)