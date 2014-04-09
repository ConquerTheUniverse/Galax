from tkinter import *
from Classes import *
import random

class Modele:
    def __init__(self, parent):
        self.parent = parent
        #Pour une surface de 1000x800 px ou les etoiles sont des cases de 10 x 10 px
        self.surfaceX = 100
        self.surfaceY = 80
        self.nbEtoiles = 0
        self.listeEtoiles = []
        #Creation d'un objet pour chaque faction pour savoir differentes informations sur chacune de celle-ci
        self.humain = Humain()
        self.gubrus = Gubrus()
        self.czin = Czin()

    #Permet de creer toutes les etoiles au debut de la partie
    def creerEtoiles(self):
        #Creer un nombre d'etoile aleatoire entre 50 et 70
        self.nbEtoiles = random.randint(50,70)

        #Vider les anciennes valeurs de la liste si il y en a
        self.listeEtoiles[:] = []

        #Creer le nombre d'etoile en fonction de la variable nbEtoiles(50 a 70)
        for i in range(1, self.nbEtoiles):
       

            
            #Permet de determiner si il y a une etoile a proximite, voir plus bas
            aProximite = True

            #Permet de creer une nouvelle position aleatoire tant que les etoiles sont trop proches
            while(aProximite)

                aProximite= False
                
                #Valeur aleatoire en X pour une etoile
                x = random.randint(0, self.surfaceX-1)
                #Valeur aleatoire en Y pour une etoile
                y = random.randint(0, self.surfaceY-1)
                
                    
                #Assurer que les etoiles ne soit pas directement les unes a cote des autres
                for j in listeEtoiles:
                    #Permet de regarder si la valeur absolue de la soustraction des deux positions est plus petite que 10 ex:abs(6-9)=3 et abs(9-6)=3
                    if (abs(x-j.posX)<10 && abs(y-j.posY)<10):
                        aProximite = True
                        break; #Permet de sortir du for des qu'il y a une etoile trop proche


            #Lorsqu'on reussit a trouver un x et un y qui est a la bonne distance on cree l'etoile a cette position 
            nbM = random.randint(4,10) #Nombre aleatoire de Manufactures entre 4 et 10
            self.listeEtoiles.append(x, y, nbM, 0)

    #Fonction permettant de creer une etoile-mere pour chacune des factions(Humains, Grubus et Czin)         
    def assignerLesEtoilesMeres(self):
        pass
                
                
            
        
        

class Vue:
    def __init__(self, parent):
        self.parent = parent #Pour l'heritage provenant du Controleur

    #Afficher le menu principal
    def afficherMenu:
        pass
    
    #Afficher les instructions pour le jeu
    def instructions
        pass

    #Afficher le menu des options pour le jeu
    def options
        pass

    #Affichage de la surface de jeu dans la fenetre
    def afficherJeu:
        pass

    
    

class Controleur:
    def __init__(self):
        pass
