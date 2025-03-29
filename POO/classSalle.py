class salle:
    numSalle=0
    etageSalle=0
    capaciterSalle=0
    def __init__(self,a,b,c):
        self.numSalle=a
        self.etageSalle=b
        self.capaciterSalle=c
obj1=salle(5,2,20)
print(obj1.numSalle)
print(obj1.etageSalle)
print(obj1.capaciterSalle)