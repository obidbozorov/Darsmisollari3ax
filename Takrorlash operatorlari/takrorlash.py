'''# S=1+2+,,,,+n n gacha bo'lgan sonlar yig'indisini hisoblash
n=int(input("n="))
i,s=0,0
while i<=n:
    s+=i
    i=i+1
print("S=",s)
# 0 bilan tugaydigan sonlar to'plami berilgan.
# Ulardan juft sonlarining o'rtacha qiymatini toping.
s,k=0,0
a=float(input("Keyingi sonni kiriting: "))
while a!=0:
    if a%2==0:
        s=s+a
        k=k+1
    a=float(input("Keyingi sonni kiriting: "))
print("Javob: ",s/k)
#7 so’mdan katta bo’lgan har qanday tiyinsiz pul miqdorini
# 3 va 5 so’mliklar yig’indisi bilan qaytimsiz to’lash
# mumkinligi isbotlansin. Berilgan n>7 uchun   shartni
# qanoatlantiruvchi, musbat va butun a,b sonlar juftliklari topilsin.
n=int(input("n="))
a,b=0,0
while a<=n//3:
    while b<=n//5:
        if 3*a+5*b==n:
            print("3*",a,"+5*",b,"=",n)
        b=b+1
    a=a+1
    b=0

# 2-masala
n=int(input("n="))
m=int(input("m="))
t,p=0,1
for i in range(2,n+1,1):
    for j in range(3,m+1):
        p=p*(i*i/j)
    t=t+p
    p=1
print("t=",t)
#Berilgan natural sonning raqamlarini teskari tartibda yozishdan hosil
# bo'ladigan sonni aniqlaydigan programma tuzilsin.
import math
ntes=0
n=int(input("n="))
k=int(math.log10(math.fabs(n)))+1
for i in range(0,k):
    ntes=ntes*10+n%10
    n=n//10
    break
print("ntes=",ntes)'''
for i in [8,7,9,6,22,15,4,3,5,312,45]:
    print(i)


