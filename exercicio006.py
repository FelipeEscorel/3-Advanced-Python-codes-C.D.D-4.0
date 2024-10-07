numeros = [0]*10
tam = len(numeros)
cont1 = 11
cont2 = 0
for a in range(tam):
    cont1 -= 1
    numeros[a] = int(input(f"Digite {cont1} número(s): "))
num = int(input("Digite mais 1 número: "))
for b in range(tam):
    if num == numeros[b]:
        cont2 += 1
print(cont2)
