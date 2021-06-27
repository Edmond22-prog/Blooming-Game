from DAO_Module.Abstract import AbstractPlayerDAO

class PlayerDAO (AbstractPlayerDAO):
    def __init__(self, database):
        AbstractPlayerDAO.__init__(self, database)
        
    
    