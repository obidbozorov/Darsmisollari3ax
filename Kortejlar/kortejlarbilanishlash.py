'''talabalar=()
print(type(talabalar))
user = ("Akmal", 21)
print(user) # ('Akmal', 21)
user="Akmal", 22,"Shoxrux",25
user = (25,)
print(type(user))
user_list = ["Yusuf", 'Tolib', 'Rustam','Qodir','Sobir','Nodir','Jobir']
user_tuple = tuple(user_list)
print(user_tuple[:3])
print(user_tuple)
user = ("Yusuf", "a","Ғ9",'tolib', 'Rustam','Qodir','Sobir','Nodir','Jobir')
usertartiblangani=tuple(sorted(user, reverse=False))
print(usertartiblangani)'''
users = ("Yusuf", 'Qodir', 'Erkin',['Sobir','Nodir'])
a, b, c,d = users
print(a) # Yusuf
print(b) # Qodir
print(c) # Erkin
print(users[3][1])
print(users[-1][-1])