def comptesPoints(mot,points):
    val=0
    for lettre in mot:
        val=val+points[lettre]
    return val

def nbConsonnes(mot,points):
    voyelles=["A","E","I","O","U","Y"]
    voy=0
    nbr1=0
    cons=0
    nbr2=0
    for lettre in mot:
        if lettre in voyelles:
            voy=voy+points[lettre]
            nbr1=nbr1+1
        else:
            cons=cons+points[lettre]
            nbr2=nbr2+1
    return [voy,cons,nbr1,nbr2]

def progPrincipal():
    points_lettres={"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8
,"K":10,"L":1,"M":2,"N":1,"O":1,"P":3,"Q":8,"R":1,"S":1,"T":1,"U":1,"V":4,"W":10,"X":10,"Y":10,"Z":10}
    mot_u=input("Veuillez entrer un mot\n")
    mot_up=mot_u.upper()
    Points=comptesPoints(mot_up,points_lettres)
    print("Le mot ",mot_u,"fait ",Points," points")
    voyelles,consonnes,nb1,nb2=nbConsonnes(mot_up,points_lettres)
    print("Le mot ",mot_u,"contient ",nb1," voyelles")
    print("Le mot ",mot_u,"contient ",nb2," consonnes")
    print("Le mot ",mot_u,"fait ",voyelles," points en voyelles")
    print("Le mot ",mot_u,"fait ",consonnes," points en consonnes")
    
if(__name__=="__main__"):
    progPrincipal()