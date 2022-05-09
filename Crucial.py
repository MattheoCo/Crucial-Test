# Ce programme à pour but de refaire le jeu crucial Test.

# import tkinter as Tk
import random

score = []
nb_joueur = 0
J = -1
lst_joueur = []

def choix_joueur():
    q1= random.randint(1, 5)
    q2= random.randint(1, 5)
    q3= random.randint(1, 5)
    while q2 == q1 and q3 == q2:
        q2= random.randint(1, 5)
    while q3 == q1 and q3 == q2:
        q3= random.randint(1, 5)
    if q1 == 1 or q2 == 1 or q3 == 1:
        print("Tapez 1 pour sciences")
    if q1 == 2 or q2 == 2 or q3 == 2:
        print("Tapez 2 pour Mathématiques")
    if q1 == 3 or q2 == 3 or q3 == 3:
        print("Tapez 3 pour Histoire")
    if q1 == 4 or q2 == 4 or q3 == 4:
        print("Tapez 4 pour Géographie")
    if q1 == 5 or q2 == 5 or q3 == 5:
        print("Tapez 5 pour Francais")
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
    elif choix == 2:
        quest = question_maths() #apprends la liste des questions
        alea = random.randint(0, 1)
        print("Question : ", quest[alea])  # ecrit une question de facon aléatoires 
        reponse = str(input())
        reponse_maths(reponse, alea)
    elif choix == 3:
        quest = question_hist() #apprends la liste des questions
        alea = random.randint(0, 1)
        print("Question : ", quest[alea])  # ecrit une question de facon aléatoires 
        reponse = str(input())
        reponse_hist(reponse, alea)
    elif choix == 4:
        quest = question_geo() #apprends la liste des questions
        alea = random.randint(0, 1)
        print("Question : ", quest[alea])  # ecrit une question de facon aléatoires 
        reponse = str(input())
        reponse_geo(reponse, alea)
    elif choix == 5:
        quest = question_francais() #apprends la liste des questions
        alea = random.randint(0, 1)
        print("Question : ", quest[alea])  # ecrit une question de facon aléatoires 
        reponse = str(input())
        reponse_francais(reponse, alea)

def question_sciences():
    '''stock les questions sciences'''
    quest = ["Quel est le symbole atomique du soufre ?", "Quelle particule est neutre ?"]
    return(quest)

def question_maths():
    '''stock les questions math'''
    quest = ["Quel théorème permet d'avoir l'hypothénuse ?", "Apres milliard il y'a ..."]
    return(quest)

def question_hist():
    '''stock les questions histoires'''
    quest = ["Qui s'est fait décapiter le 16 Mai 68", "Quand se fini la seconde guerre mondiale ?"]
    return(quest)

def question_geo():
    '''stock les questions geo'''
    quest = ["Quelle est la capital de la Suisse ?", "A qui appartient le groenland ?"]
    return(quest)

def question_francais():
    '''stock les questions francais'''
    quest = ["Pluriel du mot vitrail", "La pizza de vito est pour ses/ces parents."]
    return(quest)

def reponse_sciences(reponse, alea):
    '''stock les réponses sciences'''
    reponses = ["s","neutron"]
    score_game(reponses, reponse, alea)

def reponse_maths(reponse, alea):
    '''stock les réponses maths'''
    reponses = ["Pythagore","billion"]
    score_game(reponses, reponse, alea)

def reponse_hist(reponse, alea):
    '''stock les réponses histoire'''
    reponses = ["Louis 16","1945"]
    score_game(reponses, reponse, alea)
    
def reponse_geo(reponse, alea):
    '''stock les réponses geo'''
    reponses = ["Berne","Danemark"]
    score_game(reponses, reponse, alea)

def reponse_francais(reponse, alea):
    '''stock les réponses geo'''
    reponses = ["vitraux","ses"]
    score_game(reponses, reponse, alea)
    
    
def score_game(reponses, reponse, alea):
    '''calcule le score'''
    global score
    if reponses[alea] == reponse:
        score[J] = score[J]+1
        print("Score : ", score[J])
        return score
    else:
        score[J] = score[J]
        print("Score : ", score[J])
        return score
    
def joueur():
    global score
    global nb_joueur
    global lst_joueur
    print("Bienvenue sur Crucial Test !!")
    print("Voulez vous lire les règles ?")
    reglement = str(input())
    if reglement == "oui":
        regle()
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
                        score_joueur = list(zip(lst_joueur, score))
                        print(score_joueur)
                        classement()
                    print("Voulez vous rejouez ?")
                    demande = str(input())
                    if demande == "oui":
                        jeu()
                    else:
                        print("au revoir")

def classement():
    

def regle():
    print("Voici les règles du Crucial Test: ")
    print("Vous devrez choisir entre plusieurs thèmes,")
    print("le but est de marquer le plus de points pour remporter.")
    print("Seul les noms propres preinnent une majuscules au début.")
    print("Une réponse court et direct est attendu, exemple :")
    print("Capital de la Suisse?")
    print("Berne")
    print("Donc ne pas faire de longue phrases sinon votre réponse sera fausses.")
    print("Bon jeu")

jeu()

