import math

#Contiendra toutes les informations relatives aux Humains (Joueur)
class Humains:
    def __init__(self, parent):
        self.parent = parent
        self.etoileMere = 0
        self.nbEtoiles = 0
        self.listePossessions = [] #initialisation de la liste des Etoiles possedees par les humains
        self.listeFlottes = [] #initialisation de la liste de flottes creees par les humains

#Contiendra toutes les informations relatives aux Gubrus
class Gubrus:
    def __init__(self, parent):
        # constantes
        NB_VAISSEAUX_PAR_ATTAQUE = 5
        FORCE_ATTAQUE_BASIQUE =10
        
        # variables
        self.parent = parent
        self.etoileMere = 0
        self.nbEtoiles = 0
        self.listePossession = [] 
        self.listeFlotte = []
        
    def strategieAttaque(self):
        pass
    
    
    def forceAttaque(self):
        pass
    
    
    def formationDeFlotte(self):
        pass

#Contiendras toutes les informations relatives aux Czins
class Czins:
    def __init__(self, parent):
        # constantes
        DISTANCE_GRAPPE =  4
        NB_VAISSEAUX_PAR_ATTAQUE = 4
        FORCE_ATTAQUE_BASIQUE =20
        
        # variables
        self.parent = parent
        self.etoileMere = 0
        self.base = 0
        self.nbEtoiles = 0
        self.listePossessions = [] #initialisation de la liste des Etoiles possedees par les Czins
        self.listeFlottes = [] #initialisation de la liste de flottes creees par les Czins
        rassemblement_force = True
        conquerir_grape = False
        etablir_base = False
        positionEtoileBase = [] # va contenir la valeur en X et Y de la position de l'etoile base

    def definirValeurGrappe(self, modele):

        distance_grappe = 4
        
        for etoileValeurGrappe in modele.listeEtoile:
        
            for etoileACompter in modele.listeEtoile:
                #Si les deux etoiles ne sont pas la meme
                if(etoileACompter != etoileValeurGrappe):

                    #Pour calculer la distance
                    differenceX = abs(etoileValeurGrappe.posX - etoileACompter.posX)
                    differenceY = abs(etoileValeurGrappe.posY - etoileACompter.posY)

                    #Calculer la distance a l'aide du theoreme de pythagore
                    distance=math.sqrt(math.pow(differenceX, 2)+math.pow(differenceY, 2))
                
                    #Si la position est au moins a 4 de difference
                    if(distance <= distance_grappe):
                        s = distance_grappe - distance + 1
                        etoileValeurGrappe.valeur_grappe += s
                    
                        


    def definirValeurBase(self, modele):
        
        for etoile in modele.listeEtoile:

            #Pour calculer la distance
            differenceX = abs(etoile.posX - modele.listeEtoile[self.etoileMere].posX)
            differenceY = abs(etoile.posY - modele.listeEtoile[self.etoileMere].posY)

            #Calculer la distance a l'aide du theoreme de pythagore
            distance=math.sqrt(math.pow(differenceX, 2)+math.pow(differenceY, 2))

            #Si la valeur_grappe = 0
            if(etoile.valeur_grappe == 0):
                etoile.valeur_base = 0
            else:
                etoile.valeur_base = etoile.valeur_grappe-3 * distance

    
    def choisirGrappe(self):
        pass
    
    def etablirBase(self):
        pass
    
    def forceAttaque(self):
        pass
    

#Classe qui represente une flotte de vaisseau(Nb, Destination, etc.)
class flotteDeVaisseaux:
    def __init__(self, quantiteVaisseaux, destination, proprietaire):
        self.quantiteVaisseaux = quantiteVaisseaux
        self.destination = destination
        self.anneeArrivee = 0
        self.proprietaire = proprietaire
        

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

        self.anneeArrivee = anneeActuelle + duree
        

        
            
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
        valeur_grappe = 0 #Nb d'etoiles qui sont a 4 ou moins de distance
        valeur_base = 0 
        

    def genererVaisseau(self):
        pass
        
    def calculerValeurGrappe(self):
        pass
    
    def calculerValeurBase(self):
        pass