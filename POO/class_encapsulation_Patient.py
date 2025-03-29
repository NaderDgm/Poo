class Patient:
    def __init__(self, nom, age, diagnostic):
        self.__nom = nom
        self.__age = age
        self.__diagnostic = diagnostic
        self.__poids = None
        self.__taille = None
        self.__symptomes = []

    # Méthodes d'accès (Getters)
    def getNom(self):
        return self.__nom

    def getAge(self):
        return self.__age

    def getDiagnostic(self):
        return self.__diagnostic

    def getPoids(self):
        return self.__poids

    def getTaille(self):
        return self.__taille

    # Méthodes de modification (Setters)
    def setNom(self, nom):
        self.__nom = nom

    def setAge(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Erreur : L'âge doit être un nombre positif.")

    def setDiagnostic(self, diagnostic):
        self.__diagnostic = diagnostic

    def setPoids(self, poids):
        if poids > 0:
            self.__poids = poids
        else:
            print("Erreur : Le poids doit être un nombre positif.")

    def setTaille(self, taille):
        if taille > 0:
            self.__taille = taille
        else:
            print("Erreur : La taille doit être un nombre positif.")

    # Calcul de l'IMC
    def calculIMC(self):
        if self.__poids is not None and self.__taille is not None:
            return self.__poids / (self.__taille ** 2)
        else:
            print("Erreur : Poids et taille doivent être définis pour calculer l'IMC.")
            return None

    # Ajouter un symptôme
    def ajouterSymptome(self, symptome):
        self.__symptomes.append(symptome)

    # Afficher les informations du patient
    def afficherInfos(self):
        print(f"Nom : {self.__nom}")
        print(f"Âge : {self.__age}")
        print(f"Diagnostic : {self.__diagnostic}")
        if self.__poids and self.__taille:
            print(f"IMC : {self.calculIMC():.2f}")
        else:
            print("IMC : Non calculé (poids ou taille manquant)")
        if self.__symptomes:
            print(f"Symptômes : {', '.join(self.__symptomes)}")
        else:
            print("Symptômes : Aucun")

# Exemple d'utilisation
patient = Patient("Riad", 40, "Asthme")
patient.setPoids(60)
patient.setTaille(1.65)
patient.ajouterSymptome("Essoufflement")
patient.ajouterSymptome("Toux persistante")
patient.afficherInfos()