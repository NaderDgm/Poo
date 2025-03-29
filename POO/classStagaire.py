class Stagaire:
    Nom=""
    Prenom=""
    Age=0
    def __init__(self,a,b,c):
        self.Nom=a
        self.Prenom=b
        self.Age=c
    def Afficher_Infos(self):
        print(self.Nom,self.Prenom,self.Age)
obj1=Stagaire("Nader","Doghmi",18)
obj1.Afficher_Infos()

