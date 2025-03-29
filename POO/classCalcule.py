class Calcule:
    nbr1=0
    nbr2=0
    def __init__(self,a,b):
        self.nbr1=a
        self.nbr2=b
    def Somme(self):
        return self.nbr1 + self.nbr2
    def Soustraction(self):
        return self.nbr1 - self.nbr2
obj1=Calcule(1000,500)
obj1.Somme()
obj1.Soustraction()
print(obj1.Somme())
print(obj1.Soustraction())