'''talabalar = {"Bobur", "Zafar", "Alisher","Zafar"}
print(type(talabalar))
print(talabalar) # {'Bobur', 'Zafar', 'Alisher'}
tubSonlar = [2,3,5,7,11,11,7,2]
tubSonlarTuplami = set(tubSonlar)
print(tubSonlarTuplami)
print(tubSonlar)
print(len(tubSonlarTuplami))
print(len(tubSonlar))
tubSonlar = {2,3,5,7,11,11,7,2}
tubSonlar.add(13)
tubSonlar.add(5)
#tubSonlar.remove(55)
tubSonlar.discard(55)
if 55 in tubSonlar:
    print("5 soni to`plamda mavjud")
tubSonlar.clear()
del tubSonlar
print(tubSonlar)
tubSonlar = {2,3,5,7,11,7,2}
sonlar=tubSonlar.copy()
tubSonlar.discard(11)
tubSonlar=sonlar.copy()
print(sonlar)
print(tubSonlar)'''
famil = {"Axmedov", "Niyazov"}
ism = {"Axmedov", "Tohir","Niyazov"}
print(famil.issubset(ism))
print(ism.issuperset(famil))
#FIO=ism.difference(ism)
#print(FIO)
'''FIO = ism.union(famil)
kesish=ism.intersection(famil)
print(FIO)
print(kesish)'''
