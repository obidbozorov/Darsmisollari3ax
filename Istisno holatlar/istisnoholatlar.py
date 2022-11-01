'''str = "hello"
number = int(str)
print(number)

try:
    son = int(input("Sonni kiriting: "))
    son2=1/son
    print("Kiritilgan son:", son)
except ValueError:
    print("O`girish noto`g`ri amalga oshirildi.")
    print("Dastur tugadi.")
except ZeroDivisionError:
    print("Nolga bo'lish xatoligi yuz berdi!")
except Exception:
    print("Boshqa xatolik yuz berdi!")
print("Dastur tugadi.")'''
try:
    son = int(input("Sonni kiriting: "))
    son2=1/son
    print("Kiritilgan son:", son)
except Exception as xato:
    print("Quyidagi xatolik yuz berdi: ", xato)