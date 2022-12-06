'''from Cryptodome.Cipher import DES
def pad(text):
    n = len(text) % 8
    return text + (b' ' * (8-n))
key = b'hello123'
text1 = b'Python is the Best Language!'
des = DES.new(key, DES.MODE_ECB)
padded_text = pad(text1)
encrypted_text = des.encrypt(padded_text)
print(encrypted_text)
print(des.decrypt(encrypted_text))
#from Crypto.Cipher import DES
'''
from Cryptodome.Cipher import DES
key = b'-8B key-'
cipher = DES.new(key, DES.MODE_OFB,IV=b'12345678')
plaintext = b'!Axborot xavfsizligi    '
#print(cipher.iv)
msg = cipher.encrypt(plaintext)
print(type(msg))
print(msg.strip())
print(cipher.decrypt(msg))
