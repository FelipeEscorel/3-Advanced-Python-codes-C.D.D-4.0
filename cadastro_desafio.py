user = [""]*5
password = [""]*5
cont = 0
cont2 = 0
tent = 0
tamUser = len(user)
num = 0

while num != 4 and cont2 == 0:
    num = int(input("O que você deseja fazer?\n1 - Cadastro de usuários\n2 - Login\n3 - Mostrar usuários\n4 - Sair\n"))
    if num == 1:
        for a in range(tamUser):
            user[a] = input(f"Cadastre o nome do usuário: ")
            password[a] = input("Cadastre a senha (Apenas números inteiros): ")
            print()
    elif num == 2:
        cont = 0
        cont += 1
        usuario = input("Digite o nome do usuário: ")
        for b in range(tamUser):
            if usuario == user[b]:
                senha = input("Digite a senha: ")
                print()
                if senha == password[b]:
                    print("Login efetuado!\n")
                    cont2 += 4
                while senha != password[b] and tent < 2:
                    print("Senha inválida!\n")
                    senha = input("Digite a senha novamente: ")
                    tent += 1
                    if tent == 2 and senha != password[b]:
                        print("Limite de tentativas excedido. Tente novamente mais tarde!")
                        cont2 += 4
                    elif senha == password[b]:
                        print("Login efetuado!\n")
                        cont2 += 4
        if usuario not in user:
            print("Usuário não cadastrado.\n")
    elif num == 3:
        print("Usuários cadastrados: ")
        cont = 0
        for c in range(tamUser):
            cont+=1
            print(f"{cont}º Usuário: {user[c]}")
    elif num == 4:
        print("Fim do programa")
    else:
        print("Função não disponível.\n")
print()
print("Usuários cadastrados:")
print(user)
print("Senhas cadastradas(respectivamente):")
print(password)