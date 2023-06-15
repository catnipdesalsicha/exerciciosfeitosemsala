num = 0.0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
num = float(input("digite um número: "))
while num >= 0:
    if num >= 0 and num <= 25:
        count1 += 1
    elif num >= 26 and num <= 50:
        count2 += 1
    elif num >= 51 and num <= 75:
        count3 += 1
    elif num >= 76 and num <= 100:
        count4 += 1
    else:
        count1 = count1
    num = float(input("digite um número: "))
    
print("%g número(s) estão entre 0 e 25. %g número(s) estão entre 26 e 50. %g número(s) estão entre 51 e 75. %g número(s) estão entre 76 e 100" %(count1, count2, count3, count4))