# Ce programme à pour but de refaire le jeu crucial Test.

# import tkinter as Tk
import random

score = []
nb_joueur = 0
J = -1
lst_joueur = []

def choix_joueur():
    print("Tapez 1 pour sciences")
    choix = int(input())
    question_choix(choix)

def question_choix(choix):
    '''fonction qui va chercher une question du test en faisant attention au choix'''
    reponse = 0
    quest = 0
    if choix == 1:
        quest = question_sciences() #apprends la liste des questions
        alea = random.randint(0, 1)
        print("Question : ", quest[alea])  # ecrit une question de facon aléatoires 
        reponse = str(input())
        reponse_sciences(reponse, alea)

def question_sciences():
    '''stock les questions sciences'''
    quest = ["Quel est le symbole atomique du soufre ?", "Quelle particule est neutre ?"]
    return(quest)

def reponse_sciences(reponse, alea):
    '''stock les réponses sciences'''
    global score
    reponses_sciences = ["S","neutron"]
    if reponses_sciences[alea] == reponse:
        score[J] = score[J]+1
        print("Score : ", score[J])
        return score
    else:
        score[J] = score[J]
        print("Score : ", score[J])
        return score
    
def joueur():
    global nb_joueur
    global lst_joueur
    print("Combien de joueur êtes vous ?")
    nb_joueur = int(input())
    print("Donnez le nom des joueurs")
    for loop in range(nb_joueur):
        nom = str(input())
        lst_joueur.append(nom)
        score.append(0)
    print(lst_joueur)
    return nb_joueur

def jeu():
    '''fonction lancant le jeu'''
    global J
    global nb_joueur
    global score
    t = 0
    joueur()
    print("Combien voulez vous de tour ?")
    nb_tour = int(input())
    nb_tour = nb_tour*nb_joueur
    for loop in range(nb_tour):
        for nb in range(len(lst_joueur)):
            while t <= nb_tour:
                t +=1
                if J < nb_joueur-1:
                    J += 1
                    print(lst_joueur[J], ", à vous de jouer")
                    choix_joueur()
                elif J >= nb_joueur or J <= nb_joueur and t <= nb_tour:
                    J = -1
                    J += 1
                    print(lst_joueur[J], ", à vous de jouer")
                    choix_joueur()
                else:
                    print("Parti fini")
                    print("Voulez vous voir les scores")
                    tab = str(input())
                    if tab == "oui":
                        maNouvelleListe = list(zip(lst_joueur, score))
                        print(maNouvelleListe)
                    print("Voulez vous rejouez ?")
                    demande = str(input())
                    if demande == "oui":
                        jeu()
                    else:
                        print("au revoir")


jeu()
