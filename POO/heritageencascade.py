class personne:
    nom=""
    prenom=""
    datenaiss=0
    def __init__(self,n,p,c):
        self.nom=n
        self.prenom=p
        self.datenaiss=c
class employye(personne):
    salaire=0
    post=""
    dateemb=0
    def __init__(self,nom,prenom,datenaiss,post,sal,dateemb):
        super().__init__(nom,prenom,datenaiss)
        self.post=post
        self.salaire=sal
        self.dateemb=dateemb
    def afficher_infos(self):
        print("Nom et prenom:",self.nom,self.prenom,"Post et salaire:",self.post,self.salaire,self.dateemb)
class cadre(employye,personne):
    tycontract=""
    def __init__(self,nom,prenom,datenaiss,post,sal,dateemb,tycontract):
        personne.__init__(self,nom,prenom,datenaiss)
        employye.__init__(self,post,sal,dateemb)
        self.tycontract=tycontract
    def afficher(self):
        employye.afficher_infos(self)
        print(self.typecontract,self.calculBonus())
    def calculBonus(self):
        if self.salaire>5000:
            Bonus = self.salaire*0.1
            print(Bonus)
        else:
            print("err")
s1=cadre("Nader","Doghmi",2006,"responsable",5000,2020,"CDD")
s1.calculBonus()
s1.afficher()

