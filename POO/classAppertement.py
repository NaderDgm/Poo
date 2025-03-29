class appartement:
    numapp=0
    etageapp=0
    capaciter=0
    def __init__(self,a,b,c):
        self.numapp=a
        self.etageapp=b
        self.capaciter=c
    def AFFICHER_INFOS(self):
        print(self.numapp,self.capaciter)
    def calprix(self):
        return self.capaciter*175
s1=appartement(10,3,15)
s1.AFFICHER_INFOS()
print(s1.calprix())