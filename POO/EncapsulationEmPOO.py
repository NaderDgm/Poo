class somme:
    __xy=0
    __te=0
    def __init__(self,ft,ou):
       self.__xy=ft
       self.__te=ou
       '''def afficher_infos(self):
           print(self.__xy,self.__te)'''
    def AFFICHER_INFOS(self):
        print(self.__xy,"+",self.__te,"=",self.__somme())
    def __somme(self):
        return self.__xy + self.__te     
s1=somme(125000,500000)
s1.AFFICHER_INFOS()