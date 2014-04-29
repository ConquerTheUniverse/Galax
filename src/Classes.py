import math

#Contiendra toutes les informations relatives aux Humains (Joueur)
class Humains:
    def __init__(self, parent):
        self.parent = parent
        self.mort = False
        self.etoileMere = 0
        self.nbEtoiles = 0
        self.listePossessions = [] #initialisation de la liste des Etoiles possedees par les humains
        self.listeFlottes = [] #initialisation de la liste de flottes creees par les humains

#Contiendra toutes les informations relatives aux Gubrus
class Gubrus:
    def __init__(self, parent):
        # constantes
        self.NB_VAISSEAUX_PAR_ATTAQUE = 5
        self.FORCE_ATTAQUE_BASIQUE =10
        self.GARNISONMINIMALE = 15
        self.GARNISONLIMITE = 25
        
        # variables
        self.parent = parent
        self.mort = False
        self.etoileMere = 0
        self.nbEtoiles = 0
        self.listePossessions = []
        self.cible = []
        self.cibletemp = []
        self.listeFlottes = []

        #trouve la planete la plus proche
    def strategieAttaque(self, modele):
        x = modele.listeEtoiles[self.etoileMere].posX
        y = modele.listeEtoiles[self.etoileMere].posY
        e = None
        distance = 100000000
        
        for etoile in modele.listeEtoiles:
            differenceX = abs(etoile.posX - x)
            differenceY = abs(etoile.posY - y)
            valeurTemp = math.sqrt(math.pow(differenceX, 2) + math.pow(differenceY, 2))
            if(valeurTemp < distance and etoile != modele.listeEtoiles[self.etoileMere] and etoile.proprietaire != 2):
                e = etoile
                distance = valeurTemp
        return e
                        
    
    
    def forceAttaque(self, modele, temps_courant):
        if((temps_courant*self.NB_VAISSEAUX_PAR_ATTAQUE+self.FORCE_ATTAQUE_BASIQUE) > self.FORCE_ATTAQUE_BASIQUE*2):
            
            force_attaque = int(temps_courant*self.NB_VAISSEAUX_PAR_ATTAQUE+self.FORCE_ATTAQUE_BASIQUE)
            return force_attaque
        else:
            force_attaque = int(self.FORCE_ATTAQUE_BASIQUE*2)
            return force_attaque
    
    
    def formationDeFlotte(self, modele, temps_courant):
        if(modele.self.listeFlottes[self.etoileMere] > (self.forceAttaque(modele, temps_courant)+ self.FORCE_ATTAQUE_BASIQUE)):
            nbrDeVaisseauxParFlotte = int(modele.self.listeFlottes[self.etoileMere]/forceAttaque(modele, temps_courant))
            for i in range(nbrDeVaisseauxParFlotte):
                e = self.strategieAttaque(modele)
            for i in self.cible:
                self.listeFlottes.append(i)

