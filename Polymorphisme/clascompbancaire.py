'''class comptebancaire:
    numerocompt=0
    nom=""
    solde=0
    versemen=0
    retraite=0.0
    nbjours=0
    taux=0
    def __init__(self,a,b,c,d,e,f,j):
        self.numerocompt=a
        self.nom=b
        self.solde=c
        self.versemen=d
        self.retraite=e
        self.nbjours=f
        self.taux=j
    def versement(self,versement):
        if self.versemen and self.solde > 0:
            versement=self.versemen
            versement-=self.solde
            print("Votre verment est:",versement)
    def retrait(self,retrait):
        self.retraite=retrait
    def Agios(self):
            agios=self.solde*self.nbjours*self.taux/365
            print("Le agios est :",agios)
    def afficher_infos(self):
        print("Votre Infos est:",self.numerocompt,self.nom,self.solde,self.versemen,self.retraite,self.nbjours,self.taux)
s1=comptebancaire(432,"Nader",5000,15,0.05,12,0.1)
s1.Agios()
s1.afficher_infos()'''
'''============================================================================================================================'''
'''class employee:
    matricule=0
    nom=""
    prenom=""
    datenaiss=0
    dateembauche=0
    dateancei=0
    salaire=0
    age=0
    def __init__(self,a,b,c,d,e,f):
        self.matricule=a
        self.nom=b
        self.prenom=c
        self.datenaiss=d
        self.dateembauche=e
        self.salaire=f
    def setage(self,age):
        self.age=age
    def setdateanciente(self,anciente):
        self.dateancei=anciente
    def augmentationsalaire(self):
        if self.salaire>0 and self.dateancei<5:
            augmentation=self.salaire*0.02
            print("L'augmentation est:",augmentation)
        elif self.dateancei<10:
            augmentation=self.salaire*0.05
            print("L'augmentation est:",augmentation)
        else:
            augmentation=self.salaire*0.1
            print("L'augmentataion")
            print("L'augmentation est:",augmentation)
    def afficher_infos(self):
        print("Votre infos:",self.matricule,self.nom,self.prenom,self.datenaiss,self.dateembauche,self.dateancei)
s1=employee(132,"nader","doghmi",2006,2017,5000)
s1.setdateanciente(3)
s1.setage(25)
s1.augmentationsalaire()
s1.afficher_infos()'''
'''============================================================================================================================'''
'''import math
class point:
    x1=0
    x2=0
    y1=0
    y2=0
    def __init__(self,a,b,c,d):
        self.x1=a
        self.x2=b
        self.y1=c
        self.y2=d
    def distance(self):
        distance=math.sqrt((self.x1-self.x2)-(self.y1-self.y2))
        print("La distance est:",distance)
    def milieu(self):
        Milieu=(self.x1+self.x2/2,self.y1+self.y2/2)
        print("Le milieu est:",Milieu)
    def afficher_infos(self):
        print("Votre infos est:")
s1=point(10,6,3,2)
s1.afficher_infos()
s1.distance()
s1.milieu()'''
'''============================================================================================================================'''
'''class droite:
    a=0.0
    b=0.0
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def appartient(self,p):
        self.a*p.x+self.b-p.y==0
        if self.a*p.x+self.b-p.y ==0:
            print("L'appartenance est:",True)
        else:
            print("L'appartenance est:",False)
    def getpoint(self,x):
        y = self.a * x + self.b
        return (x, y)
    def Parallele(self,P):
        x , y = P
        parallele = y - self.a * x 
        return droite(self.a, parallele)
s1=droite(1.5,1.5)'''
'''================================================================================================================='''
'''class fournisseur:
    __idf = 0
    __nomf = ""
    __prenomf = ""

    def __init__(Self):
        pass

    def __init__(self,id,nom,prenom):
        self.__idf = id
        self.__nomf = nom 
        self.__prenomf = prenom
    def getnom(self):
        return self.__nomf
class auteur:
    __idA = 0
    __nomA = ""
    __prenomA = ""
    def __init__(self):
        pass

    def __init__(self,id,nom,prenom):
        self.__idA = id
        self.__nomA = nom 
        self.__prenomA = prenom

class livre:
    __titre = ""
    __anne = ""
    __Npage = 0
    __prix = 0.0
    s=fournisseur
    a=auteur
    def __init__(self,titre, anne , page , prix,ss,aa):
        self.__titre = titre 
        self.__anne = anne 
        self.__Npage = page
        self.__prix = prix
        self.s=ss
        self.a=aa
    def aa(self,lv):
       print(lv.s.getnom())
    def copy(self):
        return livre(self.__titre,self.__anne, self.__Npage,self.__prix,self.__idf,self.__nomf,self.__prenomf,self.__idA,self.__nomA,self.__prenomA)

f1=fournisseur("saad","akram",56789)
a1=auteur("achraf","charqy",12345)
obj = livre("la boite a merveille", 2004 , 50, 2500,f1,a1)
obj.aa(obj)
'''