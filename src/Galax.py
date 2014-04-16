from tkinter import *
import Classes
import random

class Modele:
    def __init__(self, parent):
        self.parent = parent
        #Pour une surface de 1000x800 px ou les etoiles sont des cases de 10 x 10 px
        self.surfaceX = 50
        self.surfaceY = 40
        self.nbEtoiles = 0
        self.listeEtoiles = []
        self.etoileDepart = None
        self.etoileArrivee = None
        #Creation d'un objet pour chaque faction pour savoir differentes informations sur chacune de celle-ci
        self.humain = Classes.Humains()
        self.gubrus = Classes.Gubrus()
        self.czin = Classes.Czins()
        

    #Permet de creer toutes les etoiles au debut de la partie
    def creerEtoiles(self):
        #Creer un nombre d'etoile aleatoire entre 50 et 70
        self.nbEtoiles = random.randint(30,40)

        #Vider les anciennes valeurs de la liste si il y en a
        self.listeEtoiles[:] = []

        #Creer le nombre d'etoile en fonction de la variable nbEtoiles(50 a 70)
        for i in range(1, self.nbEtoiles):
       

            
            #Permet de determiner si il y a une etoile a proximite, voir plus bas
            aProximite = True

            #Permet de creer une nouvelle position aleatoire tant que les etoiles sont trop proches
            while(aProximite):

                aProximite= False
                
                #Valeur aleatoire en X pour une etoile
                x = random.randint(0, self.surfaceX-1)
                #Valeur aleatoire en Y pour une etoile
                y = random.randint(0, self.surfaceY-1)
                print(i)
                
                    
                #Assurer que les etoiles ne soit pas directement les unes a cote des autres
                for j in self.listeEtoiles:
                    #Permet de regarder si la valeur absolue de la soustraction des deux positions est plus petite que 10 ex:abs(6-9)=3 et abs(9-6)=3
                    if (abs(x-j.posX)<2 and abs(y-j.posY)<2):
                        aProximite = True
                        break; #Permet de sortir du for des qu'il y a une etoile trop proche


            #Lorsqu'on reussit a trouver un x et un y qui est a la bonne distance on cree l'etoile a cette position 
            nbM = random.randint(4,10) #Nombre aleatoire de Manufactures entre 4 et 10
            self.listeEtoiles.append(Classes.Etoile(x, y, nbM, 0))

    
        
            

    #Fonction permettant de creer une etoile-mere pour chacune des factions(Humains, Grubus et Czin)         
    def assignerLesEtoilesMeres(self):

        positionOK = False 
        n = random.randint(0,len(self.listeEtoiles))
        print(n)
        
        self.listeEtoiles[n].proprietaire = 1
        self.listeEtoiles[n].niveauInfo = 3

        

        while(positionOK == False):

            n = random.randint(0,len(self.listeEtoiles))
            
            if(self.listeEtoiles[n].proprietaire != 1):
                self.listeEtoiles[n].proprietaire = 2
                self.listeEtoiles[n].nbVaisseaux = 100
                self.listeEtoiles[n].nbManufactures = 10
                positionOK=True
                
            
        positionOK = False
        
        while(positionOK == False):

            n = random.randint(0,len(self.listeEtoiles))
        
            if(self.listeEtoiles[n].proprietaire != 1 and self.listeEtoiles[n].proprietaire != 2):
                self.listeEtoiles[n].proprietaire = 3
                self.listeEtoiles[n].nbVaisseaux = 100
                self.listeEtoiles[n].nbManufactures = 10
                positionOK=True
                
        
            
            
        
        

