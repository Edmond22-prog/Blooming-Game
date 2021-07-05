class Party (object):
    def __init__(self, playerList, playersPosition = [1,1,1], partyType = "Single Player", turn = 1):
        "Initialization of a game party"
        self.__mPlayerList = playerList
        self.__mPartyType = partyType
        self.__mPlayersPosition = playersPosition
        self.__mTurn = turn


    def add_player(self, player):
        if(len(self.get_players()) < 3):
            self.__mPlayerList.append(player)
            self.__mPartyType = "Multi Player"
        else:
            print("Could not add more players !")
    

    def get_players(self):
        "Get all the players of the party"
        return self.__mPlayerList
    

    def get_playersPosition(self):
        "Get the position of all the players"
        return self.__mPlayersPosition
    

    def get_partyType(self):
        "Get the type of the party"
        return self.__mPartyType

    
    def set_turn (self, turn):
        self.__mTurn = turn
        

    def get_turn(self):
        return self.__mTurn


    def quit_party(self, player):
        for p in self.get_players():
            if(p.get_pseudo() == player.get_pseudo()):
                print("{} leave the party.".format(player.get_pseudo()))
                self.get_players().remove(player)
                return True
        return False
    

    # Fonction qui enregistre la position du joueur dans le jeu
    def set_playerPosition(self, player, number):
        "Set the position of a player in a party"
        for tupl in enumerate(self.get_players()):  # Recherche du joueur dans la liste des joueurs
            if (tupl[1] == player):     # Dès qu'on retrouve le joueur, on a son indice dans la liste
                position = self.get_playersPosition()[tupl[0]] + number     # À sa position actuelle, on ajoute la valeur du dé lancé et obtient sa nouvelle position
                if(position > 24):  # Si cette position est supérieure à la norme 24, on retranche
                    position -= 24
                self.get_playersPosition()[tupl[0]] = position  # On ajoute sa nouvelle position à la liste des positions des joueurs
                break
        

    # Fonction qui renvoi la position du joueur
    def get_playerPosition(self, player):
        "Get the position of a player in a party"
        for tupl in enumerate(self.get_players()):
            if (tupl[1] == player):
                return self.get_playersPosition()[tupl[0]]
    

