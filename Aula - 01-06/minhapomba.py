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

#-----------------------


salarios = []
count_e = 0
count_j = 0
count_s = 0
count_p = 0

for i in range (15):
    salarios.append(float(input("Digite um salário: ")))
    if salarios[i]>=500 and salarios[i]<=1000:
        count_e = count_e + 1
    elif salarios[i]>=1001 and salarios[i]<=2500:
        count_j = count_j + 1
    elif salarios[i]>=2501 and salarios[i]<=4500:
        count_s= count_s +1
    elif salarios[i]>=4501 and salarios[i]<=10000:
        count_p= count_p + 1
    else:
        print("Salários esquisito")
    
print(count_e)
print(count_j)
print(count_s)
print(count_p)
