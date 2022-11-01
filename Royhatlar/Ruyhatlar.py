'''sonlar = [1, 2, "Hello Worlld", 4, True,15.9256]
massiv=[[1,2,3],[4,5,6],[7,8,9,10,11],"Hello World!",[55,True],99]
print(massiv[0][1])
print(massiv[2][4])
print(massiv[3][2])

toq_sonlar=[]
toq_sonlar.append("SALOM")
for i in range(1,1001,2):
    toq_sonlar.append(i)
toq_sonlar.append("Hello")
print(toq_sonlar[10:])
toq_sonlar=[]
toq_sonlar=list(range(1,1001,2))
print(toq_sonlar)
massiv=[[1,2,3],[4,5,6],[7,8,9,10,11],"Hello World!",[55,True],99]
massiv.append(100)
massiv.insert(5,"Bobur!")
print(massiv)
print(massiv.index(("Bobur!")))
massiv.remove("Bobur!")
print(massiv)
massiv.pop(1)
print(massiv)
a=list(range(2,51,2))
b=a[-5:]
print(b)
a=[1,2,3]
a.insert(1,4)
print(a)
b=[1,1,3]
if a<b:
    print("Teng")
else:
    print("Teng emas")
a=[1,2,3]
a.insert(1,[4,5,6,7])
print(a[1][:2])
a=[]
for i in range(1,11,1):
    b=[]
    for j in range(1,11,1):
        b.append(j)
    a.append(b)
print(a[1][:2])
print(a[:][:2])
a=[4,5,6,7,8,7,6]
print(a.sort())
companies = ["Microsoft", "Google", "Oracle", "Apple"]
item = "SOracle" # o’chirish kerak bo’lgan element
if item in companies:
    companies.remove(item)
print(companies)
a=[4,5,6,7,8,7,6]
a.sort(reverse=False)
print(a)
vil1 = ["Toshkent", "Xorazm", 'Buxoro','Navoiy']
vil2 = vil1[:]
vil2.pop(1)
print(vil1)
print(vil2)
vil1 = ["Toshkent", "Xorazm", 'Buxoro']
vil2 = ['Navoi', 'Jizzax']
vil2= vil2+vil2
print(vil2)'''
''' Bo'sh bo'lmagan, raqamlardan iborat va nuqta bilan tugaydigan
 matn berilgan. Matndagi eng ko'p uchraydigan raqam chop 
 qilinsin (agar bunday raqamlar bir nechta bo'lsa, ulardan ixtiyoriy
  bittasi chop qilinsin).'''
'''a=[]
while True:
    b=input("Keyingi sonni kiriting: ")
    if b!=".":
        a.append(int(b))
    else:
        break
b=[]
for i in a:
    b.append(a.count(i))
print(a[b.index(max(b))]," elementi ", max(b), " marta qatnashgan.")'''
''' Har biri n ta butun sondan iborat ikkita ketma-ketlik berilgan. 
Birinchi ketma-ketlikning ikkinchi ketma-ketlikka kirmagan sonlari 
ichidagi eng kichigi topilsin (bunaqa sonlardan kamida bittasi mavjud
 deb faraz qilinsin).'''
'''n=10
a,b=[],[]
print("Birinchi massiv elementlarini kiriting: ")
for i in range(n):
    a.append(int(input()))
print("Ikkinchi massiv elementlarini kiriting: ")
for i in range(n):
    b.append(int(input()))
c=[]
for i in a:
    if not i in b:
        c.append(i)
print(min(c))'''
a=[4,5,6,4,8,6]
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
print(b)



