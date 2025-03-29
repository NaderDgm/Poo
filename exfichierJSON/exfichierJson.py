'''import json
dataJSON={ "Jean": 30, "Marie": 25, "Paul": 40, "Sophie": 35}
with open('zfichierJSON/data.json','w') as f:
    for i in dataJSON:
        json.dump(dataJSON, f)
f.close()'''
'''======================================'''
'''import json
with open('zfichierJSON/data2.json','r') as file:
    print(json.load(file))

file.close()'''
'''========================================='''
#devoir N6
'''import json
import csv
class produit:
    def __init__(self,a,b,c):
        self.nom=a
        self.prix=b
        self.quantite_duprduit=c
        self.categories=[]
    def __str__(self):
        return "nom",self.nom,"prix",self.prix,"quantite de produit",self.quantite_duprduit
    def mofify_prix(self,nvprix):
        self.prix=nvprix
        print("Votre nouveau prix est:",nvprix)
    def modifier_quantite(self,nvquantite):
        self.quantite_duprduit=nvquantite
        print("Votre nouveau quantite est:",nvquantite)
    def setcategories(self,categories):
        self.categories=categories
        print("Votre categorie est:",categories)
    def ajouter_categorie(self,nvcategorie):
        self.categories.append(nvcategorie)
        print("Votre nouvelle categorie est:",nvcategorie)

    def suprimer_categorie(self,categorie):
        if categorie in self.categories:
            self.categories.remove(categorie)
            print("La categorie supprimer est:",categorie)
    def enregistrer(self, nom_fichier, format_fichier):
        contact = {'nom': self.nom,'prix': self.prix,
            'quantitedeproduit':self.quantite_duprduit,
            'categorie': self.categories}

        if format_fichier == 'texte':
            with open(nom_fichier, 'w') as fichier:
                fichier.write("Nom : ","{self.nom}\n")
                fichier.write("Prix :", "{self.prix}\n")
                fichier.write("Quantite:","{self.quantite_duprduit}\n")
                fichier.write("categorie:","{self.categories}\n")

        elif format_fichier == 'json':
            with open(nom_fichier, 'w') as fichier:
                json.dump(contact, fichier )

        elif format_fichier == 'csv':
            with open(nom_fichier, 'w') as fichier:
                csv.dictWriter(fichier, contact)
                writer = csv.dictWriter(fichier, contact)
                writer.writerow(contact)


        else:
            print("Format de fichier non supporté.")

    def charger(self,nom_fichier,format_fichier):
        if format_fichier != 'json' and format_fichier != 'csv' and format_fichier != 'texte':
            print("Désolé, le format n'est pas accepté",format_fichier)
            print("Utilisez 'json', 'csv' ou 'texte'")
        elif format_fichier == 'json':
            import json
            with open(nom_fichier, 'r') as f:
                json.load(f)

        elif format_fichier == 'csv':
            import csv
            with open(nom_fichier, 'r') as f:
                csv.reader(f)
        else:
            print("err")
    def aff(self):
        print("nom:",self.nom)
        print("prix:",self.prix)
        print("quantite de produit:",self.quantite_duprduit)
        print("categories:",self.categories)
produit1=produit("pomme",100,10)
print(produit1.__str__())
produit1.setcategories(["fruit"])
produit1.mofify_prix(200)
produit1.modifier_quantite(20)
produit1.ajouter_categorie(["legume"])
produit1.suprimer_categorie("fruit")
produit1.enregistrer('produit1','json')
produit1.charger('produit1','json')'''
'''======================================================'''
#devoir7
import json
import csv
class contact:
    def __init__(self,a,b,c,d,e):
        self.nom=a
        self.prenom=b
        self.num=c
        self.tele=d
        self.email=e
        self.groupe_contact=[]
    def __str__(self):
        return "nom",self.nom,"prenom",self.prenom,"num",self.num,"telephone",self.tele,"L'adresse email",self.email
    def modifiernum(self,nvnum):
        self.num=nvnum
        print("Votre nouveau numero est:",nvnum)
    def modifieremail(self,nvemail):
        self.email=nvemail
        print("Votre nouveau email est:",nvemail)
    def setgroupe(self,groupeactuel):
        print("Votre groupe actuele est:",groupeactuel)
    def ajoutegroupe(self,nvgroupe):
        self.groupe_contact.append(nvgroupe)
        print("Votre groupe ajouter est:",nvgroupe)
    def supprimer_groupe(self,ancientgroupe):
        if ancientgroupe in self.groupe_contact:
            self.groupe_contact.remove(ancientgroupe)
        print("Le groupe supprimer  est:",ancientgroupe)
    def enregistrer(self,nom_fichier,format_fichier):
        contact={'nom':self.nom,'prenom':self.prenom,'num':self.num,'telephone':self.tele,'email':self.email}
        if format_fichier == 'texte':
            with open(nom_fichier, 'w') as fichier:
                fichier.write("Nom : ","{self.nom}\n")
                fichier.write("prenom :", "{self.prenom}\n")
                fichier.write("numero:","{self.num}\n")
                fichier.write("telephone:","{self.tele}\n")
                fichier.write("email:","{self.email}\n")

        elif format_fichier == 'json':
            with open(nom_fichier, 'w') as fichier:
                json.dump(contact, fichier )

        elif format_fichier == 'csv':
            with open(nom_fichier, 'w') as fichier:
                csv.dictWriter(fichier, contact)
                writer = csv.dictWriter(fichier, contact)
                writer.writerow(contact)


        else:
            print("Format de fichier non supporté.")

    def charger(self,nom_fichier,format_fichier):
        if format_fichier != 'json' and format_fichier != 'csv' and format_fichier != 'texte':
            print("Désolé, le format n'est pas accepté",format_fichier)
            print("Utilisez 'json', 'csv' ou 'texte'")
        elif format_fichier == 'json':
            with open(nom_fichier, 'r') as f:
                json.load(f)

        elif format_fichier == 'csv':
            with open(nom_fichier, 'r') as f:
                csv.reader(f)
        else:
            print("err")
    def supprimmer(self):
        del self
        print("objet ete suprimmer")
s1=contact("Nader","Dogmhi",1234,632443,"nader@gmail.com")
print(s1.__str__())
s1.setgroupe(["moonlights"])
s1.ajoutegroupe(["lights"])
s1.supprimer_groupe(["moonlights"])
s1.modifiernum(61523769)
s1.modifieremail("naderdogmhi@gmail.com")
s1.enregistrer('zfichierJSON/contact','json')
s1.charger('zfichierJSON/contact','json')
s1.supprimmer()