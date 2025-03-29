class Disque:
    type=""
    capaciter=0 
    marque=""
    vitesse=0 
    def __init__(self,a,b,c,d):
        self.type=a
        self.capaciter=b
        self.marque=c
        self.vitesse=d
    def Afficher_Infos(self):
        print(self.type,self.capaciter,self.marque,self.vitesse)
obj1=Disque( "ssd","1TB","Kingstone","50 m/s" )
obj1.Afficher_Infos()

    