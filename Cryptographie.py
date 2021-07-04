import sys #pour arreter le programme
from sys import stdout #pour pouvoit l'utiliser pour réecrire le message sur la même ligne



# 
def crypterCaractere(caractere, a, b):
    valeurCaractere = alphabet[caractere]
    y = ( (a*valeurCaractere) +b)%26
    nouveauCaractere = list(alphabet.keys())[list(alphabet.values()).index(y)]
    
    return nouveauCaractere


alphabet={"a":0, "b":1, "c":2,"d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9,
          "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17,
          "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}

# ***

mes= input("Entrer le message à chiffrer :") #On demande à l'utilisateur de rentrer le message qu'il souhaite chiffrer
mes = mes.lower() #On met en miniscules l'intégralité du message pour vérifier qu'il soit compatible avec l'aphabet décrit plus haut

a= int(input("Entrer la 1ère clef de chiffrement (a étant un nombre premier avec 26) :"))
b= int(input("Enter la 2ème clef de chiffrement b (b étant un nombre premier avec 26) :"))

if a==1 or a==2 or a==3 or a==5 or a==7 or a==11 or a==15 or a==13 or a==17 or a==19 or a==21 or a==23 or a==25: #On vérifie que a est un nombre premier avec 26 pour que le code affine puisse fonctionner
    pass
else :
    print ("Votre nombre a n'est pas premier avec 27")
    exit()

if b==1 or b==2 or b==3 or b==5 or b==7 or b==11 or b==13 or b==17 or b==19 or b==23:#On vérifie que b est un nombre premier avec 26 pour que le code affine puisse fonctionner
    pass
else :
    print ("Votre nombre b n'est pas premier avec 27")
    exit()

message_chiffrer = "" #On crée une liste vide pour pouvoir y insérer les valeurs qui vont correspondre aux lettres pouvant construire le nouveau message
x=0
for caractereCourant in mes: #On modifie les valeurs des clés pour ainsi les chiffrer et accéder aux nouvelles valeurs qui coderont le nouveau message
    #ON PREND TOUTES LES X POUR Y ASSOCIER TOUTES LES NOUVELLES VALEURS CORRESPONDANTES
    message_chiffrer = message_chiffrer + crypterCaractere(caractereCourant, a, b) #On ajoute 

print(message_chiffrer)
exit()





    #dict[k]=x #On relève une valeur d'une clé #PROBLEME ICI CAR LA VALEUR DE X N EST PAS RELEVEE CE QUI FAIT QUE AxX=0
    # alphabet[k]=x
    #y=a*x+b # On la modifie selon le a et le b entrés par l'utilisateur
    #k+=1
    #message_chiffrer.append(y)  #On entre cette nouvelle valeur dans une nouvelle liste
#print (message_chiffrer)


    

#message_chiffre=[] #On initialise une nouvelle liste
#i=0
#for i in range(len(message_chiffrer)):#On crée une boucle pour retirer les nouvelles valeurs modifiées et les faire correspondre à de nouvelles lettres du nv message
 #   d_inv[i] #On récupère la clé de la valeur correspondante
  #  message_chiffre.append #On l'ajoute à la nouvelle liste
   # i+=1

#print (message_chiffre)
#PROBLEMES RENCONTRES :
       #AFFICHER TOUT LE MESSAGE EN MINUSCULES CONFORMEMENT AUX LETTRES DU DICTIONNAIRES CHOISIES
       #RECUPERER LES VALEURS DES CLES DU MESSAGE QUE L ON DOIT CODER
       #CHOIX ENTRE DICTIONNAIRE OU LISTE POUR Y INSERER LES NOUVELLES VALEURS DES CLES CORRESPONDANTES DEJA MODIFIEES
       #AFFICHER TOUT LE MESSAGE DANS SON INTEGRALITE SUR LA MEME LIGNE
       #RECUPERER LES CLES DES VALEURS UNE FOIS MODIFIEES ETANT DONNE QU UN DICTIONNAIRE N EST PAS FAIT POUR SA AU DEPART
       #ARRIVER A FAIRE CORRESPONDRE LES VALEURS AVEC LES CLES CORRESPONDANTES AVEC DES VALEURS EXISTANTES DONC EN UTILISANT MODULO 26
       #Pour a=0 comment chiffrer le message?
       
