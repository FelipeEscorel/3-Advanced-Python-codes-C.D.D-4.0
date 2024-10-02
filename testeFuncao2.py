def piramide(num):
    for a in range (1,num+1):
        for b in range (1, a+1):
            print(a, end = " ")
        print()
num = int(input("Digite um número: "))
piramide(num)
