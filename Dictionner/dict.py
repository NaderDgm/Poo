'''dict1={"cat":"chat","dog":"chien","horse":"cheval"}
dict2=()#dict vide
dict3=dict.copy(dict1)
print(dict1)
print(dict2)
print(dict3)
print(dict1['cat'])
print(dict1.get('cat'))
'''
'''d={"d":1,"text":"nader doghmi",1:"ada","lala":"alala",(1,2,3):[3,2,1]}'''
'''d={1:1,2:2,3:3,4:4}'''
'''for k in d.keys():
    print(k)
    print(d[k])
for v in d.values():
        print(v)'''
'''for x,y in d.items():
      print(x,":",y)'''
'''for x,y in sorted(d.items()):
    print(x,":",y)
'''
''''dict={"cat":"chat","dog":"chien","horse":"cheval"}
dict.update((2,1,3))
print(dict)
'''
'''user={
    "name":"bark obamaa"
    "age":"30"
    "country:"egypt"
    "skills":["html","Css","js"]
    "ratting":10.5
}'''
'''language = {
    "one":{
        "name":"html"
        "progress":"80%"
        },
        "two":{
            "name":"css"
            "progress":"90%"
        },
        "three":{
            "name":"js"
            "progress": "90%"
        }
}
print(language)
print(language['one'])
print(language['Three']['progress'])'''
'''============================================================'''
'''personne={
    "nom":"ali",
    "age":15,
    "ville":"rabat"
}
# 2
for i in personne.keys():
    print(i)
    
personne["age"]=26
personne.update({"profession":"ingenieur"})
for i in personne.keys():
    print(i)
personne.pop('ville')
for k,v in personne.items():
    print(f"{k}:{v}")
    
if "profession" in personne:
    print("up")
else:
    print("non")'''