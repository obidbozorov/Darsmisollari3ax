class Person:
    def __init__(self, name):
        self.__name = name # ismini o'rnatish
        self.__yoshi = 1  # yoshni o'rnatish
    def get_yoshi(self,yoshi):
        if yoshi in range(1,150):
            self.__yoshi=yoshi
        else:
            print("Mumkin bo'lmagan yosh!")
    def set_age(self):
        return self.__yoshi
Nuriddin=Person("Nuriddin")
Nuriddin.get_yoshi(50)
Nuriddin.__yoshi=20
print(Nuriddin.set_age())