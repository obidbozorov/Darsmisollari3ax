class mashina:
    def __init__(self, nomi,yili, rangi):
        self.nomi=nomi
        self.yili=yili
        self.rangi=rangi
    def yurish(self):
        print("G'ingngngnngngngngngn!")
class yengil_mashina(mashina):
    def __init__(self, nomi, yili,rangi,turi,urindiq_soni):
        super.__init__(self, nomi,yili, rangi)
        self.turi=turi
        self.urndiqsoni=urindiq_soni
Gentra=yengil_mashina("Gentra",2022,"Qora","Sedan",5)
print(Gentra.yili)