class Vue:
    def __init__(self, parent):
        self.parent = parent #Pour l'heritage provenant du Controleur
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title("Galax")
        self.width = 1200
        self.height = 800
        self.root.geometry(str(self.width)+"x"+str(self.height))

        
        
        #Images
        self.imageHumains = PhotoImage(file="images/logoHumains.gif")
        self.imageGubrus = PhotoImage(file="images/logoGubrus.gif")
        self.imageCzins = PhotoImage(file="images/logoCzins.gif")
        self.imagePlanete1 = PhotoImage(file="images/planete1.gif")
        self.imagePlanete2 = PhotoImage(file="images/planete2.gif")
        self.imagePlanete3 = PhotoImage(file="images/planete3.gif")
        self.imagePlanete4 = PhotoImage(file="images/planete4.gif")
        #self.backgroundSurface = PhotoImage(file="images/bgSurface.gif")
        self.backgroundMenu = PhotoImage(file="images/bgMenu.gif")

        #Resize des planetes
        self.imagePlanete1 = self.imagePlanete1.subsample(30,30)
        self.imagePlanete2 = self.imagePlanete2.subsample(30,30)
        self.imagePlanete3 = self.imagePlanete3.subsample(30,30)
        self.imagePlanete4 = self.imagePlanete4.subsample(30,30)

        #Elements du menu
        self.backgroundMenu = Label(self.root, image=self.backgroundMenu)
        self.boutonJouer = Button(self.root, text='Jouer',width=50, bg='black', fg='white',activebackground='black', activeforeground='white')
        self.boutonQuitter = Button(self.root, text='Quitter',width=50, bg='black', fg='white',activebackground='black', activeforeground='white', command=self.root.destroy)
        
        #Widgets pour l'affichage du jeu
        self.surfaceJeu = Canvas(self.root, width=1000, height=800, bg='white', highlightthickness=0)
        self.labelHumains = Label(self.root, text="Humains : 1", font=("Arial",16))
        self.labelGubrus = Label(self.root, text="Gubrus : 1", font=("Arial",16))
        self.labelCzins = Label(self.root, text="Czins : 1", font=("Arial",16))
        self.boutonChangerAnnee = Button(self.root, text='Annee Suivante',width=50, bg='black', fg='white',activebackground='black', activeforeground='white')
        


        #Label contenant les images pour le panel sur le cote
        self.imageTempH = self.imageHumains.zoom(1,1)
        self.imageTempH = self.imageTempH.subsample(2,2)
        self.logoHumains = Label(self.root, image=self.imageTempH)
        

        self.imageTempG = self.imageGubrus.zoom(1,1)
        self.imageTempG = self.imageTempG.subsample(2,2)
        self.logoGubrus = Label(self.root, image=self.imageTempG)

        self.imageTempC = self.imageCzins.zoom(1,1)
        self.imageTempC = self.imageTempC.subsample(2,2)
        self.logoCzins = Label(self.root, image=self.imageTempC)

        #Keybinds
        self.surfaceJeu.bind('<Button-1>', self.getMouseClick)
        
        
    #Obtenir le click de souris sur la surface   
    def getMouseClick(self, event):

        self.parent.transmissionMouseClick(event.x, event.y)
            
        

    #Afficher le menu principal
    def afficherMenu(self):
        pass
    
    #Afficher les instructions pour le jeu
    def instructions(self):
        pass

    #Afficher le menu des options pour le jeu
    def options(self):
        pass

    #Affichage de la surface de jeu dans la fenetre
    def afficherJeu(self, modele):
        #Place la surface de jeu
        self.surfaceJeu.place(x=0,y=0)

        #Boucle pour afficher cahcune des etoiles
        for y in range(0, modele.surfaceY):
            for x in range(0, modele.surfaceX):
                for etoile in modele.listeEtoiles:                  
                    if(x == etoile.posX and y == etoile.posY):
                        n = random.randint(1,4)

                        if(n == 1):
                            randomImage = self.imagePlanete1
                        elif(n == 2):
                            randomImage = self.imagePlanete2
                        elif(n == 3):
                            randomImage = self.imagePlanete3
                        elif(n == 4):
                            randomImage = self.imagePlanete4

                        self.surfaceJeu.create_image(x*20,y*20,anchor=NW, image=randomImage, tags="planete")
                        break #Pour sortir du for interne puisqu'il ne peut pas y avoir deux etoiels a la meme position
                        

        #Place les item qui seront sur le coter de la surface
        self.logoHumains.place(x=1000)
        self.labelHumains.place(x=1030, width=170, height=30)

        self.logoGubrus.place(x=1000, y=30)
        self.labelGubrus.place(x=1030, y=30, width=170, height=30)

        self.logoCzins.place(x=1000, y=60)
        self.labelCzins.place(x=1030, y=60, width=170, height=30)

        #Place le bouton pour changer d'annee
        self.boutonChangerAnnee.place(x=1025, y=750, width=150)

    #Affiche les proprietaires sur les planetes
    def afficherProprietaire(self, modele):
        
        self.surfaceJeu.delete("logo")
        
        for etoile in modele.listeEtoiles:
            print(etoile.proprietaire)
            
            if(etoile.proprietaire == 1):
                self.imageHumains = self.imageHumains.subsample(3,3)
                self.surfaceJeu.create_image(etoile.posX*20, etoile.posY*20, anchor=NW, image=self.imageHumains, tags="logo")
            elif(etoile.proprietaire == 2):
                self.imageGubrus = self.imageGubrus.subsample(3,3)
                self.surfaceJeu.create_image(etoile.posX*20, etoile.posY*20, anchor=NW, image=self.imageGubrus, tags="logo")
            elif(etoile.proprietaire == 3):
                self.imageCzins = self.imageCzins.subsample(3,3)
                self.surfaceJeu.create_image(etoile.posX*20, etoile.posY*20, anchor=NW, image=self.imageCzins, tags="logo")

    #Affiche les informations de la planete selectione
    def afficherInformations(self):
        pass
        
            
    

