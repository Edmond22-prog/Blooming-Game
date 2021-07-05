from Dao_Module.Abstract import AbstractPlayerDAO
import sqlite3


class PlayerDAO (AbstractPlayerDAO):
    def __init__(self, database):
        self.__database = database
        self.__connection()

    def __connection (self):
        "Connection to the database"
        self.__mConnection = sqlite3.connect(self.__database)
        self.__mCursor = self.__mConnection.cursor()
    

    def __deconnection (self):
        "Deconnection to the database"
        self.__mCursor.close()
        self.__mConnection.close()


    def register_profession (self, player_profession):
        self.__connection()
         # Insertion des données liées à la profession d'un joueur
        data_profession = (player_profession.get_name(), player_profession.get_salary(), player_profession.get_savings())
        requete2 = "INSERT INTO Profession (Nom, Salaire, Economie) VALUES (?,?,?)"
        self.__mCursor.execute(requete2, data_profession)

        # Récupération de l'id de la profession
        self.__mCursor.execute("SELECT idProfession FROM Profession WHERE Nom = ?", (player_profession.get_name(),))
        for result in self.__mCursor.fetchone():
            idProfession = int(result)
        self.__deconnection()
        return idProfession


    
    def register_Player(self, player):
        self.__connection ()
        #Enregistrement de la profession dans la BD et récupération de son id
        idProfession = self.register_profession(player.get_profession())
        
        # Insertion des données liées au joueur
        data_player = (player.get_pseudo(), player.get_dream(), player.get_cashFlow(), player.get_childNumber(), player.get_cash(), idProfession)
        requete3 = "INSERT INTO Joueur (Pseudo, Reve, CashFlow, NombreEnfant, Cash, idProfession) VALUES (?,?,?,?,?,?)"
        #requete3 = "INSERT INTO Joueur (Pseudo, Reve, CashFlow, NombreEnfant, Cash) VALUES (?,?,?,?,?)"
        self.__mCursor.execute(requete3, data_player)
        self.__mCursor.execute()

        # Récupération de l'id du joueur
        player_inf = (player.get_pseudo(), player.get_cash())
        self.__mCursor.execute("SELECT idJoueur FROM Joueur WHERE Nom = ? AND Cash = ?", player_inf)
        for result in self.__mCursor.fetchone():
            idPlayer = int(result)
        
        self.__deconnection()
        return idPlayer

    