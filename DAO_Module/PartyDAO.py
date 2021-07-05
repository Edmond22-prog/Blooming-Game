from Dao_Module.Abstract import AbstractPartyDAO
from Dao_Module.PlayerDAO import PlayerDAO
import sqlite3
from datetime import datetime


class PartyDAO (AbstractPartyDAO):
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


    def save_Party (self, party):
        save_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.__connection()

        # Insertion des données liées à la partie
        data_party = (party.get_partyType(), party.get_turn(), save_date, len(party.get_players()))
        requete1 = "INSERT INTO Partie (TypePartie, Tour, DateSauvegarde, NombreJoueur) VALUES (?,?,?,?)"
        self.__mCursor.execute(requete1,data_party)

        # Récupération de l'id de la partie
        date = (save_date, )
        self.__mCursor.execute("SELECT idPartie FROM Partie WHERE DateSauvegarde = ?", date)
        for result in self.__mCursor.fetchone():
            idParty = int(result)

        for player in party.get_players():
            # Enregistrement du joueur dans la BD
            player_dao = PlayerDAO(self.__database)
            idPlayer = player_dao.register_Player(player)

            # Liaison du joueur à la partie, avec sa position
            self.__mCursor.execute("INSERT INTO Jouer VALUES (?,?,?)", (idPlayer, idParty, party.get_playerPosition(player)))

            # Insertion des dettes du joueur
            for liability in player.get_liabilities():
                data_liability = (liability[0], liability[1])
                requete4 = "INSERT INTO Dette (Nom, Somme) VALUES (?,?)"
                self.__mCursor.execute(requete4, data_liability)

                # Récupération de l'id de la dette
                self.__mCursor.execute("SELECT idDette FROM Dette WHERE Nom = ? AND Somme = ?", data_liability)
                for result in self.__mCursor.fetchone():
                    idLiability = int(result)

                # Liaison du joueur à la dette dans la BD
                self.__mCursor.execute("INSERT INTO Avoir2 VALUES (?,?)", (idPlayer, idLiability))

            # Insertion des dépenses du joueur
            for expense in player.get_monthExpenses():
                data_expense = (expense[0], expense[1])
                requete5 = "INSERT INTO Depense (Nom, Somme) VALUES (?,?)"
                self.__mCursor.execute(requete5, data_expense)

                # Récupération de l'id de la dépense
                self.__mCursor.execute("SELECT idDepense FROM Depense WHERE Nom = ? AND Somme = ?", data_expense)
                for result in self.__mCursor.fetchone():
                    idExpense = int(result)

                # Liaison du joueur à la dépense dans la BD
                self.__mCursor.execute("INSERT INTO Avoir3 VALUES (?,?)", (idPlayer, idExpense))

            # Insertion des grandes opportunitées du joueur
            for big in player.get_investments():
                data_big = (big.get_name(), big.get_description(), big.get_cost(), big.get_cashFlow(), big.get_payDown())
                requete6 = "INSERT INTO Big_Deals (Nom, Description, Prix, CashFlow, Paiement) VALUES (?,?,?,?,?)"
                self.__mCursor.execute(requete6, data_big)

                # Récupération de l'id de l'opportunité
                self.__mCursor.execute("SELECT idBig FROM Big_Deals WHERE Nom = ?", (big.get_name(),))
                for result in self.__mCursor.fetchone():
                    idBig_deal = int(result)

                # Liaison du joueur à l'opportunité dans la BD
                self.__mCursor.execute("INSERT INTO Acheter_Big VALUES (?,?)", (idPlayer, idBig_deal))

            # Insertion des petites opportunitées du joueur
            for small in player.get_funds():
                data_small = (small.get_name(), small.get_description(), small.get_cost(), small.get_cashFlow(), small.get_payDown(), small.get_tradingInterval()[0], small.get_tradingInterval()[1])
                requete7 = "INSERT INTO Small_Deals (Nom, Description, Prix, CashFlow, Paiement, minTrade, maxTrade) VALUES (?,?,?,?,?,?,?)"
                self.__mCursor.execute(requete7, data_small)

                # Récupération de l'id de l'opportunité
                self.__mCursor.execute("SELECT idSmall FROM Small_Deals WHERE Nom = ?", (small.get_name(),))
                for result in self.__mCursor.fetchone():
                    idSmall_deal = int(result)

                # Liaison du joueur à l'opportunité dans la BD
                self.__mCursor.execute("INSERT INTO Acheter_Small VALUES (?,?,?)", (idPlayer, idSmall_deal, small.get_shares()))
        print("Save is done !\n")
        self.__mConnection.commit()
        self.__deconnection()



    def show_Parts(self):
        self.__connection()
        self.__mCursor.execute("SELECT * FROM Partie")
        results = list(self.__mCursor)
        if(len(results) == 0):
            print("No saving party !\n")
        else:
            for result in results:
                print("Party ID : {}; Date of save : {}; {}; Turn {}\n".format(result[0], result[3], result[1], result[2]))
        self.__deconnection()