# Ce programme à pour but de refaire le jeu crucial Test.

# import tkinter as Tk
import random

score = 0
nb_joueur = 0

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
    quest = ["Quel est le symbole atomique du souffre ?", "Quelle particule est neutre ?"]
    return(quest)

def reponse_sciences(reponse, alea):
    '''stock les réponses sciences'''
    global score
    reponses_sciences = ["S","neutron"]
    if reponses_sciences[alea] == reponse:
        score = score + 1
        print("Score : ", score)
    else:
        score = score
        print("Score : ", score)
#     
# def joueur():
#     global nb_joueur
#     print("Combien de joueur êtes vous ?")
#     nb_joueur = 
# def point():
#     '''compte les points'''
#     
# 
# 
# def jeu():
#     '''fonction lancant le jeu'''
choix_joueur()