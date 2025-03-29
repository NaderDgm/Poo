'''from abc import ABC,abstractmethod
class comparable:
    @abstractmethod
    def compareTol(self):
        pass
class personne(comparable):
    def __init__(self,nom,age):
        self.__nom=nom
        self.__age=age
    def compareTol(self,p):
        if self.__age==p.__age:
            return True
        else:
            return False
class Outils(comparable):
    def __init__(self,L,prix):
        self.__L=L
        self.__prix=prix
    def compareTol(self,o):
        if self.__L==o.__L:
            return True
        else:
            return False
s1=personne("n1",20)
s2=personne("n2",20)
p1=Outils(60,450)
p2=Outils(60,450)
if (s1.compareTol(s2)):
    print("ont le mème age")
else:
    print("ages different")
if (p1.compareTol(p2)):
    print("mème longueur")
else:
    print("Longueur different")'''
'''==============================================================================='''
'''from abc import ABC,abstractmethod
import math
class Ishape:
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetre(self):
        pass
class Circle(Ishape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def perimetre(self):
        return 2 * math.pi * self.radius
circle=Circle(5)
print(circle.area())
print(circle.perimetre())'''
'''==============================================================================='''
''''from abc import ABC,abstractmethod
class instrument:
    @abstractmethod
    def jouer(self):
        pass
class guitare(instrument):
    def jouer(self):
        print("jouer la guitare")
class piano(instrument):
    def jouer(self):
        print("jouer le piano")
s1=guitare()
s1.jouer()
s1=piano()
s1.jouer()'''
'''==============================================================================='''
'''from abc import ABC,abstractmethod
class transport:
    @abstractmethod
    def deplacer(self):
        pass
class voiture(transport):
    def deplacer(self):
        print("deplacer en voiture")
class avion(transport):
    def deplacer(self):
        print("deplacer en avion")
s1=voiture()
s1.deplacer()
s1=avion()
s1.deplacer()'''
'''==============================================================================='''
'''from abc import ABC,abstractmethod
class paiement:
    @abstractmethod
    def payer(self):
        pass
class carteBancaire(paiement):
    def payer(self):
        print("payer par carte bancaire")
class paypal(paiement):
    def payer(self):
        print("payer par paypal")
class crypto(paiement):
    def payer(self):
        print("payer par crypto")
s1=carteBancaire()
s1.payer()
s1=paypal()
s1.payer()
s1=crypto()
s1.payer()'''
'''==============================================================================='''
'''from abc import ABC,abstractmethod
class employee:
    @abstractmethod
    def calculerSalaire(self):
        pass
    def afficher_infos(self):
        print("Votre Salaire est:",self.calculerSalaire())
class Manager(employee):
    def calculerSalaire(self):
        return 5000
class Developpeur(employee):
    def calculerSalaire(self):
        return 4000
class Stagiaire(employee):
    def calculerSalaire(self):
        return 3000
s1=Manager()
s1.afficher_infos()
s1=Developpeur()
s1.afficher_infos()
s1=Stagiaire()
s1.afficher_infos()'''
'''==============================================================================='''
'''from abc import ABC,abstractmethod
class media:
    @abstractmethod
    def emprunter(self):
        pass
    @abstractmethod
    def retourner(self):
        pass
    def afficher(self):
        print(self.emprunter(),self.retourner())
class livre(media):
    def __init__(self,a,b):
        self.emprunte=a
        self.livre=b
    def emprunter(self):
        if self.livre in self.emprunte:
            print("le livre est emprunter")
        else:
            print("le livre n'est pas emprunter")
    def retourner(self):
        if self.retourner==True:
            print("le livre est retourner")
        else:
            print("le livre n'est pas retourner")
class dvd(media):
    def emprunter(self):
        if self.emprunter==True:
            print("le dvd est emprunter")
        else:
            print("le dvd n'est pas emprunter")
    def retourner(self):
        if self.retourner==True:
            print("le dvd est retourner")
        else:
            print("le dvd n'est pas retourner")
class magazin():
    def emprunter(self):
        if self.emprunter==True:
            print("le magazin est emprunter")
        else:
            print("le magazin n'est pas emprunter")
    def retourner(self):
        if self.retourner==True:
            print("le magazin est retourner")
        else:
            print("le magazin n'est pas retourner")
s1=livre()
s1.emprunter()
s1.retourner()
s1=dvd()
s1.emprunter()
s1.retourner()
s1=magazin()
s1.emprunter()
s1.retourner()'''