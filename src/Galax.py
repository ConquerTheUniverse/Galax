from tkinter import *
import Classes
import math
import random

class Modele:
    def __init__(self, parent):
        self.parent = parent
        self.temps_courant = 1
        #Pour une surface de 1000x800 px ou les etoiles sont des cases de 10 x 10 px
        self.surfaceX = 40
        self.surfaceY = 20
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
        self.posXsurface = 0
        self.posYsurface = 0
        self.ePx = 60
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
        self.backgroundSurface = PhotoImage(file="images/bgSurface.gif")
        self.backgroundMenu = PhotoImage(file="images/bgMenu.gif")

        #Resize des planetes
        self.resizeRatio = int(600/self.ePx)
        self.imagePlanete1 = self.imagePlanete1.subsample(self.resizeRatio,self.resizeRatio)
        self.imagePlanete2 = self.imagePlanete2.subsample(self.resizeRatio,self.resizeRatio)
        self.imagePlanete3 = self.imagePlanete3.subsample(self.resizeRatio,self.resizeRatio)
        self.imagePlanete4 = self.imagePlanete4.subsample(self.resizeRatio,self.resizeRatio)

        #Elements du menu
        self.backgroundMenu = Label(self.root, image=self.backgroundMenu)
        self.boutonJouer = Button(self.root, text='Jouer',width=50, bg='black', fg='white',activebackground='black', activeforeground='white')
        self.boutonInstructions = Button(self.root, text='Instructions', width=50, bg='black', fg='white',activebackground='black', activeforeground='white')
        self.boutonQuitter = Button(self.root, text='Quitter',width=50, bg='black', fg='white',activebackground='black', activeforeground='white', command=self.root.destroy)
        
        #Widgets pour l'affichage du jeu
        self.surfaceJeu = Canvas(self.root, width=1200, height=600, bg='white', highlightthickness=0)
        self.surfaceJeu.configure(scrollregion=(0,0,2400,1200))
        self.surfaceMap = Canvas(self.root, width=240, height=120, bg='black', highlightthickness=0)
        self.labelHumains = Label(self.root, text="Humains : 1", font=("Arial",16))
        self.labelGubrus = Label(self.root, text="Gubrus : 1", font=("Arial",16))
        self.labelCzins = Label(self.root, text="Czins : 1", font=("Arial",16))
        self.boutonEnvoyerFlotte = Button(self.root, text='Envoyer Une Flotte',width=50, bg='black', fg='white',activebackground='black', activeforeground='white', command=self.parent.envoyerFlotte)
        self.boutonChangerAnnee = Button(self.root, text='Annee Suivante',width=50, bg='black', fg='white',activebackground='black', activeforeground='white', command=self.parent.deroulerTour)
        self.choisirNbVaisseaux = Scale(self.root, orient=HORIZONTAL, width=50)
        self.labelAnnee = Label(self.root, text="Annee : 1", font=("Arial",16))

        #Text
        self.info = Text(self.root, bg='black', fg='white')
        self.info.see(END)
            

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

        #Pour faire un lien deux planetes pour envoyer des flottes
        self.surfaceJeu.bind("<ButtonPress-3>", self.getRightClick)

        #Double click pour les infos sur la planete
        self.surfaceJeu.bind("<Double-Button-1>", self.getDoubleClick)
        
        #Pour que le canvas scroll lorsquon click
        self.surfaceJeu.bind("<ButtonPress-1>", self.scroll_start)
        self.surfaceJeu.bind("<B1-Motion>", self.scroll_move)
     
    def scroll_start(self, event):
        self.surfaceJeu.scan_mark(event.x, event.y)
        
    
    def scroll_move(self, event):
        self.surfaceJeu.scan_dragto(event.x, event.y, gain=1)
        print(self.surfaceJeu.canvasx(0), self.surfaceJeu.canvasy(0))
        self.surfaceMap.delete("camera")
        self.surfaceMap.create_rectangle(math.floor(self.surfaceJeu.canvasx(0)/60)*6, math.floor(self.surfaceJeu.canvasy(0)/60)*6, (math.floor(self.surfaceJeu.canvasx(0)/60)*6+120), (math.floor(self.surfaceJeu.canvasy(0)/60)*6+60), outline='red', tags="camera")
        
        
        
    #Obtenir le click de souris sur la surface   
    def getRightClick(self, event):
        self.parent.transmissionMouseClick(event.x, event.y)

    #Obtenir les informations d'une planete lors d'un right click
    def getDoubleClick(self, event):

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
        self.surfaceJeu.place(x=0,y=25)
        self.surfaceMap.place(x=935, y=640)
        self.surfaceJeu.create_image(0, 0, anchor=NW, image=self.backgroundSurface)
        
        

        #Boucle pour afficher cahcune des etoiles sur la surface
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

                        self.surfaceJeu.create_image(x*self.ePx,y*self.ePx,anchor=NW, image=randomImage, tags="planete")
                        self.surfaceMap.create_rectangle(0, 0, 120, 60, outline='red', tags="camera")
                        break #Pour sortir du for interne puisqu'il ne peut pas y avoir deux etoiels a la meme position


        
        #Place les item qui seront sur le coter de la surface
        self.logoHumains.place(x=330, y=660)
        self.labelHumains.place(x=360, y=660, width=170, height=30)

        self.logoGubrus.place(x=330, y=690)
        self.labelGubrus.place(x=360, y=690, width=170, height=30)

        self.logoCzins.place(x=330, y=720)
        self.labelCzins.place(x=360, y=720, width=170, height=30)

        self.info.place(x=550, y=640, width=370, height=120)
        
        #Place le bouton pour changer d'annee
        self.labelAnnee.place(x=680, y=760)
        self.boutonChangerAnnee.place(x=980, y=765, width=150)


    #Afficher map
    def afficherMap(self, modele):
        for y in range(0, modele.surfaceY):
            for x in range(0, modele.surfaceX):
                for etoile in modele.listeEtoiles:
                    if(x == etoile.posX and y == etoile.posY):
                        if(etoile.proprietaire == 0):
                            couleur = 'white'
                        elif(etoile.proprietaire == 1):
                            couleur = 'blue'
                        elif(etoile.proprietaire == 2):
                            couleur = 'yellow'
                        elif(etoile.proprietaire == 3):
                            couleur = 'red'
                            
        
                        self.surfaceMap.create_rectangle(x*6,y*6, (x*6)+6, (y*6)+6, fill=couleur)
                        break #Pour sortir du for interne puisqu'il ne peut pas y avoir deux etoiels a la meme position
    
    #Affiche les proprietaires sur les planetes
    def afficherProprietaire(self, modele):
        
        self.surfaceJeu.delete("logo")
        
        for etoile in modele.listeEtoiles:
            #print(etoile.proprietaire)
            
            if(etoile.proprietaire == 1):
                self.surfaceJeu.create_image(etoile.posX*self.ePx, etoile.posY*self.ePx, anchor=NW, image=self.imageHumains, tags="logo")
            elif(etoile.proprietaire == 2):
                self.surfaceJeu.create_image(etoile.posX*self.ePx, etoile.posY*self.ePx, anchor=NW, image=self.imageGubrus, tags="logo")
            elif(etoile.proprietaire == 3):
                self.surfaceJeu.create_image(etoile.posX*self.ePx, etoile.posY*self.ePx, anchor=NW, image=self.imageCzins, tags="logo")

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
        self.vue.afficherMap(self.modele)
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

            

            if(self.modele.listeEtoiles[i].posX*60 <= self.vue.surfaceJeu.canvasx(x) and self.modele.listeEtoiles[i].posX*60+60 >= self.vue.surfaceJeu.canvasx(x)):
                if(self.modele.listeEtoiles[i].posY*60 <= self.vue.surfaceJeu.canvasy(y) and self.modele.listeEtoiles[i].posY*60+60 >= self.vue.surfaceJeu.canvasy(y)):

                    #Si l'etoile de depart n'est pas selectionné
                    if(self.modele.etoileDepart == None and self.modele.listeEtoiles[i].proprietaire == 1):
                        self.vue.surfaceJeu.create_oval(self.modele.listeEtoiles[i].posX*self.vue.ePx-10, self.modele.listeEtoiles[i].posY*self.vue.ePx-10, self.modele.listeEtoiles[i].posX*self.vue.ePx+70, self.modele.listeEtoiles[i].posY*self.vue.ePx+70, dash=(4,4), outline='red', tags="selection")
                        self.modele.etoileDepart = i
                        self.etoileClique = True
                        print("trouve")
                        
                    elif(self.modele.etoileDepart != None):
                        self.vue.surfaceJeu.create_oval(self.modele.listeEtoiles[self.modele.etoileDepart].posX*self.vue.ePx-10, self.modele.listeEtoiles[self.modele.etoileDepart].posY*self.vue.ePx-10, self.modele.listeEtoiles[self.modele.etoileDepart].posX*self.vue.ePx+70, self.modele.listeEtoiles[self.modele.etoileDepart].posY*self.vue.ePx+70, dash=(4,4), outline='red', tags="selection")
                        if(i != self.modele.etoileDepart):
                            self.modele.etoileArrivee = i
                            self.vue.surfaceJeu.create_oval(self.modele.listeEtoiles[i].posX*self.vue.ePx-10, self.modele.listeEtoiles[i].posY*self.vue.ePx-10, self.modele.listeEtoiles[i].posX*self.vue.ePx+70, self.modele.listeEtoiles[i].posY*self.vue.ePx+70, dash=(4,4), outline='green', tags="selection")
                            self.vue.surfaceJeu.create_line(self.modele.listeEtoiles[self.modele.etoileDepart].posX*self.vue.ePx+30,self.modele.listeEtoiles[self.modele.etoileDepart].posY*self.vue.ePx+30, self.modele.listeEtoiles[self.modele.etoileArrivee].posX*self.vue.ePx+30, self.modele.listeEtoiles[self.modele.etoileArrivee].posY*self.vue.ePx+30, fill='blue', tags="selection")
                            self.vue.choisirNbVaisseaux.config(from_=0, to = self.modele.listeEtoiles[self.modele.etoileDepart].nbVaisseaux)
                            print(self.modele.listeEtoiles[self.modele.etoileDepart].nbVaisseaux)
                            self.vue.choisirNbVaisseaux.place(x=25, y=650, width=300)
                            self.vue.boutonEnvoyerFlotte.place(x=100, y=725, width=150, height=50)
                            self.etoileClique = False
                    break

                     
            #Sinon set les etoiles selectionnées a None
            elif(self.etoileClique == False):
                print("le else")
                self.modele.etoileDepart = None
                self.modele.etoileArrivee = None
                self.etoileClique = True

    def obtenirInfoEtoile(self, x, y):

        self.vue.surfaceJeu.delete("info")
        
        #Boucle pour passer chacune des etoiles
        for etoile in self.modele.listeEtoiles:
            if(etoile.posX*60 <= self.vue.surfaceJeu.canvasx(x) and etoile.posX*60+60 >= self.vue.surfaceJeu.canvasx(x)):
                if(etoile.posY*60 <= self.vue.surfaceJeu.canvasy(y) and etoile.posY*60+60 >= self.vue.surfaceJeu.canvasy(y)):
                    
                    if(etoile.posX >= 37):
                        offset = -145
                    else:
                        offset = 60

                    if(etoile.niveauInfo == 0):
                        break
                    elif(etoile.niveauInfo == 1):
                        self.vue.surfaceJeu.create_text((etoile.posX*60)+offset, (etoile.posY*60)+10, text='Nb Vaisseaux : '+ str(etoile.nbVaisseauxDerniereVisite), font=('Arial', 12), fill='white', tags="info")
                        self.vue.surfaceJeu.create_text((etoile.posX*60)+offset, (etoile.posY*60)+50, text='Niveau Info : '+ str(etoile.niveauInfo), font=('Arial', 12), fill='white', tags="info")
                    elif(etoile.niveauInfo == 2):
                        self.vue.surfaceJeu.create_text((etoile.posX*60)+offset, (etoile.posY*60)+10, text='Nb Vaisseaux : '+ str(etoile.nbVaisseauxDerniereVisite), font=('Arial', 12), fill='white', tags="info")
                        self.vue.surfaceJeu.create_text((etoile.posX*60)+offset, (etoile.posY*60)+30, text='Nb Manufactures : '+ str(etoile.nbManufactures), font=('Arial', 12), fill='white', tags="info") 
                        self.vue.surfaceJeu.create_text((etoile.posX*60)+offset, (etoile.posY*60)+50, text='Niveau Info : '+ str(etoile.niveauInfo), font=('Arial', 12), fill='white', tags="info")
                    elif(etoile.niveauInfo == 3):
                        self.vue.surfaceJeu.create_text((etoile.posX*60)+offset, (etoile.posY*60)+10, anchor=W, text='Nb Vaisseaux : '+ str(etoile.nbVaisseaux), font=('Arial', 12), fill='white', tags="info")
                        self.vue.surfaceJeu.create_text((etoile.posX*60)+offset, (etoile.posY*60)+30, anchor=W, text='Nb Manufactures : '+ str(etoile.nbManufactures), font=('Arial', 12), fill='white', tags="info") 
                        self.vue.surfaceJeu.create_text((etoile.posX*60)+offset, (etoile.posY*60)+50, anchor=W, text='Niveau Info : '+ str(etoile.niveauInfo), font=('Arial', 12), fill='white', tags="info")
                        
            
        
    def deroulerTour(self):
        #Tour des Gubrus
        if(not self.modele.gubrus.mort):
            #Envoyer flottes vers planete la plus proche
            self.modele.gubrus.listeFlottes.append(Classes.flotteDeVaisseaux(self.modele.listeEtoiles[self.modele.gubrus.etoileMere].nbVaisseaux,self.modele.listeEtoiles[self.modele.gubrus.etoileMere],self.modele.gubrus.strategieAttaque(self.modele),2,self.modele.temps_courant))
        
        #Tour des Czin

        #Si les Czins sont toujours en vie
        if(not self.modele.czin.mort):
        
            #Si les Czins sont en mode rassemblement_force
            if(self.modele.czin.rassemblement_force):

                #Si on possede une armada soit 3 x force_attaque
                if(self.modele.listeEtoiles[self.modele.czin.base].nbVaisseaux >= self.modele.czin.forceAttaque(self.modele.temps_courant)*3):
                    #Envoyer l'Armada vers la base prospective
                    self.modele.listeFlottes.append(Classes.flotteDeVaisseaux(self.modele.listeEtoiles[self.modele.czin.base].nbVaisseaux, self.modele.listeEtoiles[self.modele.czin.base], self.modele.czin.etablirBase(self.modele), 3, self.modele.temps_courant))
                    self.self.modele.listeEtoiles[self.modele.czin.base].nbVaisseaux = 0
                    self.modele.czin.listePossessionsFlottes.append(len(self.modele.listeFlottes)-1)
                    self.modele.czin.rassemblement_force = False
                    self.modele.czin.etablir_base = True
                
                #Si les Czins on plusieurs Etoiles
                elif(len(self.modele.czin.listePossessions) > 1):

                    planeteProche = False
                    
                    #Pour tous les numeros d'etoile que les Czins possedent
                    for numero in self.modele.czin.listePossession:
                        print("infinie")
                        
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
                                self.modele.listeFlottes.append(Classes.flotteDeVaisseaux(vaisseauxAEnvoyer, self.modele.listeEtoile[numero], self.modele.listeEtoile[self.modele.czin.base], 3, self.modele.temps_courant))
                                self.modele.listeEtoile[numero].nbVaisseaux -= vaisseauxAEnvoyer
                                self.modele.listeFlottes[len(self.modele.listeFlottes)-1].armada = True
                                self.modele.czin.listePossessionsFlottes.append(len(self.modele.listeFlottes)-1)
                            
                                #On enleve les vaisseaux sur l'etoile une fois la flotte creee
                                self.modele.listeEtoile[numero].nbVaisseaux = self.modele.listeEtoile[numero].nbVaisseaux - vaiseauxAEnvoyer

                    #Si il n'y a pas d'etoile a distance rassemblement de la base changer la base pour l'etoile mere
                    if(not planeteProche):
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
                            self.modele.listeFlottes.append(Classes.flotteDeVaisseaux(self.modele.czin.forceAttaque(self.modele.temps_courant), self.modele.listeEtoile[self.modele.czin.base], etoileAConquerir, 3, self.modele.listeEtoiles.index(etoileAConquerir), self.modele.temps_courant))
                            self.modele.listeEtoile[self.modele.czin.base].nbVaisseaux -= self.modele.czin.forceAttaque(self.modele.temps_courant)
                            self.modele.czin.listePossessionsFlottes.append(len(self.modele.listeFlottes)-1)
                            

                        #Sinon on sort de la boucle puisqu'il n'y a pas assez de vaisseaux sur la base
                        else:
                            break

                    if(not etoileABonneDistance):
                        self.modele.czin.rassemblement_force = True
                        self.modele.czin.conquerir_grappe = False
                        
        #Evaluer chaque dixieme d'annee
        for i in range(0,10):

            #Pour chaque flotte Czin   
            for flotte in self.modele.czin.listeFlottes:
                #Si la flotte est arrivee a destination
                if(round(flotte.anneeArrivee, 1) == self.modele.temps_courant+(i/10)):
                    print("Une flotte Czin est arrivee!")
                    #Si la planete est ennemi
                    self.combatVaisseau(flotte, flotte.destination)
                        
                    if(flotte.armada):
                        self.modele.czin.etablir_base = False
                        self.modele.czin.conquerir_grappe = True

            #Pour chaque flotte Humaine 
            for flotte in self.modele.humain.listeFlottes:
                #Si la flotte est arrivee a destination
                if(round(flotte.anneeArrivee, 1) == self.modele.temps_courant+(i/10)):
                    print("Une flotte Humaine est arrivee!")
                    #Si la planete est ennemi
                    self.combatVaisseau(flotte, flotte.destination)

            #Pour chaque flotte Gubrus  
            for flotte in self.modele.gubrus.listeFlottes:
                #Si la flotte est arrivee a destination
                if(round(flotte.anneeArrivee, 1) == self.modele.temps_courant+(i/10)):
                    print("Une flotte Gubru est arrivee!")
                    #Si la planete est ennemi
                    self.combatVaisseau(flotte, flotte.destination)
                

        #Generer des vaisseaux
        for etoile in self.modele.listeEtoiles:
            etoile.genererVaisseau()
            print(etoile.nbVaisseaux)

        #Update les informations
        self.vue.choisirNbVaisseaux.place_forget()
        self.vue.boutonEnvoyerFlotte.place_forget()
        self.vue.surfaceJeu.delete("selection")
        self.vue.surfaceJeu.delete("info")
        self.modele.temps_courant += 1
        self.vue.labelAnnee.config(text="Annee : "+str(self.modele.temps_courant))

        #Update les logo ainsi que la map
        self.vue.afficherProprietaire(self.modele)
        self.vue.afficherMap(self.modele)
            
        
    
    def combatVaisseau(self, flotteAttaquante, etoileDefendante):
        tourAttaque = False # verifier si c'est au tour de l'attaquant d'attaquer
        if(flotteAttaquante.quantiteVaisseaux < etoileDefendante.nbVaisseaux):
            # Possible attaque surprise
            # 1-calculer ratio r : 
            r = round((etoileDefendante.nbVaisseaux /flotteAttaquante.quantiteVaisseaux))
            print("ratio r : " + str(r))
            pourcentageSurprise = 0
            # 2-determiner pourcentageSurprise :
            if(r < 5):
                pourcentageSurprise = round(r/10, 2)
            elif(r < 20):
                pourcentageSurprise = round(((3*r + 35) /100), 2)
            else : pourcentageSurprise = 0.95
            
            print("pourcentage : " + str(pourcentageSurprise))
            
            
            if(random.randrange(100) < pourcentageSurprise):
                tourAttaque = True # situation d'une attaque surprise
        
        while(flotteAttaquante.quantiteVaisseaux > 0 and etoileDefendante.nbVaisseaux > 0):
            if(tourAttaque): # l'attaquant attaque 
                pourcentage = 100
                nbTemp = 0
                for i in range(0,etoileDefendante.nbVaisseaux):
                    if(random.randrange(100) < pourcentage):
                        nbTemp = nbTemp+1
                etoileDefendante.nbVaisseaux = etoileDefendante.nbVaisseaux-nbTemp
                print("nbVaisseauxDefendant : " + str(etoileDefendante.nbVaisseaux))
                tourAttaque = False
            
            else : # le defenseur attaque
                pourcentage = 70
                nbTemp = 0
                for i in range(0,flotteAttaquante.quantiteVaisseaux):
                    if(random.randrange(100) < pourcentage):
                        nbTemp = nbTemp+1
                flotteAttaquante.quantiteVaisseaux = flotteAttaquante.quantiteVaisseaux-nbTemp
                print("nbVaisseauxAttaquant : " + str(flotteAttaquante.quantiteVaisseaux))
                tourAttaque = True    
                
                
        if(etoileDefendante.nbVaisseaux == 0): #attaquants gagnent
            print("Attaquant gagne")
            print("Nombre de vaisseaux attaquants restants : " + str(flotteAttaquante.quantiteVaisseaux))
            
            for i in range(0, len(self.modele.listeEtoiles)):

                #1-enlever l'etoile de la liste de la civilisation defendante
                if(self.modele.listeEtoiles[i] == etoileDefendante):

                    if(etoileDefendante.proprietaire == 1): #Si le defendant est Humain
                        self.modele.humain.listePossessions.remove(i) #Remove i de la liste, i n'est pas la position mais la valeur

                    elif(etoileDefendante.proprietaire == 2): #Si le defendant est Gubrus
                        self.modele.gubrus.listePossessions.remove(i) #Remove i de la liste, i n'est pas la position mais la valeur

                    elif(etoileDefendante.proprietaire == 1): #Si le defendant est Czin
                               self.modele.czin.listePossessions.remove(i) #Remove i de la liste, i n'est pas la position mais la valeur

                    #2-ajouter l'etoile de la liste de la civilisation attaquante
                    if(flotteAttaquante.proprietaire == 1):
                        self.modele.humain.listePossessions.append(i)
                           
                    elif(flotteAttaquante.proprietaire == 2):
                        self.modele.gubrus.listePossessions.append(i)

                    elif(flotteAttaquante.proprietaire == 3):
                        self.modele.czin.listePossessions.append(i)

                    break
                           
            #3-actualiser le nombre de vaisseaux sur l'etoile qui change de proprietaire
            etoileDefendante.proprietaire = flotteAttaquante.proprietaire
            etoileDefendante.nbVaisseaux = flotteAttaquante.quantiteVaisseaux
            etoileDefendante.niveauInfo = 3
            
            return True
               
        else:# (nbVaisseauxAttaquant == 0) et donc defendants gagnent
            print("Defendant gagne")
            print("Nombre de vaisseaux defendants restants : " + str(etoileDefendante.nbVaisseaux))

            #1- eliminer la flotte attaquante de la liste
            if(flotteAttaquante.proprietaire == 1):
                self.modele.humain.listeFlottes.remove(flotteAttaquante)

            elif(flotteAttaquante.proprietaire == 2):
                self.modele.gubrus.listeFlottes.remove(flotteAttaquante)

            elif(flotteAttaquante.proprietaire == 3):
                self.modele.czin.listeFlottes.remove(flotteAttaquante)

            #Changer le niveau d'info
            if(etoileDefendante.niveauInfo < 3):
                etoileDefendante.niveauInfo += 1
           
                           
            return False

    def envoyerFlotte(self):
        if(self.vue.choisirNbVaisseaux.get() > 0):
            self.modele.humain.listeFlottes.append(Classes.flotteDeVaisseaux(self.vue.choisirNbVaisseaux.get(), self.modele.listeEtoiles[self.modele.etoileDepart], self.modele.listeEtoiles[self.modele.etoileArrivee], 1, self.modele.temps_courant))
            self.modele.listeEtoiles[self.modele.etoileDepart].nbVaisseaux -= self.vue.choisirNbVaisseaux.get()
            etoileDepart = None
            etoileDepart = None
            self.vue.surfaceJeu.delete("selection")
            self.vue.choisirNbVaisseaux.set(0)
            self.vue.choisirNbVaisseaux.place_forget()
            self.vue.boutonEnvoyerFlotte.place_forget()
    
        

if __name__ == "__main__":
    c = Controleur()
    
