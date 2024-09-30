notas = ["", "", "", "", ""]
soma = 0
cont = 0
media = 0
tamanho = len(notas)
for a in range(tamanho):
    notas[a] = float(input("Digite os nomes dos 5 alunos: "))
    soma = soma + notas[a]
    media = soma / tamanho
print(f"\nA soma das notas dos alunos é {soma} e a média da turma é de {media}")
