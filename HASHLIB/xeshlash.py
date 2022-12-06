#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)
from hashlib import *
'''xeshqiymat=sha256(b"Assalomu Alaykum")
print(xeshqiymat.hexdigest())
xeshqiymat=md5(b"gffa faad f fadsfasd fasdfsd fasd fadsfasf f fasd fsdads fasdfasdfasedag g dsfdsdsasfds")
xeshqiymat=sha256(b"Assalomu ")
xeshqiymat.update(b"Alaykum")
print(xeshqiymat.hexdigest())'''
fadres=f"D:/Instal/Labaratoriya INSTAL/ISO/SERVER_EVAL_x64FRE_en-us.iso"
blokulchami=65536
xeshqiymat=sha256()
with open(fadres,'rb') as f:
    fb=f.read(blokulchami)
    while len(fb)>0:
        xeshqiymat.update(fb)
        fb=f.read(blokulchami)
print(xeshqiymat.hexdigest())







