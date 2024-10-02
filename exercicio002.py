notas = ["", "", "", "", ""]
soma = 0
cont = 0
media = 0
tamanho = len(notas)
for a in range(tamanho):
    notas[a] = float(input("Digite as notas dos 5 alunos: "))
for b in range(tamanho):
    soma = soma + notas[b]
    media = soma / tamanho
print(f"\nA soma das notas dos alunos é {soma} e a média da turma é de {media}. ")
for c in range(tamanho):
    if notas[c] > media:
        cont+=1
print(f"{cont} alunos tiveram a nota maior que a média.")
