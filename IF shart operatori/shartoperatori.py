'''yoshi = 21
if yoshi >18:
    print("Kirishga ruxsat beriladi")
print("Tamom")
import math

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
D=pow(b,2)-4*a*c
if D>0:
    x1=((-b)+math.sqrt(D))/(2*a)
    x2 = ((-b) - math.sqrt(D)) / (2 * a)
    print("x1=",x1,"\nx2=",x2)
elif D==0:
    x=(-b)/(2*a)
    print("x=",x)
else:
    print("Tenglama ildizga ega emas!")'''
'''1-masala  Agar tomonlarining uzunliklari ixtiyoriy a, b, c sonlarga teng 
bo’lgan uchburchakni qurish mumkin bo’lmasa 0, aks holda – uchburchak
 teng tomonli bo’lsa 3, teng yonli bo’lsa 2 va boshqa hollar
  uchun 1 qiymatini chop qiluvchi programma tuzilsin.'''

'''a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
        print("Uchburchak teng tomonli! 3")
    elif a==b or b==c or a==c:
        print("Uchburchak teng yonli 2")
    else:
        print("Uchburchak oddiy 1")
else:
    print("Uchburchak yasab bo'lmaydi!")'''
''' Uchta X,Y,Z haqiqiy sonlar berilgan, agar  ular monoton bo’lsa
 ularning qiymatlari ikkilantirilsin, 
aks holda har bir uzgaruvchi qiymati qarama qarshisiga almashtirilsin.  '''
'''x=float(input("x="))
y=float(input("y="))
z=float(input("z="))
if (x>y and y>z) or (x<y and y<z):
    print("Monoton \n")
    print("x=",x*2," y=",y*2, " z=",z*2)
else:
    print("Monoton emas \n")
    print("x=", -x, " y=", -y, " z=", -z)'''
''' Berilgan uch  xonali son raqamlari orasida bir xillari bormi?  '''
a=int(input("a="))
x=a//100
y=(a//10)%10
z=a%10
if x==y or y==z or x==z:
    print("Bor")
else:
    print("Yo`q")

