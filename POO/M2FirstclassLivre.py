class livre:
    titre=""
    NP=0
    editeur=""
    auteur=""
    def __init__(self,e,f,g,h):
        self.titre=e
        self.NP=f
        self.editeur=g
        self.auteur=h
    def modificatio_auteur(self,a):
        self.auteur=a
    def afficher_infos(self):
        print(self.titre,self.auteur)
Obj1=livre("le rouge et le noire",484,"Stendhal","SL")
print(Obj1.auteur)
print(Obj1.NP)
Obj1.afficher_infos()
Obj1.modificatio_auteur("LS")
print(Obj1.auteur)