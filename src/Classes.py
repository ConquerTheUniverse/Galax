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

        #Si le X est plus grand
        if(differenceX > differenceY):
            distance = differenceX
           
        #Si le Y est plus grand ou si les deux sont egaux
        else:
            distance = differenceY

        #Calculer l'annee d'arrivee
        if(distance <= 2):
            duree = distance / 2
        else:
            duree = 1 + ((distance- 2) / 3)

        self.anneeArrivee = anneeActuelle + duree
        

        
            
#Classe qui represente une etoile(manufactures, vaisseaux, etc.)
class Etoile:
    def __init__(self, posX, posY, nbManufactures, appartenance):
        self.posX = posX #Position en X de l'etoile sur la surface de jeu
        self.posY = posY #Position en Y de l'etoile sur la surface de jeu
        self.appartenance = appartenance #A qui cette etoile appartient (0 = Neutre, 1 = Humain, 2 = Gubrus et 3 = Czin)
        self.nbManufactures = nbManufactures #Nb de manufactures sur l'etoile
        self.nbVaisseaux = 0 #Nb de vaisseau sur l'etoile
        
