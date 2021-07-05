from random import shuffle

class Dream (object):
    def __init__(self, description, cost):
        self.__mDescription = description 
        self.__mCost= cost

    def set_description(self, description):
        self.__mDescription = description

    def get_description(self):
        return self.__mDescription
    
    def set_cost(self, cost):
        self.__mCost = cost

    def get_cost(self):
        return self.__mCost    


dream1 = Dream ("GO AROUND THE WORLD", 50000000)                      # Faire le tour du monde
dream2 = Dream ("BECOME A PILOT", 100000000)                           # Devenir pilote
dream3 = Dream ("BUY A VILLA", 50000000)                              # Acheter une villa
dream4 = Dream ("BUILD A POKER ROOM", 1000000000)                      # Construire une salle de poker
dream5 = Dream ("HAVE A PRIVATE JET", 200000000)                       # Avoir un jet privé
dream6 = Dream ("HAVE A CRUISE SHIP", 300000000)                       # Avoir un navire de croisière
dream7 = Dream ("MAKE A HOLIDAY IN THE MOUNTAINS", 150000000)          # Faire des vacances en montagne
dream8 = Dream ("HAVE A COLLECTION OF CARS",3000000000)                # Avoir une collection de voitures
dream9 = Dream ("BE AN AN ASTRONAUT",100000000)                       # Être astronaute
dream10 = Dream ("LIVING IN JAPAN",25000000)                         # Vivre au japon
dream11 = Dream ("GO TO HAWAII",30000000)                            # Aller à hawaï
dream12 = Dream ("RUNNING FOR PRESIDENT",25000000)                  # Se présenter à la présidence
dream13 = Dream ("OPEN A ZOO",1000000000)                              # Ouvrir un zoo
dream14 = Dream ("BUILDING A HYPERMARKET",70000000)                  # Construire un hypermarché
dream15 = Dream ("CREATE A TRADING COMPANY",200000000)                # Créer une entreprise de trading
dream16 = Dream ("BUILDING A TRAINING SCHOOL",500000000)              # Construire une école de formation
dream17 = Dream ("BUY A VILLA BY THE SEA",2000000000)                  # S'acheter une villa au bord de mer
dream18 = Dream ("MAKE A VIDEO GAME CONSOLE COLLECTION",20000000)    # Faire une collection de console de jeu vidéo
dream19 = Dream ("VOLUNTEERING IN POOR COUNTRIES",300000000)          # Faire du bénévolat dans les pays pauvres
dream20 = Dream ("CREATE AN APPLICATION",500000)                   # Créer une application
dream21 = Dream ("SPEND YOUR HONEYMOON IN CANADA",8000000)          # Passer sa lune de miel au Canada
dream22 = Dream ("OPENING A MOVIE THEATER",1000000)                 # Ouvrir une salle de cinéma
dream23 = Dream ("CREATE AN ASIAN SITE",80000000)                    # Créer un site asiatique

list_dreams = [dream1, dream2, dream3, dream4, dream5, dream6, dream7, dream8, 
                dream9, dream10, dream11, dream12, dream13, dream14, dream15, dream16,
                dream17, dream18, dream19, dream20, dream21, dream22, dream23]


def provide_dream ():
    while(True):
        print("\nWhat is your dream ?")
        i = 1
        for dream in list_dreams:
            print("{} - {}".format(i, dream.get_description()))
            i += 1
        choice = input("Your dream : ")
        try:
            choice = int(choice)
            if(choice in range(1,24)):
                break
            else:
                print("Make a good choice from what is on offer !")
        except:
            print("Enter a number !")
    print("Dream selected !\n")
    return list_dreams[choice-1]