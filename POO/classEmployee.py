class Employer:
    nom=""
    age=0
    salaire=0.0
    def _init__(self,a,b,c):
        self.nom=a
        self.age=b
        self.salaire=c
    def setNom(self, nom):
        self.nom = nom

    def setAge(self, age):
        if age > 0:
            self.age = age
            
    def setSalaire(self, salaire):
        if salaire > 0:
            self.salaire = salaire
    def getNom(self):
        return self.nom

    def getAge(self):
        return self.age
    def getSalaire(self):
        return self.salaire
    def calculBonus(self):
        return self.salaire 