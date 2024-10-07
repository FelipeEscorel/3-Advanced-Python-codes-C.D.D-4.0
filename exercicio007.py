nomes = [""]*5
tam = len(nomes)
cont1 = tam + 1
for a in range(tam):
    cont1 -= 1
    nomes[a] = input(f"Digite o {cont1}° nome: ")
print(nomes)
for b in range(tam-1, -1, -1):
    print(nomes[b])
