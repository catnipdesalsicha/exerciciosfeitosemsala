a = int(input("digite um número inteiro para eu fatorar: "))
fato = a
for i in range (a-1, 0, -1):
    print(a,"X",i)
    fato *= i
    if i == 1:
        print("=", fato)