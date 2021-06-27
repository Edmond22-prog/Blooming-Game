class Party (object):
    def __init__(self, playerList, player1Position = 1, player2Position = 1, player3Position = 1, lastToPlay = 0):
        "Initialization of a game party"
        self.__mPlayerList = playerList
        self.__mPartType = "Single Player"
        self.__mPlayer1Position = player1Position
        self.__mPlayer2Position = player2Position
        self.__mPlayer3Position = player3Position
        self.__mLastToPlay = lastToPlay


    def add_player(self, player):
        if(len(self.get_players()) < 3):
            self.__mPlayerList.append(player)
            self.__mPartType = "Multi Player"
        else:
            print("Could not add more players !")
    

    def get_players(self):
        return self.__mPlayerList


    def quit_party(self, player):
        for p in self.get_players():
            if(p.get_pseudo() == player.get_pseudo()):
                self.get_players().remove(player)
                return True
        return False
    

    # Fonction qui enregistre la position du joueur 1 dans le jeu
    def set_player1Position(self, number):
        self.__mPlayer1Position += number
        if(self.__mPlayer1Position > 24):
            self.__mPlayer1Position -= 24
        

    # Fonction qui renvoi la position du joueur 1
    def get_player1Position(self):
        return self.__mPlayer1Position


    def set_player2Position(self, number):
        self.__mPlayer2Position += number
        if(self.__mPlayer2Position > 24):
            self.__mPlayer2Position -= 24
        

    def get_player2Position(self):
        return self.__mPlayer2Position
    

    def set_player3Position(self, number):
        self.__mPlayer3Position += number
        if(self.__mPlayer3Position > 24):
            self.__mPlayer3Position -= 24
        

    def get_player3Position(self):
        return self.__mPlayer3Position
    

    # Détermine le prochain joueur à jouer, paradoxalement le dernier à avoir jouer aussi
    def next_to_play(self):
        if(len(self.get_players()) > 1):
            if(self.__mLastToPlay < len(self.get_players())-1):
                self.__mLastToPlay += 1
                print("It's {}'s turn".format(self.get_players()[self.__mLastToPlay]))
            else:
                self.__mLastToPlay = 0
                print("It's {}'s turn".format(self.get_players()[self.__mLastToPlay]))
        else:
            print("It's {}'s turn".format(self.get_players()[self.__mLastToPlay]))
