class GestionÉtudiants:
    __nom=""
    __age=0
    __notes=0
    __nbnotes=0
    def setAge(self,age):
        if age > 0:
            self.__age = age
        else:
             print("ERR")
    def ajouterNote(self):
        if self.__notes>20 and self.__notes<0 :
            print("ERR")
    def calculMoyenne(self):
        return  self.__notes * self.__nbnotes 
    def analysePerformance(self):
        for m in GestionÉtudiants:
            if float(m)<10:
                print("Insuffissant :",m)
                if float (m)>=10 and float(m)<12:
                    print("passable :",m)
                    if float(m)>12:
                        print("tres bien :",m)
    def Afficher_Details(self):
        print(self.__notes)
        print(self.calculMoyenne())
        print(self.analysePerformance())
obj1=GestionÉtudiants("Riad",18,3)
print(obj1.Afficher_Details())