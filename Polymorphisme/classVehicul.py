class vehicule:
    def __init__(self, marque, modele, couleur):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
    def afficher(self):
        print("Marque: ", self.marque)
        print("Modele: ", self.modele)
        print("Couleur: ", self.couleur)
class voiture(vehicule):
    def __init__(self, marque, modele, couleur, nb_portes):
        vehicule.__init__(self, marque, modele, couleur)
        self.nb_portes = nb_portes
    def afficher(self):
        vehicule.afficher(self)
        print("Nombre de portes: ", self.nb_portes)
class bicycle(vehicule):
    def __init__(self, marque, modele, couleur, type):
        vehicule.__init__(self, marque, modele, couleur)
        self.type = type
    def afficher(self):
        vehicule.afficher(self)
        print("Type: ", self.type)