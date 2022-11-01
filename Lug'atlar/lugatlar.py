'''talaba={"FISH":"Otanazarov Asadbek","kursi":2,
        "Baholari":[3,3,4,5,3,2], "oilalimi":False,"FISH":"Xusanboyev Zokir"}
print(talaba["FISH"])
talaba["kursi"]=3
talaba["yunalishi"]="AX"
print(talaba)
talaba["yunalishi"]="ATT"
print(talaba)
users_list = [["909837022", "Tolib"],["909939343", "Bobur"],
["90394349",""] ]
users_dict = dict(users_list)
#print(users_dict)
#print(users_dict['9077777777'])
print(users_dict.get("909939343"))
users_tuple = ( ("909837022", "Tolib"),
("909939343", "Bobur"),
("903943493", "Alibek") )
users_dict = dict(users_tuple)
#print(users_dict)
telraqam=input("Telefon raqamini kiriting: ")
if telraqam in users_dict:
    print(users_dict[telraqam])
else:
    print("Kontaktingizda bunday raqamli foydalanuvchi yo'q!")
    if input("Kontaktingizga qo`shishni istaysizmi? 1-Ha, 2-Yo'q :")=="1":
        users_dict[telraqam]=input("Ismini kiriting: ")
print(users_dict)
en_uzb={"book":"kitob","pen":"ruchka","cat":"mushuk","dog":"it"}
print(en_uzb.get(input("So`zni kiriting: "),"Bu so`zning tarjimasi yo`q"))
bahoDict = {"A": 5, "B": 4, "C": 3, "D": 2}
print(bahoDict) # {'A': 5, 'B': 4, 'C': 3, 'D': 2}
uchirilgan_baho=bahoDict.pop("A","Hech qanday baho o`chirilmadi")
print(uchirilgan_baho)
#del bahoDict["F"]
print(bahoDict)
bahoDict.clear()
del bahoDict
print(bahoDict)
l = {"ismi": "Sardor", "yoshi": 34}
l["ismi"]="Umar"
l2 = l.copy()
print(l) # {'ismi': 'Sardor', 'yoshi': 34}
print(l2) # {'ismi': 'Sardor', 'yoshi': 34}
l1 = {"ismi": "Sardor", "yoshi": 34}
l2 = {"kursi": 1, "yo`nalishi": "IAT","yoshi":22}
l2.update(l1)
print(l1)
print(l2)
talabalar = {
"+99890123": "Tolmas",
"+99890124": "Bobur",
"+99890125": "Alisher" }
for tal_raqami,ismi in talabalar.items():
    print(tal_raqami, " - ", ismi)
talabalar = {
"+99890123": "Tolmas",
"+99890124": "Bobur",
"+99890125": "Alisher" }
# lug'atning kalitlariga murojaat
print("Kalitlar:")
ismlar=list(talabalar.values())
print(ismlar)
for kalit in talabalar.keys():
    print(kalit, end='; ')
# lug'atning qiymatlariga murojaat
print("\n Qiymatlar:")
for qiymat in talabalar.values():
    print(qiymat, end='; ')
loginData = {
"Zafar":
{
"email": "zafar@nuu.uz",
"tel": "+99890933",
"manzil": "Univer ko`chasi 4"
},
"Rustam":
{
"email": "rustam@nuu.uz",
"tel":
    {"mobil":+998902222,"ish":71254644},
"manzil": "Dekanat ko`chasi 105"
} }
print(loginData["Rustam"]["tel"]["ish"])'''
en_uzb={"book":"kitob","pen":"ruchka","Apple":"Olma",
        "cat":"mushuk","dog":"it"}
eng_uzbtartiblangani=sorted(en_uzb)
for i in eng_uzbtartiblangani:
    print(i, en_uzb[i])



