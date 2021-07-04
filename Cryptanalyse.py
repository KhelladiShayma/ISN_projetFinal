#Programme de déchiffrement
import sys #pour arreter le programme
from sys import stdout #pour pouvoit l'utiliser pour réecrire le message sur la même ligne



def decrypterCaractere (caractere, a, b): #On définit la fonction qui va permettre de calculer les nouvelles valeurs du message codé
    valeurCaractere = alphabet[caractere]
    
    y = (inverse(a)*(valeurCaractere-b))%26

    return list(alphabet.keys())[list(alphabet.values()).index(y)]

def inverse(a): #On définit la fonction qui calcule l'inverse modualire de a 
    x=0
    while(a*x%26!=1):
         x = x+1
    return x


    

alphabet={"a":0, "b":1, "c":2,"d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, #On définit notre alphabet, le même que tout à l'heure
          "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17,
          "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}



# ***

mes=input("Entrer le message à déchiffrer :")
mes=mes.lower() #Pour que l'intégralité de notre message soit en miniscule conformément à notrea alphabet
a=int(input('Entrer la 1ère clef de chiffrement qui a servit à coder votre message :'))#On demande à l'utlisateur d'entrer la première clef de chiffrement
b=int(input('Entrer la 2ème clef de chiffrement qui a servit à coder votre message :'))#Pareil pour b (deuxième clef)


if a==1 or a==3 or a==5 or a==7 or a==9 or a==11 or a==15 or a==17 or a==19 or a==21 or a==23 or a==25: #On vérifie que a et b sont bien conformes à ce qu'on demandait
    pass
else:
    print ("Votre nombre a n'est pas premier avec 26, revérifiez que c'est la bonne clef de chiffrement !")
    exit() #on vérifie la cohérence de a
    
if b<26:    
    pass
else:
    print ("Votre nombre b n'est pas inférieur à 26, revérifiez que c'est la bonne clef de chiffrement !")
    exit() #on vérifie la cohérence de b
    

message_dechiffrer = "" #On crée la liste qui acceuillera nos nouvelles valeurs
for caractereCourant in mes:
    message_dechiffrer += decrypterCaractere(caractereCourant, a, b)

print( message_dechiffrer )

exit()










