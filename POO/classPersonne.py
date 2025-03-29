class Personne:
    nom=""
    prenom=""
    age=0
    def __init__(self,a,b,c):
        self.nom=a
        self.prenom=b
        self.age=c
    def Afiicher_Infos(self):
        print(self.nom,self.prenom,self.age)
obj1=Personne("Nader","Doghmi","18ans")
obj1.Afiicher_Infos()