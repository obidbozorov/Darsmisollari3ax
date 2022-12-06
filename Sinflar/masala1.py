class sanoq_sistema:
    def __init__(self,sonunlik):
        self.son10=sonunlik
    def son2(self):
        self.son2lik=f"{self.son10:b}"
    def son8(self):
        self.son8lik=f"{self.son10:o}"
        return self.son8lik
    def son16(self):
        return f"{self.son10:X}"
son=sanoq_sistema(256)
print(son.son2())
print(son.son2lik)
print(son.son8())
print(son.son8lik)
print(son.son16)
print(son.son16())