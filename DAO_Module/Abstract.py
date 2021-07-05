from abc import ABC
import sqlite3

# DAO = Data Access Object

class AbstractPlayerDAO (ABC):

    # Definition des interfaces d'accès à la classe PlayerDAO
    ''' Recherche d'un joueur '''
    def find_Player (id_player):
        pass


    ''' Enregistrement d'un joueur dans la BD '''
    def register_Player (player):
        pass

    
    ''' Modification des informations d'un joueur '''
    def update_Player (id_player):
        pass


    ''' Enregistrement d'une grosse opportunité '''
    def register_Investment (big_deal):
        pass


    ''' Enregistrement d'une petite opportunité '''
    def register_Fund (small_deal):
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

    
    ''' Sauvegarde d'une partie '''
    def save_Party (party):
        pass


    ''' Restauration d'une partie '''
    def load_Party (id_party):
        pass

    
    ''' Suppression d'une partie sauvegardée '''
    def delete_Party (id_party):
        pass


    ''' Affichage des parties sauvegardées '''
    def show_Parts ():
        pass