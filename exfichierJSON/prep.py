#devoire N6
'''import csv
import json
class produit:
    categories=[]
    def __init__(self,a,b,c):
        self.nom=a
        self.prix=b
        self.quantite_duprduit=c
    def __str__(self):
        return "nom",self.nom,"prix",self.prix,"quantite de produit",self.quantite_duprduit
    def mofify_prix(self,nvprix):
        self.prix=nvprix
        print("Votre nouveau prix est:",nvprix)
    def modifier_quantite(self,nvquantite):
        self.quantite_duprduit=nvquantite
        print("Votre nouveau quantite est:",nvquantite)
    def ajouter_categorie(self,nvcategorie):
        self.categories.append(nvcategorie)
        print("Votre nouvelle categorie est:",nvcategorie)
    def suprimer_categorie(self,categorie):
        if categorie in self.categories:
            self.categories.remove(categorie)
            print("La categorie supprimer est:",categorie)
    def enregistrer(self,nom_fichier,format_fichier):
        produit = {'nom': self.nom,'prix': self.prix,
            'quantitedeproduit':self.quantite_duprduit,
            'categorie': self.categories}
        if format_fichier!='json' and format_fichier!='csv' and format_fichier!='texte':
            print("le format de fichier n'est pas valide")
        elif format_fichier=='json':
            with open('nom_fichier', 'w') as f:
                json.dump(produit, f)
        elif format_fichier=='csv':
            with open('nom_fichier', 'w') as f:
                writer=csv.DictWriter(f,produit)
                writer.writeheader()
                writer.writerow(produit)
        elif format_fichier=='texte':
            with open('nom_fichier', 'w') as f:
                f.write("Nom : ",self.nom,"\n")
                f.write("Prix :", self.prix,"\n")
                f.write("Quantite: ",self.quantite_duprduit,"\n")
                f.write("categorie: ",self.categories,"\n")
        else:
            print("Format de fichier non supporté.Utilisez 'json', 'csv' ou 'texte'")
    def charger(self,nom_fichier,format_fichier):
        if format_fichier!='json' and format_fichier!='csv' and format_fichier!='texte':
            print("le format de fichier n'est pas valide")
        elif format_fichier=='json':
            with open('nom_fichier','r') as f:
                produit=json.load(f)
                print(produit)
        elif format_fichier=='csv':
            with open('nom_fichier','r') as f:
                produit=csv.DictReader(f)
                for row in produit:
                    print(row)
        elif format_fichier=='texte':
            with open('nom_fichier','r') as f:
                produit=f.read()
                print(produit)
        else:
            print("Format de fichier non supporté.Utilisez 'json', 'csv' ou 'texte'")
p=produit("pomme",10,100)
print(p.__str__())
p.ajouter_categorie("fruit")
p.ajouter_categorie("legume")
p.suprimer_categorie("fruit")
p.enregistrer("produit","json")
p.charger("produit","json")'''
'''===================================='''
#devoire N7
import csv
import json
class contact:
    groupe=[]
    def __init__(self,a,b,c,d,e):
        self.nom=a
        self.prenom=b
        self.tele=c
        self.numero=d
        self.email=e
    def __str__(self):
        return "nom",self.nom,"prenom",self.prenom,"telephone",self.tele,"numero",self.numero,"email",self.email
    def modifier_telephone(self,nvnum):
        self.numero=nvnum
        print("Votre nouveau telephone est:",nvnum)
    def modifier_email(self,nvemail):
        self.email=nvemail
        print("Votre nouveau email est:",nvemail)
    def ajouter_groupe(self,nvgroupe):
        self.groupe.append(nvgroupe)
        print("Votre nouveau groupe est:",nvgroupe)
    def suprimer_groupe(self,groupe):
        if groupe in self.groupe:
            self.groupe.remove(groupe)
            print("Le groupe supprimer est:",groupe)
    def enregistrer(self,nom_fichier,format_fichier):
        contact = {'nom': self.nom,'prenom': self.prenom,
            'telephone':self.tele,
            'numero': self.numero,
            'email':self.email,
            'groupe': self.groupe}
        if format_fichier!='json' and format_fichier!='csv' and format_fichier!='texte':
            print("le format de fichier n'est pas valide")
        elif format_fichier=="txt":
            with open(nom_fichier,'w') as f:
                f.write("Nom : ",self.nom,"\n")
                f.write("Prenom :", self.prenom,"\n")
                f.write("Telephone: ",self.tele,"\n")
                f.write("Numero: ",self.numero,"\n")
                f.write("Email: ",self.email,"\n")
        elif format_fichier=='json':
            with open(nom_fichier,'w') as f:
                json.dump(contact,f)
        elif format_fichier=='csv':
            with open(nom_fichier,'w') as f:
                writer=csv.DictWriter(f,contact)
                writer.writeheader()
                writer.writerow(contact)
        else:
            print("Format de fichier non supporté.Utilisez 'json', 'csv' ou 'texte'")
    def charger(self,nom_fichier,format_fichier):
        if format_fichier!='json' and format_fichier!='csv' and format_fichier!='txt':
            print("le format de fichier n'est pas valide")
        elif format_fichier=='json':
            with open(nom_fichier,'r') as f:
                contact=json.load(f)
                print(contact)
        elif format_fichier=='csv':
            with open(nom_fichier,'r') as f:
                contact=csv.DictReader(f)
                for row in contact:
                    print(row)
        elif format_fichier=='txt':
            with open(nom_fichier,'r') as f:
                print(f.read())
                
        else:
            print("Format de fichier non supporté.Utilisez 'json', 'csv' ou 'texte'")
    def supprimer(self):
        del self
c=contact("mohamed","ali","0666666666","123456789","nader@gmail.com")
print(c.__str__())
c.ajouter_groupe("famille")
c.ajouter_groupe("amis")
c.suprimer_groupe("amis")
c.enregistrer("contact","txt")
c.charger("contact","txt")

'''===================================='''
