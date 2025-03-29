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
a=int(input("Nombre 1 :"))
b=int(input("Nombre 2 :"))
s1=somme(a,b)
s1.AFFICHER_INFOS()