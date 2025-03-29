class Car:
    Matricule=0
    Marque=""
    Model=0
    def __init__(self,a,b,c):
        self.Matricule=a
        self.Marque=b
        self.Model=c
    def Afficher_Infos(self):
        print(self.Matricule,self.Marque,self.Model)
obj1=Car(6483236,"BMW",2020)
obj1.Afficher_Infos()
