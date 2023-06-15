##desenvolva um algoritmo que efetue a soma de todos os números
##ímpares que são múltiplos de 2 a partir de 1-500

soma = 0

for i in range (1,501):
    if i % 2 == 1 and i % 3 == 0:
        soma = soma + 1
print(soma)