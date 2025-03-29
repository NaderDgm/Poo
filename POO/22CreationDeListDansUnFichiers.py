f=open('Lesnotes.txt',mode="r")
t=[]
for x in f:
    t.append(x.strip())
f.close()
print(t)
for i in t:
    if float(i)<10:
        print("tres mal :",i)
    if float (i)>=10 and float(i)<12:
        print("passable :",i)
    if float(i)>12:
        print("tres bien :",i)