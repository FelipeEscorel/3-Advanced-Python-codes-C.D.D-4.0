user = [""]*5
senha = [""]*5
cont = 0
tamUser = len(user)

for a in range(tamUser):
    user[a] = input("Digite seu nome: ")
    senha[a] = input("Digite senha: ")
for b in range(tamUser):
    cont += 1
    print(f"{cont}° Usuário: {user[b]} (Posição: {b})/ Senha: {senha[b]} (Posição: {b})")
