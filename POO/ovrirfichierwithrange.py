f = open('a.txt', 'at')
for i in range(10):
    f.write("ligne" + str(i+1) + "/ln") 
f.close()
