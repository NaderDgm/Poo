class Rectangle:
    Long=0
    Larg=0
    def __init__(self,a,b):
        self.Long=a
        self.Larg=b
    def Afficher_Infos(self):
        print(self.Long,self.Larg)
obj1=Rectangle(100,200)
obj1.Afficher_Infos()
