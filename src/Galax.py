from tkinter import *
import Classes
import random

class Modele:
    def __init__(self, parent):
        self.parent = parent
        self.temps_courant = 1
        #Pour une surface de 1000x800 px ou les etoiles sont des cases de 10 x 10 px
        self.surfaceX = 50
        self.surfaceY = 37
        self.nbEtoiles = 0
        self.listeEtoiles = []
        self.listeFlottes = [] # liste d'objets de type Classes.flotteDeVaisseaux
        self.etoileDepart = None
        self.etoileArrivee = None
        #Creation d'un objet pour chaque faction pour savoir differentes informations sur chacune de celle-ci
        self.humain = Classes.Humains(self)
        self.gubrus = Classes.Gubrus(self)
        self.czin = Classes.Czins(self)
        

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
                #print(i)
                
                    
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
        n = random.randint(0,len(self.listeEtoiles)-1)
        #print(n)

        self.listeEtoiles[n].nbVaisseaux = 100
        self.listeEtoiles[n].nbManufactures = 10
        self.listeEtoiles[n].proprietaire = 1
        self.listeEtoiles[n].niveauInfo = 3
               
        self.humain.etoileMere = n
        self.humain.listePossessions.append(n)

        

        while(positionOK == False):

            n = random.randint(0,len(self.listeEtoiles)-1)
            
            if(self.listeEtoiles[n].proprietaire != 1):
                self.listeEtoiles[n].proprietaire = 2
                self.listeEtoiles[n].nbVaisseaux = 100
                self.listeEtoiles[n].nbManufactures = 10
                self.gubrus.etoileMere = n
                self.gubrus.listePossessions.append(n)
                positionOK=True
                
            
        positionOK = False
        
        while(positionOK == False):

            n = random.randint(0,len(self.listeEtoiles)-1)
        
            if(self.listeEtoiles[n].proprietaire != 1 and self.listeEtoiles[n].proprietaire != 2):
                self.listeEtoiles[n].proprietaire = 3
                self.listeEtoiles[n].nbVaisseaux = 100
                self.listeEtoiles[n].nbManufactures = 10
                self.czin.base = n
                self.czin.etoileMere = n
                self.czin.listePossessions.append(n)
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
        self.boutonInstructions = Button(self.root, text='Instructions', width=50, bg='black', fg='white',activebackground='black', activeforeground='white')
        self.boutonQuitter = Button(self.root, text='Quitter',width=50, bg='black', fg='white',activebackground='black', activeforeground='white', command=self.root.destroy)
        
        #Widgets pour l'affichage du jeu
        self.surfaceJeu = Canvas(self.root, width=1000, height=740, bg='white', highlightthickness=0)
        self.labelHumains = Label(self.root, text="Humains : 1", font=("Arial",16))
        self.labelGubrus = Label(self.root, text="Gubrus : 1", font=("Arial",16))
        self.labelCzins = Label(self.root, text="Czins : 1", font=("Arial",16))
        self.boutonEnvoyerFlotte = Button(self.root, text='Envoyer Une Flotte',width=50, bg='black', fg='white',activebackground='black', activeforeground='white')
        self.boutonChangerAnnee = Button(self.root, text='Annee Suivante',width=50, bg='black', fg='white',activebackground='black', activeforeground='white')
        self.choisirNbVaisseaux = Scale(self.root, orient=HORIZONTAL, length=300)

        #Label pour l'affichage des informations
        self.labelNbVaisseaux = Label(self.root, font=("Arial", 16))
        self.labelNiveauInfo = Label(self.root, font=("Arial", 16))
        self.labelNbManufactures = Label(self.root, font=("Arial", 16))
        

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
        self.surfaceJeu.bind('<Button-1>', self.getLeftClick)
        self.surfaceJeu.bind('<Button-3>', self.getRightClick)
        
        
    #Obtenir le click de souris sur la surface   
    def getLeftClick(self, event):

        self.parent.transmissionMouseClick(event.x, event.y)

    #Obtenir les informations d'une planete lors d'un right click
    def getRightClick(self, event):

        print(event.x, event.y)
        self.parent.obtenirInfoEtoile(event.x, event.y)
        

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
            #print(etoile.proprietaire)
            
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
        #Creation des etoiles
        self.modele.creerEtoiles()
        #Creation de valeur_grappe et valeur_base pour chaque etoile
        self.modele.czin.definirValeurGrappe(self.modele)
        self.modele.czin.definirValeurBase(self.modele)
        #Assignation des etoiles meres
        self.modele.assignerLesEtoilesMeres()
        #Affichage Initial du jeu
        self.vue.afficherJeu(self.modele)
        #Affichage des proprietaires sur les etoiles
        self.vue.afficherProprietaire(self.modele)
        #Booleen pour gerer le mouseclick lors de la selection d'une etoile
        self.etoileClique = False
        #Booleen pour ne pas essayer d'envoyer une Arma une deuxieme fois
        self.vue.root.mainloop()

    
    def transmissionMouseClick(self, x, y):
        
        self.vue.surfaceJeu.delete("selection")
        self.vue.choisirNbVaisseaux.place_forget()
        self.vue.boutonEnvoyerFlotte.place_forget()

        print(len(self.modele.listeEtoiles))
        for i in range(0, len(self.modele.listeEtoiles)):

            if(self.modele.listeEtoiles[i].posX*20 <= x and self.modele.listeEtoiles[i].posX*20+20 >= x):
                if(self.modele.listeEtoiles[i].posY*20 <= y and self.modele.listeEtoiles[i].posY*20+20 >= y):
                
                    #Si l'etoile de depart n'est pas selectionné
                    if(self.modele.etoileDepart == None and self.modele.listeEtoiles[i].proprietaire == 1):
                        self.vue.surfaceJeu.create_oval(self.modele.listeEtoiles[i].posX*20-10, self.modele.listeEtoiles[i].posY*20-10, self.modele.listeEtoiles[i].posX*20+30, self.modele.listeEtoiles[i].posY*20+30, dash=(4,4), outline='red', tags="selection")
                        self.modele.etoileDepart = i
                        self.etoileClique = True
                        print("trouve")
                        
                    elif(self.modele.etoileDepart != None):
                        self.vue.surfaceJeu.create_oval(self.modele.listeEtoiles[self.modele.etoileDepart].posX*20-10, self.modele.listeEtoiles[self.modele.etoileDepart].posY*20-10, self.modele.listeEtoiles[self.modele.etoileDepart].posX*20+30, self.modele.listeEtoiles[self.modele.etoileDepart].posY*20+30, dash=(4,4), outline='red', tags="selection")
                        if(i != self.modele.etoileDepart):
                            self.modele.etoileArrivee = i
                            self.vue.surfaceJeu.create_oval(self.modele.listeEtoiles[i].posX*20-10, self.modele.listeEtoiles[i].posY*20-10, self.modele.listeEtoiles[i].posX*20+30, self.modele.listeEtoiles[i].posY*20+30, dash=(4,4), outline='green', tags="selection")
                            self.vue.surfaceJeu.create_line(self.modele.listeEtoiles[self.modele.etoileDepart].posX*20+10,self.modele.listeEtoiles[self.modele.etoileDepart].posY*20+10, self.modele.listeEtoiles[self.modele.etoileArrivee].posX*20+10, self.modele.listeEtoiles[self.modele.etoileArrivee].posY*20+10, fill='blue', tags="selection")
                            self.vue.choisirNbVaisseaux.config(from_=0, to = self.modele.listeEtoiles[self.modele.etoileDepart].nbVaisseaux)
                            print(self.modele.listeEtoiles[self.modele.etoileDepart].nbVaisseaux)
                            self.vue.choisirNbVaisseaux.place(x=50, y=740, width=500)
                            self.vue.boutonEnvoyerFlotte.place(x=580, y=755, width=150)
                            self.etoileClique = False
                    break

                     
            #Sinon set les etoiles selectionnées a None
            elif(self.etoileClique == False):
                print("le else")
                self.modele.etoileDepart = None
                self.modele.etoileArrivee = None
                self.etoileClique = True

    def obtenirInfoEtoile(self, x, y):

        self.vue.labelNbVaisseaux.place_forget()
        self.vue.labelNiveauInfo.place_forget()
        self.vue.labelNbManufactures.place_forget()
        
        #Boucle pour passer chacune des etoiles
        for etoile in self.modele.listeEtoiles:
            if(etoile.posX*20 <= x and etoile.posX*20+20 >= x):
                if(etoile.posY*20 <= y and etoile.posY*20+20 >= y):
                    if(etoile.niveauInfo == 0):
                        break
                    elif(etoile.niveauInfo == 1):
                        self.vue.labelNbVaisseaux.config(text='Nb Vaisseaux : ' + str(etoile.nbVaisseauxDerniereVisite))
                        self.vue.labelNbVaisseaux.place(x=1000, y=200, width=200, height=30)
                        self.vue.labelNiveauInfo.config(text="Niveau d'info : " + str(etoile.niveauInfo))
                        self.vue.labelNiveauInfo.place(x=1000, y=230, width=200, height=30)
                    elif(etoile.niveauInfo == 2):
                        self.vue.labelNbVaisseaux.config(text='Nb Vaisseaux : ' + str(etoile.nbVaisseauxDerniereVisite))
                        self.vue.labelNbVaisseaux.place(x=1000, y=200, width=200, height=30)
                        self.vue.labelNbManufactures.config(text='Nb Manufactures : ' + str(etoile.nbManufactures))
                        self.vue.labelNbManufactures.place(x=1000, y=230, width=200, height=30)
                        self.vue.labelNiveauInfo.config(text="Niveau d'info : " + str(etoile.niveauInfo))
                        self.vue.labelNiveauInfo.place(x=1000, y=260, width=200, height=30)
                    elif(etoile.niveauInfo == 3):
                        self.vue.labelNbVaisseaux.config(text='Nb Vaisseaux : ' + str(etoile.nbVaisseaux))
                        self.vue.labelNbVaisseaux.place(x=1000, y=200, width=200, height=30)
                        self.vue.labelNbManufactures.config(text='Nb Manufactures : ' + str(etoile.nbManufactures))
                        self.vue.labelNbManufactures.place(x=1000, y=230, width=200, height=30)
                        self.vue.labelNiveauInfo.config(text="Niveau d'info : " + str(etoile.niveauInfo))
                        self.vue.labelNiveauInfo.place(x=1000, y=260, width=200, height=30)
            
        
    def deroulerTour(self):
        #Tour des Gubrus
        if(not self.modele.gubrus.mort):
            pass
        
        #Tour des Czins

        #Si les Czins sont toujours en vie
        if(not self.modele.czin.mort):
        
            #Si les Czins sont en mode rassemblement_force
            if(self.modele.czin.rassemblement_force):

                #Si on possede une armada soit 3 x force_attaque
                if(self.modele.listeEtoiles[self.modele.czin.base].nbVaisseaux >= self.modele.czin.forceAttaque(self.modele.temps_courant)*3):
                    #Envoyer l'Armada vers la base prospective
                    self.modele.listeFlottes.append(flotteDeVaisseaux(self.modele.listeEtoiles[self.modele.czin.base].nbVaisseaux, self.modele.listeEtoiles[self.modele.czin.base], self.modele.czin.etablirBase(self.modele), 3))
                    self.modele.czin.listePossessionsFlottes.append(len(self.modele.listeFlottes)-1)
                    self.modele.czin.rassemblement_force = False
                    self.modele.czin.etablir_base = True
                
                #Si les Czins on plusieurs Etoiles
                elif(len(self.modele.czin.listePossession) > 1):

                    planeteProche = False
                    
                    #Pour tous les numeros d'etoile que les Czins possedent
                    for numero in self.modele.czin.listePossession:
                        
                        #Pour calculer la distance
                        differenceX = abs(self.modele.listeEtoiles[numero].posX - modele.listeEtoiles[sel.modele.czin.base].posX)
                        differenceY = abs(self.modele.listeEtoiles[numero].posY - modele.listeEtoiles[sel.modele.czin.base].posY)

                        #Calculer la distance a l'aide du theoreme de pythagore
                        distance=math.sqrt(math.pow(differenceX, 2)+math.pow(differenceY, 2))
                        
                        #Si les etoiles sont a distance rassemblement
                        if(distance <= 6):

                            planeteProche = True
                            
                            #Si le nombre de vaisseau sur cette etoile est plus grand que 3
                            if(self.modele.listeEtoile[numero] > 3):
                                
                                #Choisir le nombre de vaisseaux a envoyer sur la base soit nbVaisseaux - 3
                                vaisseauxAEnvoyer = self.modele.listeEtoile[numero].nbVaisseaux - 3
                            
                                #Creation de la flotte de Vaisseau
                                self.modele.listeFlottes.append(flotteDeVaisseaux(vaisseauxAEnvoyer, self.modele.listeEtoile[numero], self.modele.listeEtoile[self.modele.czin.base], 3))
                                self.modele.czin.listePossessionsFlottes.append(len(self.modele.listeFlottes)-1)
                            
                                #On enleve les vaisseaux sur l'etoile une fois la flotte creee
                                self.modele.listeEtoile[numero].nbVaisseaux = self.modele.listeEtoile[numero].nbVaisseaux - vaiseauxAEnvoyer

                        #Si il n'y a pas d'etoile a distance rassemblement de la base changer la base pour l'etoile mere
                        elif(not planeteProche):
                            self.modele.czin.base = self.modele.czin.etoileMere
                            
                
            
            #Si on est en mode conquerir_grappe
            if(self.modele.czin.conquerir_grappe):

                etoileABonneDistance = False
                
                for etoileAConquerir in self.modele.listeEtoiles:

                    #Pour calculer la distance
                    differenceX = abs(etoile.posX - modele.listeEtoiles[sel.modele.czin.base].posX)
                    differenceY = abs(etoile.posY - modele.listeEtoiles[sel.modele.czin.base].posY)

                    #Calculer la distance a l'aide du theoreme de pythagore
                    distance=math.sqrt(math.pow(differenceX, 2)+math.pow(differenceY, 2))

                    #Si cette toile est a distance grappe 
                    if(distance <= self.czin.DISTANCE_GRAPPE):

                        #Si il y a une etoile a la bonne distance
                        etoileABonneDistance = True
                        
                        #Si le nombre de vaisseau sur la base est plus grand ou egal a froce_attaque
                        if(self.modele.listeEtoiles[self.modele.czin.base] >= self.modele.czin.forceAttaque(self.modele.temps_courant)):
                            self.modele.listeFlottes.append(flotteDeVaisseaux(vaisseauxAEnvoyer, self.modele.listeEtoile[self.modele.czin.base], etoileAConquerir, 3))
                            self.modele.czin.listePossessionsFlottes.append(len(self.modele.listeFlottes)-1) 

                        #Sinon on sort de la boucle puisqu'il n'y a pas assez de vaisseaux sur la base
                        else:
                            break

                    if(not etoileABonneDistance):
                        self.modele.czin.rassemblement_force = True
                        self.modele.czin.conquerir_grappe = False
                        
            
        
    
    def combatVaisseau(self):
        pass
    
        

if __name__ == "__main__":
    c = Controleur()
    
