class Etudiant:
    nom=""
    prenom=""
    age=0
    def __init__(self,a,b,c):
        self.nom=a
        self.prenom=b
        self.age=c
    def Affcher_Infos(self):
        print(self.nom,self.prenom,self.age)
obj1=Etudiant("Nader","Doghmi","18ans")
obj1.Affcher_Infos()