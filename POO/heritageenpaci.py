'''class personne:
    nom=""
    prenom=""
    def __init__(self,n,p):
        self.nom=n
        self.prenom=p
    def afficher_infos(self):
        print("Nom et prenom:",self.nom,self.prenom)
#class mere:
class employee:
    code=0
    salaiare=0
    def __init__(self,code,s):
        self.code=code
        self.salaire=s
    def afficher_infos(self):
        print("Salaire et post:",self.code,self.salaire)
class Directeur(employee):
    bureau=""
    def __init__(self,n,p,code,s,b):
        employee.__init__(self,n,p,code,s,b)
        self.bureau=b'''
'''================================================================================================================='''
'''class vehicule:
    Marque=""
    Model=0
    def __init__(self,a,b,c):
        self.Marque=b
        self.Model=c
class voiture(vehicule):
    couleur=""
    def __init__(self,a,b,c,d):
        vehicule.__init__(self,a,b,c,d)
        self.couleur=d
class camion(voiture):
    poids=0.0
    def __init__(self,a,b,c,d,e):
        vehicule.__init__(self,a,b,c,d,e)
        self.poids=e'''
'''================================================================================================================='''
'''class CompteBancair:
    solde=0
    debitMax=0
    def __init__(self,a,b):
        self.solde=a
        self.debitMax=b
    def setsold(self,setsold):
        self.solde=setsold
    def setdebitsMax(self,setdebimax):
        self.debitMax=setdebimax
    def getsold(self):
        print("Le sold est:",self.solde)
    def getdebitMax(self):
        print("Le debit est:",self.debitMax)'''
'''================================================================================================================='''
'''class etudiants:
    __nom=""
    __prenom=""
    __note=[]
    def __init__(self,a,b):
        self.__nom=a
        self.__prenom=b
    def setnom(self,setnom):
        setnom=self.__nom
    def setprenom(self,setprenom):
        setprenom=self.__prenom
    def ajouternotes(self,notes):
        if 0<self.__note>=20:
            self.__note.append(notes)
    def getnom(self):
        print("Nom:",self.__nom)
    def getprenom(self):
        print("Prenom:",self.__prenom)
    def calculmoyenne(self):
        if len(self.__note)==0:
            return "Pas encore de note"
        else:
            return sum(self.__note)/len(self.__note)'''
'''================================================================================================================='''
'''class personne:
    nom=""
    prenom=""
    def __init__(self,a,b):
        self.nom=a
        self.personne=b
class employee(personne):
    code=0.0
    salaire=0
    def __init__(self,a,b,c,d):
        personne.__init__(self,a,b,c,d)
        self.code=c
        self.salaire=d
class manager(personne,employee):
    service=""
    def __init__(self,a,b,c,d,e):
        employee.__init__(self,a,b,c,d,e)
        self.service=e'''
'''================================================================================================================='''