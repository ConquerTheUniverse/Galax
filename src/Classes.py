import math

#Contiendra toutes les informations relatives aux Humains (Joueur)
class Humains:
    def __init__(self):
        pass

#Contiendra toutes les informations relatives aux Gubrus
class Gubrus:
    def __init__(self):
        pass

#Contiendras toutes les informations relatives aux Czins
class Czins:
    def __init__(self):
        pass

#Classe qui represente une flotte de vaisseau(Nb, Destination, etc.)
class flotteDeVaisseaux:
    def __init__(self, quantiteVaisseaux, destination):
        self.quantiteVaisseaux = quantiteVaisseaux
        self.destination = destination
        self.anneeArrivee = 0
        

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
        