class Controleur:
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self)
        self.modele.creerEtoiles()
        self.modele.assignerLesEtoilesMeres()
        self.vue.afficherJeu(self.modele)
        self.vue.afficherProprietaire(self.modele)
        self.etoileClique = False
        self.vue.root.mainloop()

    
    def transmissionMouseClick(self, x, y):
        
        self.vue.surfaceJeu.delete("selection")

        print(len(self.modele.listeEtoiles))
        for i in range(0, len(self.modele.listeEtoiles)):

            if(self.modele.listeEtoiles[i].posX*20 <= x and self.modele.listeEtoiles[i].posX*20+20 >= x):
                if(self.modele.listeEtoiles[i].posY*20 <= y and self.modele.listeEtoiles[i].posY*20+20 >= y):
                
                    #Si l'etoile de depart n'est pas selectionné
                    if(self.modele.etoileDepart == None):
                        self.vue.surfaceJeu.create_oval(self.modele.listeEtoiles[i].posX*20-10, self.modele.listeEtoiles[i].posY*20-10, self.modele.listeEtoiles[i].posX*20+30, self.modele.listeEtoiles[i].posY*20+30, dash=(4,4), outline='red', tags="selection")
                        self.modele.etoileDepart = i
                        self.etoileClique = True
                        print("trouve")
                        
                    else:
                        self.vue.surfaceJeu.create_oval(self.modele.listeEtoiles[self.modele.etoileDepart].posX*20-10, self.modele.listeEtoiles[self.modele.etoileDepart].posY*20-10, self.modele.listeEtoiles[self.modele.etoileDepart].posX*20+30, self.modele.listeEtoiles[self.modele.etoileDepart].posY*20+30, dash=(4,4), outline='red', tags="selection")
                        if(i != self.modele.etoileDepart):
                            self.modele.etoileArrivee = i
                            self.vue.surfaceJeu.create_oval(self.modele.listeEtoiles[i].posX*20-10, self.modele.listeEtoiles[i].posY*20-10, self.modele.listeEtoiles[i].posX*20+30, self.modele.listeEtoiles[i].posY*20+30, dash=(4,4), outline='green', tags="selection")
                            self.vue.surfaceJeu.create_line(self.modele.listeEtoiles[self.modele.etoileDepart].posX*20+10,self.modele.listeEtoiles[self.modele.etoileDepart].posY*20+10, self.modele.listeEtoiles[self.modele.etoileArrivee].posX*20+10, self.modele.listeEtoiles[self.modele.etoileArrivee].posY*20+10, fill='blue', tags="selection")
                            self.etoileClique = False
                    break

                     
            #Sinon set les etoiles selectionnées a None
            elif(self.etoileClique == False):
                print("le else")
                self.modele.etoileDepart = None
                self.modele.etoileArrivee = None
                self.etoileClique = True
                
    
        

if __name__ == "__main__":
    c = Controleur()
    
