idades = []
soma = 0
media = 0
count = 0

for i in range (10):
    idades.append(int(input("Digite uma idade: ")))
    soma=soma +idades[i]
    if idades [i] >=30:
        count = count+1

media = soma /10

print(media)
print(count)