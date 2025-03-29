class Employee:
    nom=""
    age=""
    salaire=0
    def __init__(self,a,b,h):
        self.nom=a
        self.age=b
        self.salaire=h
    def AFFICHER_INFOS(self):
        print(self.nom,self.age,self.salaire)
class Developpeur(Employee):
    language=""
    prenom=""
    carrierprofesionnelle=""
    def __init__(self,z,x,c,j,k,l):
        Employee.__init(self,z,x,c)
        self.language=j
        self.carrierprofesionnelle=k
        self.prenom=l
    def AFFICHER_INFOS(self):
        Employee.AFFICHER_INFOS(self)
        print(self.language,self.carrierprofesionnelle,self.prenom)
obj1=Employee("Nader","software engnering","doghmi")
obj1.AFFICHER_INFOS()