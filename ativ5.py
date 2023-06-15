count1 = 0
count2 = 0
count3 = 0
par = 0
total = 0
num = (float(input("digite um número positivo(0 encerra o programa): ")))
while num >0:
    if (num%2) == 0:
        par +=num
        count1 += 1
    else:
        count2 += 1
    count3 +=1
    total += num
    num = (float(input("digite um número positivo(0 encerra o programa): ")))
print("números pares: ", count1)
print("números ímpares: ", count2)
print("média total: ", total/count3)
print("média de pares: ", par/count1)