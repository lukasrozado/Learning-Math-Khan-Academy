# Learn to organize data into frequency tables and dot plots (sometimes called line plots).

print("Age of Students in class")
# FREQUENCY TABLE
age = (5,7,5,9,7,7,6,9,9,9,10,12,12,7)
range_age = max(age) - min(age)
age2 = {}
cont1 = cont2 = cont3 = cont4 = cont5 = cont6 = cont7= cont8= cont9 = cont10 = cont11 = cont12 = cont13 = cont14 = cont15 = cont16 = cont17 = cont18 = cont19 = cont20 = 0

for num in range(0,len(age)):
    if age[num] == 1:
        cont1 += 1
    if age[num] == 2:
        cont2 += 1
    if age[num] == 3:
        cont3 +=1
    if age[num] == 4:
        cont4 += 1
    if age[num] == 5:
        cont5 += 1
    if age[num] == 6:
        cont6 += 1
    if age[num] == 7:
        cont7 += 1
    if age[num] == 8:
        cont8 += 1
    if age[num] == 9:
        cont9 += 1
    if age[num] == 10:
        cont10 += 1
    if age[num] == 11:
        cont11 += 1
    if age[num] == 12:
        cont12 += 1
    if age[num] == 13:
        cont13 +=1
    if age[num] == 14:
        cont14 += 1
    if age[num] == 15:
        cont15 += 1
    if age[num] == 16:
        cont16 += 1
    if age[num] == 17:
        cont17 += 1
    if age[num] == 18:
        cont18 +=1
    if age[num] == 19:
        cont19 += 1
    if age[num] == 20:
        cont20 += 1
#CHECKING THE NUMBERS OF PEOPLE OF AGES
if cont1 >= 1:
    print(f"Temos {cont1} pessoas de 1 ano na lista")
if cont2 >= 1:
    print(f"Temos {cont2} pessoas de 2 anos na lista")
if cont3 >= 1:
    print(f"Temos {cont3} pessoas de 3 anos na lista")
if cont4 >= 1:
    print(f"Temos {cont4} pessoas de 4 anos na lista")
if cont5 >= 1:
    print(f"Temos {cont5} pessoas de 5 anos na lista")
if cont6 >= 1:
    print(f"Temos {cont6} pessoas de 6 anos na lista")
if cont7 >= 1:
    print(f"Temos {cont7} pessoas de 7 anos na lista")
if cont8 >= 1:
    print(f"Temos {cont8} pessoas de 8 anos na lista")
if cont9 >= 1:
    print(f"Temos {cont9} pessoas de 9 anos na lista")
if cont10 >= 1:
    print(f"Temos {cont10} pessoas de 10 anos na lista")
if cont11 >= 1:
    print(f"Temos {cont11} pessoas de 11 anos na lista")
if cont12 >= 1:
    print(f"Temos {cont12} pessoas de 12 anos na lista")
if cont13 >= 1:
    print(f"Temos {cont13} pessoas de 13 anos na lista")
if cont14 >= 1:
    print(f"Temos {cont14} pessoas de 14 anos na lista")
if cont15 >= 1:
    print(f"Temos {cont15} pessoas de 15 anos na lista")
if cont16 >= 1:
    print(f"Temos {cont16} pessoas de 16 anos na lista")
if cont17 >= 1:
    print(f"Temos {cont17} pessoas de 17 anos na lista")
if cont18 >= 1:
    print(f"Temos {cont18} pessoas de 18 anos na lista")
if cont19 >= 1:
    print(f"Temos {cont19} pessoas de 19 anos na lista")
if cont20 >= 1:
    print(f"Temos {cont20} pessoas de 20 anos na lista")
# MOST FREQUENT AGE
print("A maior frequencia de idades é de", end=" ")
print(max(cont1 , cont2 , cont3 , cont4 , cont5 , cont6 , cont7, cont8, cont9 , cont10 , cont11 , cont12 , cont13 , cont14 , cont15 , cont16 , cont17 , cont18 , cont19 , cont20))
# THE RANGE OF AGES
print(f"O intervalo de idades é de {range_age}")
# HOW MANY OLDER THAN 9
soma = cont10 + cont11 + cont12 + cont13 + cont14 + cont15 + cont16 + cont17 + cont18 + cont19 + cont20
print(f"A quantidade de pessoas maiores de 9 anos é de {soma} pessoas")

