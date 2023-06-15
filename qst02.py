#desenvolva um algoritmo que leia a altura de 15 pessoas
##calcule  a menor e a maior altura do grupo

alturas = []

for i in range(1,16):
    altura = float(input("Digite a altura da pessoa: "))
    alturas.append(altura)

    menor_alt = min(alturas)
    maior_alt = max(alturas)

    print("A maior altura é: ", maior_alt)
    print("A menor altura é: ", menor_alt)