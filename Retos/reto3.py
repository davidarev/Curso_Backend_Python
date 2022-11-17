billetes = [5, 10, 20, 50, 100, 200, 500]
total = 0
menu = []
precios = []

num = int(input("¿Cuantos platos quieres introducir? "))
for i in range(num):
    plato = input("Escribe el nombre del plato: ")
    menu.append(plato)
    precio = int(input("Escribe el precio del plato: "))
    precios.append(precio)

print("\n")

cont = 0
while cont < len(menu):
    print(cont + 1, "--", menu[cont], "--", precios[cont], "euros")
    cont += 1

print("\n")

eleccionPlatos = []
eleccionPrecio = []
tecla = 0
while tecla == 0:
    tecla = int(input("¿Que quiere comer? (indiquelo por el numeo del plato) "))
    eleccionPlatos.append(menu[tecla - 1])
    eleccionPrecio.append(precios[tecla - 1])
    tecla = int(input("¿Quiere pedir algo mas? (0: si; 1: no) "))

print("\n")

total = sum(eleccionPrecio)
print("Su pedido es:", eleccionPlatos, "\nPrecio total:", total, "euros")