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
        
    
    