# les bases de python

a="Bonjour a tout le monde"
b="comment allez vous ?"
f=a[0:10]
print(a)
print(f)
print(b.lower())
print(b.capitalize())
c="192.168.1.1"
d=c.split(".")
print(d, end='\n')

#Cours sur les liste

e=[1,2,3,4,5,6,7,8,9]
print(e[2:6])
print(e[::1])
e[3]=14
print(e)
e1=[1,1.4,"text",[12,15,18,19]]
print(len(e1))
print(e1[2])
print(e1[3])
print(e1[3][2])
print(e1[::-1])
e3=[1,2,3,4,5,6,7,8,9,4]
e3.append(10)
print(e3)
e4=e3.copy()
print(e4)
e3 [3]=14 # attention ne garde pas en memoire
print(e3)
print(e4)
print(e4.count(4))
print(e4.index(4))
print(e4.index(8))
print(e4.index(4,4))
e4.sort()   # ordre croisant
print(e4)
e4.pop()    # efface la derniere de la liste
print(e4)
e4.reverse() # inverse une liste
print(e4)
e4.insert(5,32) # insersion dans un liste 
print(e4)



# dictionnaire 

d={"pomme":1,"poires":1.3,"kiwi":2,"coco":3.4}
print(len(d))
print(d["pomme"])
d["datte"]=2.1
print(d)
print(d.values())
print(d.keys())

# condifion 

# if (condition):
# condition :
# == egalite
# != egale
# > superieur
# < inferieur
# >= superieur ou egal 
# <= inferieur ou egal 
w=20
if (w>10):
    w-1
    print(w)
else: 
     print(w)

for var in "Bonjour tous le monde\n":
    print(var,end=' ')

print("\n")

for var1 in [1,2,3,4,5,6,7,8,9,"texte"]:
    print (var1,end=(" "))
    
print("\n")

for var3 in range (1,255):
    print(var3,end=".")

print("\n")


d={"voiture": "véhicule à quatre roues", "vélo": "véhicule à deux roues"}
for var,var1 in d.items():
    print("var :",var)
    print("var1 :",var1)
print("="*20)
for var in d.items():
    print("var :",var)


print("\n")

import time
x=1
while(x<10):
    print(x)
    if (x==5):
        x=x+2
        continue
    x=x+1
    time.sleep(0.5)

#definition 
def madefinition(nb1,nb2):
    result=nb1**2
    result2=nb2*100
    return result,result2



n=int(input("entre un nombre:\n"))
l=int(input("entre un deuxieme nombre:\n"))
resultat1=madefinition(n,l)

print(resultat1)

