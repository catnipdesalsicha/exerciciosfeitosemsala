##desenvolva um algoritmo que leia um número indeterminado de valores
##calcule e escreva a média aritmetica dos valores lidos, a quantia
##de valores positivos e negativos, além do percentual de valores negativos
##e positivos

valores = []
num_p = 0
num_n = 0

while True:
    valor = float(input("Digite um número (digitar 0 irá interromper o programa): "))
    if valor == 0:
        exit
    valores.append(valor)
    if valor >0:
        num_p = num_p + 1
    if valor <0:
        num_n = num_n + 1

soma = sum(valores)
media = soma / len(valores)

total_valores = len(valores)
perc_n = (num_n / total_valores) * 100
perc_p = (num_p / total_valores) * 100

print("Média aritmética: ", media)
print("Quantidade de valores positivos:", num_p)
print("Quantidade de valores negativos:", num_n)
print("Percentual de valores positivos:", perc_p)
print("Percentual de valores negativos:", perc_n)