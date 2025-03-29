'''class rectangle:
    l=0.0
    L=0.0
    def __init__(self,a,b):
        self.l=a
        self.L=b
    def setl(self,l):
        l=self.l
    def setL(self,L):
        L=self.L
    def perimtre(self):
        perimetre=self.l+self.L
        print("Le perimtre est :",perimetre)
    def surface(self):
        surface= self.l*self.L
        print("La surface est :",surface)
    def afficher_infos(self):
        print("Les infos:",self.surface(),self.perimtre())
class parallelepiped(rectangle):
    def __init__(self,a,b,c):
        rectangle.__init__(a,b)
        self.hauteur=c
    def volume(self):
        print("Le volume est :",self.l*self.L*self.hauteur)'''
'''============================================================================================'''
'''class salaire:
    def __init__(self):
        self.__matricule=0
        self.__nom=""
        self.__prenom=""
        self.__salaire=0
        self.__tauxcs=0
    def __init__(self,a,b,c,d,e):
        self.__matricule=a
        self.__nom=b
        self.__prenom=c
        self.__salaire=d
        self.__tauxcs=e
    def calculerSalaireNET(self):
        if self.__salaire>0 and self.__tauxcs>0:
            salaire= self.__salaire-(self.__salaire*self.__tauxcs)
            return"Le salaire est",salaire
        else:
            print("ERR")
    def Equals(self):
        self.__matricule=self.__matr'''