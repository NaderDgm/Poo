class House:
    AdressM=""
    nbChanmbre=0
    def __init__(self,a,b):
        self.AdressM=a
        self.nbChambre=b
Obj1=House("Hay al Menzah",10)
print(Obj1.AdressM)
print(Obj1.nbChambre)