#Contiendras toutes les informations relatives aux Czins
class Czins:
    def __init__(self, parent):
        # constantes
        self.DISTANCE_GRAPPE =  4
        self.NB_VAISSEAUX_PAR_ATTAQUE = 4
        self.FORCE_ATTAQUE_BASIQUE =20
        
        # variables
        self.parent = parent
        self.etoileMere = 0
        self.base = 0
        self.mort = False
        self.nbEtoiles = 0
        self.listePossessions = [] #initialisation de la liste des Etoiles possedees par les Czins
        self.listeFlottes = [] #initialisation de la liste de flottes creees par les Czins
        self.rassemblement_force = True
        self.conquerir_grappe = False
        self.etablir_base = False
        positionEtoileBase = [] # va contenir la valeur en X et Y de la position de l'etoile base

        

    def definirValeurGrappe(self, modele):
        
        for etoileValeurGrappe in modele.listeEtoiles:
        
            for etoileACompter in modele.listeEtoiles:
                #Si les deux etoiles ne sont pas la meme
                if(etoileACompter != etoileValeurGrappe):

                    #Pour calculer la distance
                    differenceX = abs(etoileValeurGrappe.posX - etoileACompter.posX)
                    differenceY = abs(etoileValeurGrappe.posY - etoileACompter.posY)

                    #Calculer la distance a l'aide du theoreme de pythagore
                    distance=math.sqrt(math.pow(differenceX, 2)+math.pow(differenceY, 2))
                
                    #Si la position est au moins a 4 de difference
                    if(distance <= self.DISTANCE_GRAPPE):
                        s = self.DISTANCE_GRAPPE - distance + 1
                        etoileValeurGrappe.valeur_grappe += s
                    
                        


    def definirValeurBase(self, modele):
        
        for etoile in modele.listeEtoiles:

            #Pour calculer la distance
            differenceX = abs(etoile.posX - modele.listeEtoiles[self.etoileMere].posX)
            differenceY = abs(etoile.posY - modele.listeEtoiles[self.etoileMere].posY)

            #Calculer la distance a l'aide du theoreme de pythagore
            distance=math.sqrt(math.pow(differenceX, 2)+math.pow(differenceY, 2))

            #Si la valeur_grappe = 0
            if(etoile.valeur_grappe == 0):
                etoile.valeur_base = 0
            else:
                etoile.valeur_base = etoile.valeur_grappe-3 * distance

    
    def etablirBase(self, modele):
        plusGrandeValeur = 0
        etoileChoix = None

        #Regrade valeur_grappe de chacune des etoiles
        for etoile in modele.listeEtoiles:
            #Si la valeur grappe est plus haute que la valeur retenu presentement il faut la changer sinon continuer la boucle
            if(etoile.valeur_base > plusGrandeValeur and etoile.proprietaire != 3):
                plusGrandeValeur = etoile.valeur_base
                etoileChoix = etoile

            
        return etoileChoix
    
    
    def forceAttaque(self, temps_courant):
        force_attaque = temps_courant*self.NB_VAISSEAUX_PAR_ATTAQUE*self.FORCE_ATTAQUE_BASIQUE
        return force_attaque 
    

#Classe qui represente une flotte de vaisseau(Nb, Destination, etc.)
class flotteDeVaisseaux:
    def __init__(self, quantiteVaisseaux, depart, destination, proprietaire, annee):
        self.quantiteVaisseaux = quantiteVaisseaux
        self.depart = depart
        self.destination = destination
        self.anneeArrivee = self.calculerArrivee(self.depart, annee)
        print(self.anneeArrivee)
        self.proprietaire = proprietaire
        self.armada = False
        
        

    #Permet de calculer l'annee d'arrivee en fonction de la destination
    def calculerArrivee(self, etoileDepart, anneeActuelle):
        #Pour calculer la distance
        differenceX = abs(etoileDepart.posX - self.destination.posX)
        differenceY = abs(etoileDepart.posY - self.destination.posY)

        #Calculer la distance a l'aide du theoreme de pythagore
        distance=math.sqrt(math.pow(differenceX, 2)+math.pow(differenceY, 2))

        #Calculer l'annee d'arrivee
        if(distance <= 2):
            duree = distance / 2
        else:
            duree = 1 + ((distance- 2) / 3)

         
        return anneeActuelle + duree
        
        

        
            
#Classe qui represente une etoile(manufactures, vaisseaux, etc.)
class Etoile:
    def __init__(self, posX, posY, nbManufactures, proprietaire):
        self.posX = posX #Position en X de l'etoile sur la surface de jeu
        self.posY = posY #Position en Y de l'etoile sur la surface de jeu
        self.proprietaire = proprietaire #A qui cette etoile appartient (0 = Neutre, 1 = Humain, 2 = Gubrus et 3 = Czin)
        self.nbManufactures = nbManufactures #Nb de manufactures sur l'etoile
        self.nbVaisseaux = 0 #Nb de vaisseau sur l'etoile
        self.niveauInfo = 0 
        self.nbVaisseuxDerniereVisite = 0 #Nb de vaisseau lors de la derniere visite
        self.valeur_grappe = 0 #Nb d'etoiles qui sont a 4 ou moins de distance
        self.valeur_base = 0 
        

    def genererVaisseau(self):
        pass
        
    def calculerValeurGrappe(self):
        pass
    
    def calculerValeurBase(self):
        pass

