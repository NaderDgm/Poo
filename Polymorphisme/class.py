class stg:
    def __init__(self, nom,prenom,note):
        self.nom = nom
        self.prenom = prenom
        self.note = note
    def ajouterbonus(self, bonus1,bonus2=None):
        if bonus2 is None:
            self.note += bonus1
        else:
            self.note += bonus1+bonus2 
    def afficher(self):
        print("Note de l'etudiant", self.nom, self.prenom, "est", self.note)
s1=stg("abdo","doukha", 15)
s1.afficher()
s1.ajouterbonus(1)
s1.afficher()
s1.ajouterbonus(1,1)
s1.afficher()
