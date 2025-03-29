class animal:
    nom=""
    def __init__(self,a):
        self.nom=a
    def Afficher_Infos(self):
        print(self.nom)
class animals(animal):
    couleur=""
    def __init__(self,j,h):
        animal.__init__(self,h)
        self.couleur=h
    def Afficher_Infos(self):
        animal.Afficher_Infos(self)
        print(self.couleur)
obj1=animals("Lions","orange")
obj1.Afficher_Infos()