def piramide(num):
    for a in range (1, num+1):
        for b in range (1, a+1):
            print(a, end = " ")
        print()
def piramide2(num):
    for a in range(1, num+1):
        for b in range(1, a+1):
            print(b, end = " ")
        print()
def vogais(num):
    cont = 0
    for a in num:
        if a in "aeiouAEIOU":
            cont += 1
    print(f"O texto digitado possui {cont} vogais")
