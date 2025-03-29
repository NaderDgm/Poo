'''from abc import ABC,abstractmethod
class vehicul:
    @abstractmethod
    def printinfos(self):
        pass
    def Aug_vitess(self,vitesse):
        self.vitesse+=vitesse
class MOTO(vehicul):
    def __init__(self,V):
        self.vitesse=V
    def printinfos(self):
        print("IM Nader Doghmi",self.vitesse)
v=MOTO(20)
v.printinfos()
v.Aug_vitess(10)
v.printinfos()
#ve=vehicul()'''
'''================================================================================================='''
'''from abc import ABC,abstractmethod
class Forme:
    @abstractmethod
    def calculer_aire(self):
        pass
class rectangle(Forme):
    def __init__(self,a,b):
        self.L=a
        self.l=b
    def calculer_aire(self):
        aire= self.L*self.l
        print("L'aire est:",aire)
class cercle(Forme):
    def __init__(self,r):
        self.rayon=r
    def calculer_aire(self):
        aire=3.14 *self.rayon**2
        print("L'aire est :",aire)
s1=rectangle(1.5,1.5)
s1.calculer_aire()
s1=cercle(4)
s1.calculer_aire()'''
'''================================================================================================='''
'''from abc import ABC,abstractmethod
class employee:
    nom=""
    prenom=""
    salaire=0
    def __init__(self,a,b,c):
        self.nom=a
        self.prenom=b
        self.salaire=c
    @abstractmethod
    def calculer_prime(self):
        pass
class Manager(employee):
    def __init__(self,a,b,c):
        employee.__init__(self,a,b,c)
    def calculer_prime(self,a):
        prime=self.salaire*a
        print("VOTRE PRIME EST:",prime)
class Ingenieur(employee):
    def __init__(self,a,b,c):
        employee.__init__(self,a,b,c)
    def calculer_prime(self,a):
        prime=self.salaire*a
        print("VOTRE PRIME EST:",prime)
s1=Manager("nader","doghmi",5000)
s1.calculer_prime(0.01)'''
'''================================================================================================='''
'''from abc import ABC,abstractmethod
class vehicul:
      @abstractmethod
      def aff(self):
        pass
class Voiture(vehicul):
    marque=""
    modele=0
    vitesse_max=0
    def __init__(self,a,b,c):
        self.marque=a
        self.modele=b
        self.vitesse_max=c
    def aff(self):
        print("Les infos de voiture:",self.marque,self.modele,self.vitesse_max)
class camion(vehicul):
    marque=""
    modele=0
    vitess_max=0
    def __init__(self,a,b,c):
        self.marque=a
        self.modele=b
        self.vitess_max=c
    def aff(self):
        print("Les infos de camion:",self.marque,self.modele,self.vitess_max)
s1=Voiture("BMW",2019,180)
s1.aff()
s1=camion("rMOUK",2009,100)
s1.aff()'''
'''================================================================================================='''
'''from abc import ABC,abstractmethod
class transport:
@abstractmethod
    def moyen_transport(self):
        pass
class avion(transport):
    def moyen_transport(self):
        print("Je suis un avion")
class train(transport):
    def moyen_transport(self):
        print("je suis un train")
class bateau(transport):
    def moyen_transport(self):
        print("Je suis un bateau")
s1=avion()
s1.moyen_transport()'''
'''================================================================================================='''
'''from abc import ABC,abstractmethod
class jeu:
    @abstractmethod
    def commencer(self):
        pass
class football(jeu):
    def commencer(self):
        print("Le jeu de football commence.")
class tennis(jeu):
    def commencer(self):
        print("Le jeu de tennis commence.")
def lancer_jeu(x):
        if isinstance (x,jeu):
            x.commencer()
        else:
            print("n'est pas une inst a jeu")
k=tennis()
lancer_jeu(k)
h=100
lancer_jeu(h)'''
'''================================================================================================='''
'''from abc import ABC,abstractmethod
class outil:
    @abstractmethod
    def utilisser(self):
        pass
class marteau(outil):
    def utilisser(self):
        print( "J'utilise un marteau pour enfoncer un clou.")
class tournevis(outil):
    def utilisser(self):
        print("J'utilise un tournevis pour serrer une vis")
s1=marteau()
s1.utilisser()
s1=tournevis()
s1.utilisser()
'''
'''================================================================================================='''
'''from abc import ABC,abstractmethod
class media:
    @abstractmethod
    def aff(self):
        pass
class livre(media):
    Titre=""
    Auteur=""
    def __init__(self,a,b):
        self.Titre=a
        self.Auteur=b
    def aff(self):
        print("Les infos de livre:",self.Titre,self.Auteur)
class film(media):
    titre=""
    realisateur=""
    def __init__(self,a,b):
        self.titre=a
        self.realisateur=b
    def aff(self):
        print("Les infos de film:",self.titre,self.realisateur)
s1=livre("LE noire","Nader")
s1.aff()
s1=film("fast","nader")
s1.aff()'''
'''========================================================================================================'''
'''from abc import ABC,abstractmethod
class compagnie:
    @abstractmethod
    def calculer_revenu(self):
        pass
class restaurant(compagnie):
    revenu_journalier=0
    nombre_jours=0
    def __init__(self,a,b):
        self.revenu_journalier=a
        self.nombre_jours=b
    def calculer_revenu(self):
        revenu=self.revenu_journalier*self.nombre_jours
        print("Le revenu est:",revenu)
class supermarcher(compagnie):
    ventetotal=0
    marge=0
    def __init__(self,a,b):
        self.ventetotal=a
        self.marge=b
    def calculer_revenu(self):
        revenu=self.ventetotal*self.marge
        print("Le revenu est:",revenu)
s1=restaurant(3500,15)
s1.calculer_revenu()
s1=supermarcher(10,0.1)
s1.calculer_revenu()
        '''
'''========================================================='''
'''from abc import ABC,abstractmethod
class instruments:
    @abstractmethod
    def jouer(self):
        pass
class guitar(instruments):
    def jouer(self):
        print("guitar")
class piano(instruments):
    def jouer(self):
        print("piano")
s1=guitar()
s1.jouer()'''
'''========================================================='''
'''from abc import ABC,abstractmethod
class transport:
    def deplacer(self):
        pass
class avion(transport):
    def deplacer(self):
        print("avion")
class bateau(transport):
    def deplacer(self):
        print()'''