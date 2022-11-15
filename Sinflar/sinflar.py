'''class notebook:
    nomi="Acer"
    protsessori="Core i5 10700H"
    operativ_xotirasi=16
    videoxotira="RTX 2070"
    doimiy_xotirasi=512
    def dasturlash(self):
        print(self.nomi+" nomli notebookda dsturlash boshlandi")
FA506=notebook()
FA506.nomi="ASUS TUF GAMING FA506"
FA506.videoxotira=6
FA506.doimiy_xotirasi=1000
FA506.protsessori="Ryzen 7 4800H"
print(FA506.protsessori)
print(FA506.dasturlash())'''
class notebook:
    def __init__(self, OX,DX,VX,PR,oylik,nomi="Acer"):
        self.tuliq_nomi=nomi+" nomli notebook!"
        self.OX=OX
        self.DX=DX
        self.soliq=oylik*0.12
        self.VX=VX
        self.protsessori=PR
        self.rangi="Qora"

    def __del__(self):
        print("Sinf obekti o'chirildi")
    def dasturlashga_buladimi(self):
        if self.OX>=8 and self.OX<16:
            print("Minimal talablarga javob beradi.")
        if self.OX>16:
            print("Talablarg to'liq javob beradi.")
        if self.OX<8:
            print("Ushbu notebookni dasturlashga ishlatmagan ma'qul.")

yuldoshev_acer=notebook(PR="Core i5", OX=16,DX=512, VX=8, oylik=500000)
print(yuldoshev_acer.tuliq_nomi)
yuldoshev_acer.__del__()
del yuldoshev_acer
del notebook
qodirov_dell=notebook(PR="Core i5", OX=16,DX=512, VX=8,
                      oylik=500000,nomi="DELL")
print(qodirov_dell.tuliq_nomi)



