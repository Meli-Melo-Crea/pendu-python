#Import du module qui génère l'aléatoire
import random
nb_erreurs = 0
max_erreurs = 7

def afficher_pendu(nb_erreurs):
    if nb_erreurs == 0:
        print(" Potence vide !")
    elif nb_erreurs == 1:
        print(r"""
                  +---+
                  |   |
                  o   |
                      |
                      |
                      |
                 ========= """)
    elif nb_erreurs == 2:
        print(r"""
                 +---+
                 |   |
                 o   |
                 |   |
                     |
                     |
               ========= """)
    elif nb_erreurs == 3:
        print(r"""
                 +---+
                 |   |
                 o   |
                /|   |
                     |
                     |
               ========= """)
    elif nb_erreurs == 4:
        print(r"""
                 +---+
                 |   |
                 o   |
                /|\  |
                     |
                     |
               ========= """)
    elif nb_erreurs == 5:
        print(r"""+---+
                 |   |
                 o   |
                /|\  |
                /    |
                     |
               ========= """)
    elif nb_erreurs == 6:
        print(r"""
                 +---+
                 |   |
                 o   |
                /|\  |
                / \  |
                     |
               ========= """)
    elif nb_erreurs == 7:
        print(r"""
                 +---+
                 |   |
                 x   |
                /|\  |
                / \  |
                     |
               =========""")

mot_a_decouvrir = ["Arias", "Tidus", "Azastus", "Sacrifissia", "Enshrouded", "Bahamut"] #Liste de mot qui seront à découvrir
mot_pioche = random.choice(mot_a_decouvrir) #On choisit un mot au hasard
mot_saisit = [] #Enregistrement des données saisites
jeu_en_cours = True #Interrupteur pour démarrer le jeu

print(" _ " * len(mot_pioche)) #ça va afficher le mot sous forme de _ avec la bonne longueur du mot grace au len()
mot_affiche = ["_"] * len(mot_pioche)  # Liste de _ à remplir



while jeu_en_cours:
#Vérification si la lettre figure dans le mot 
    #Intéraction avec l'user (demande + stockage)
    user_input = input("Entrez une lettre : ").upper()  #upper pour mettre les lettres en majuscule
    mot_pioche = mot_pioche.upper()
    if user_input in mot_saisit:
        print("Vous avez deja proposé cette lettre")
        afficher_pendu(nb_erreurs)
        print(f"Il vous reste {max_erreurs - nb_erreurs} essais")
    else:
        if user_input in mot_pioche:
            print(f"La lettre est dans le mot ❤️")

            for i in range(len(mot_pioche)):
                if mot_pioche[i] == user_input:
                    mot_affiche[i] = user_input #ça va remplacer le _ par la lettre proposée
        else:
            print(f"La lettre n'est pas dans le mot")
            nb_erreurs = nb_erreurs + 1
            afficher_pendu(nb_erreurs)
            print(f"Il vous reste {max_erreurs - nb_erreurs} essais")
            if nb_erreurs == max_erreurs:
                print("Vous avez perdu ! Le mot etait", mot_pioche)
                break
        mot_saisit.append(user_input) #C'est ce qui va enregistrer les lettres proposées
        print(f"Tu as déjà proposé les lettres suivante : {mot_saisit}") #Il annonce les lettres déjà proposées par l'utilisateur
        print(" ".join(mot_affiche))  # Affiche le mot avec les lettres trouvées

    if "_" not in mot_affiche:
        print("Vous avez gagné ! 👌")
        jeu_en_cours = False