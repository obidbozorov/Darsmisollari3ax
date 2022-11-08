'''
9-masala
'''
import math

''' 1/2=(2-1)/2   1/3=(3-2)/3
a=int(input("a="))
b=int(input("b="))'''
s=0
for i in range(1,21):
    s=s+math.factorial(20)/i
a=s
b=math.factorial(20)
k=min(a,b)
print(a,b,k)
i=2
if a % k == 0 and b % k == 0:
    a = a / k
    b = b / k
while i<math.sqrt(k)+1:
    if a%i==0 and b%i==0:
        a=a/i
        b=b/i
        print(i)
        k=min(a,b)
    else:
        i=i+1
p=a
q=b
print("a=",a, " b=",b)







