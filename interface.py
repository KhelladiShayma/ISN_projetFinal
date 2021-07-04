from tkinter import *
from math import *


# ***

alphabet={"a":0, "b":1, "c":2,"d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9,
          "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17,
          "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}



# Chiffre le message mes à l'aide des clés a et b
def chiffrerAffine(mes, a, b):
    a = int(a)
    b = int(b)
    mes=mes.lower()
    message_chiffrer = ""
    for caractereCourant in mes:
        valeurCaractere = alphabet[caractereCourant]
        y = ( (a*valeurCaractere) +b)%26
        nouveauCaractere = list(alphabet.keys())[list(alphabet.values()).index(y)]
        message_chiffrer += nouveauCaractere
    
    return message_chiffrer

def chiffrerVigenere (mes, a) :
    mes = mes.lower()
    mes = mes.translate(remove_accents)
    lm = len(mes)
    
    if len(a) == 0 :
        print("la clé doit être strictement supérieur à 0"); exit()
    
    for i in range (0,len(mes)) :
        lettre=mes[i]
        if ((ord(lettres)>64) and (ord(lettre)<91)) - 65:
                decalage=ord(a[i])-65
                numero=(ord(lettres)-65+decalage)%26
                mes+= chr(numero+65)
        else :
                code = lettre
                mes+=code
    return mes

    print ("crypt")
def chiffrerCesar (mes, a) :
    a= int(a)
    nouveautexte=""
    for i in range(0,len(mes)) :
        y=ord(mes[i])-65 
        y=(y+a)%26 
        y=chr(y+65)
        nouveautexte=nouveautexte+y
    return nouveautexte

def chiffrerSpartiate (mes, a) :
    a=int(a)
    nouveaumessage=""
    for i in range(0,a):
        j=0
        while i+j<len(mes) :
            n=mes[i+j]
            j+=a
            nouveaumessage+=n
    return nouveaumessage
    
    

# Déchiffre le message mes à l'aide des clés a et b
def dechiffrerAffine(mes, a, b):
    a = int(a)
    b = int(b)
    mes=mes.lower()
    message_dechiffrer = ""
    for caractereCourant in mes:
        valeurCaractere = alphabet[caractereCourant]
        x=0
        while(a*x%26!=1):
             x = x+1
        y = (x*(valeurCaractere-b))%26
        message_dechiffrer += list(alphabet.keys())[list(alphabet.values()).index(y)]
        
    return message_dechiffrer

def dechiffrerCesar (mes,a):
    a=int(a)
    mes=mes.lower()
    nouveautexte= ""
    for j in range(1,26):
        for i in range(0,len(mes)):
            y=ord(mes[i])
            y=((y+j)-65)%26
            nouveautexte=nouveautexte+chr(y+65)
    return nouveautexte
def dechiffrerVigenere (mes, a):
    decrypt = decrypt.lower()
    decrypt = decrypt.translate(remove_accents)
    lm=len(crypt)
    if len(a) == 0 :
        print("la clé doit être strictement supérieur à 0"); exit()
    
    for i in range (lm) :
        lettre=crypt[i]
        if ((ord(lettres)>64) and (ord(lettre)<91)) + 65:
                decalage=ord(a[i])+65
                numero=(ord(lettres)+65+decalage)%26
                crypt+= chr(numero-65)
        else :
                code = lettre
                decrypt=decrypt+code
    return decrypt


def dechiffrerSpartiate (mes, a) :
    
    a=int(a)
    num_col=int(math.ceil(len(mes) // a+1))
    num_rows=a
    num_empty =(num_col*num_rows) - len(mes)
    decrypted =['']*num_col
    col=0
    row=0
    for car in mes:
        decrypted[col]+=car
        col+=1
        if (col==num_col) or (col==num_col - 1 and row >= num_rows - num_empty):
            col=0
            row+=1
    return decrypted

def chiffrer():
    resultat.delete(0, "end") #On supprime l'ancier message qu'il restait
    if a.get()=='' or b.get()=='' or mes.get()=='' : #On vérifie que tous les champs sont remplis
            notification_erreur.pack()
    else : #On modifie nos strings obtenus pour qu'ils deviennent des entiers
        h=int(a.get())
        d=int(b.get())

        if methodeChiffrement.get()==1 : #On décrit les vérifications à faire pour lancer le programme de chiffrement choisit par l'utilisateur s'il y en a 
        
           if h==1 or h==3 or h==5 or h==7 or h==9 or h==11 or h==13 or h==15 or h==17 or h==19 or h==21 or h==23 or h==25:
               if d<26:
                    resultat.insert(0, chiffrerAffine(mes.get(), h, d))
               else:
                    resultat.insert(0, "Votre nombre b est supérieur à 26, recommencez!")
           else:
                resultat.insert(0, "Votre nombre A n'est pas premier avec 26 !")

        elif methodeChiffrement.get()==2 :
             resultat.insert(0, chiffrerVigenere(mes.get(), h))

        elif methodeChiffrement.get()==3 :
             resultat.insert(0, chiffrerCesar(mes.get(), h))

        else :
             resultat.insert(0, chiffrerSpartiate(mes.get(), h))
    
    


    
        
       

#
def dechiffrer(): # On fait la même chose que pour la fonction chiffrer
   resultat.delete(0, "end")

   if a.get()=='' or b.get()=='' or mes.get()=='' :
            notification_erreur.pack()
   else : 
        h=int(a.get())
        d=int(b.get())

        if methodeChiffrement.get()==1 : #On décrit les vérifications à faire pour lancer le programme de chiffrement choisit par l'utilisateur s'il y en a 
        
           if h==1 or h==3 or h==5 or h==7 or h==9 or h==11 or h==13 or h==15 or h==17 or h==19 or h==21 or h==23 or h==25:
               if d<26:
                    resultat.insert(0, dechiffrerAffine(mes.get(), h, d))
               else:
                    resultat.insert(0, "Votre nombre b est supérieur à 26, recommencez!")
           else:
                resultat.insert(0, "Votre nombre A n'est pas premier avec 26 !")

        elif methodeChiffrement.get()==2 :
            resultat.insert(0, dechiffrerVigenere(mes.get(), h))

        elif methodeChiffrement.get()==3 :
            resultat.insert(0, dechiffrerCesar(mes.get(), h))

        else :
            resultat.insert(0, dechiffrerSpartiate(mes.get(), h))

# ***
fenetre=Tk() #On ouvre une fenêtre tKinter
                        
methodeChiffrement = IntVar() #permet de rassembler plusieurs boutons radio sous une seule variable d'entiers
methodeChiffrement.set(1)



# Message à chiffrer / déchiffrer
Label(fenetre, bg="pink", font="helvetica 16 italic", text="Saisir le message :").pack(padx=3, pady=3) #Création d'un message 
mes = Entry(fenetre, width=50) #Création d'une zone de texte ...
mes.pack() #... qu'on affiche directement


# Clés de chiffrement et de déchiffrement (a et b)

Label(fenetre, bg="pink", text="Saisir a :").pack()
a=Entry(fenetre)
a.pack()
Label(fenetre, bg="pink", text="Saisir b :").pack()
b = Entry(fenetre)
b.pack()


# Méthodes de chiffrement
Label(fenetre, bg="pink", font="helvetica 16 italic", text="Choisir la méthode de chiffrement :").pack(padx=3, pady=3) #On va définir les bouttons radios rassemblés sous une seule variable methodeChiffrement
Radiobutton(fenetre, bg="pink", text="Affine", variable=methodeChiffrement, value=1).pack()
Radiobutton(fenetre, bg="pink", text="Vigenère", variable=methodeChiffrement, value=2).pack()
Radiobutton(fenetre, bg="pink", text="César", variable=methodeChiffrement, value=3).pack()
Radiobutton(fenetre, bg="pink", text="Spartiate", variable=methodeChiffrement, value=4).pack()

# Bouttons pour chiffrer / Déchiffrer
Button(fenetre, bg="white", text="Chiffrer", borderwidth= 5, command=chiffrer).pack(padx=5, pady=5)
Button(fenetre, bg="white", text="Déchiffrer", borderwidth= 5, command=dechiffrer).pack(side=TOP, padx=5, pady=5)

# Resultat du chiffrement / déchiffrement
resultat = Entry(fenetre, width=50)
resultat.pack(padx=10, pady=10)

# Notification d'erreur lorsque tous les champs ne sont pas remplis
notification_erreur = Label(fenetre, text=" Tous les champs ne sont pas remplis !! ")

fenetre.mainloop() 
