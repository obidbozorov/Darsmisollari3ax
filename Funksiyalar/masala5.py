'''N natural son berilgan, N ta ihtiyoriy sonlar ketma – ketligi
berilgan ishora almashishlar sonini aniqlovchi funktsiya tuzilsin.
7,8,-3,6,9,-12,-13,15,6
'''
def ishoralmash(a):
    k=0
    for i in range(0,len(a)-1):
        if a[i]*a[i+1]<0:
            k=k+1
    print("Ishora alamshishlar soni=",k)
a=[7,8,-3,6,9,-12,-13,15,6]
ishoralmash(a)




a=[7,8,-3,6,9,-12,-13,15,6]
