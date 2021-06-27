from DAO_Module.Abstract import AbstractPartyDAO

class PartyDAO (AbstractPartyDAO):
    def __init__(self, database):
        AbstractPartyDAO.__init__(self, database)