from abc import ABC
import sqlite3

# DAO = Data Access Object

class AbstractPlayerDAO (ABC):
    # Définition d'une classe abstraite d'un joueur DAO
    def __init__(self, database):
        "Connection to the database"
        self.mConnection = sqlite3.connect(database)
        self.mCursor = self.mConnection.cursor()

    # Definition des interfaces d'accès à la classe PlayerDAO
    ''' Recherche d'un joueur '''
    def find_Player (id_player):
        pass


    ''' Ajout d'un joueur dans la partie '''
    def add_Player (player):
        pass

    
    ''' Modification des informations d'un joueur '''
    def update_Player (player):
        pass


    ''' Achat d'une grosse opportunité '''
    def buy_Investment (big_deal):
        pass


    ''' Achat d'une petite opportunité '''
    def buy_Fund (small_deal):
        pass


    ''' Vente d'une propriété '''
    def sell_Investment (big_deal):
        pass


    ''' Vente des parts d'une entreprise '''
    def sell_Fund (small_deal):
        pass

#=============================================================================================

class AbstractPartyDAO (ABC):
    # Définition d'une classe abstraite d'une party DAO
    def __init__(self, database):
        "Connection to the database"
        self.mConnection = sqlite3.connect(database)
        self.mCursor = self.mConnection.cursor()

    
    ''' Sauvegarde d'une partie '''
    def save_Party (party):
        pass


    ''' Restauration d'une partie '''
    def load_Party (party):
        pass

    
    ''' Modification des données d'une partie '''
    def update_Party (party):
        pass


    ''' Recherche d'une partie '''
    def find_Party (id_party):
        pass