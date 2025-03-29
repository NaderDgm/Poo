class personne:
    nom=""
    prenom=""
    age=0
    def __init__(self,a,b,c):
        self.nom=a
        self.prenom=b
        self.age=c
    def afficher_infos(self):
        print(self.nom,self.prenom,self.age)
class stg(personne):
    niveau=""
    filier=""
    groupe=0
    def __init__(self,e,f,g,h,i,j):
        personne.__init__(self,e,f,g)
        self.niveau=h
        self.groupe=i
        self.filiers=j
    def afficher_infos(self):
        personne.afficher_infos(self)
        print(self.niveau,self.filiers,self.groupe)
obj1=stg("nader","doghmi","18","tronc commun ","105","dd")
obj1.afficher_infos()