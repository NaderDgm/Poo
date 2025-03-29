class stg:
    def __init__(self, nom,prenom,note):
        self.nom = nom
        self.prenom = prenom
        self.note = note
    def calcule(self,t):
        s=0
        for el in t:
            s+=el
    def __add__(self,d):
        return self.note+d.note
s1=stg("abdo","doukha", 15)
s2=stg("daniel","khoukha", 15)   
s1.calcule([1])              
print(s1.calcule([1]))
print(s1+s2)
print(s1.__add__(s2))