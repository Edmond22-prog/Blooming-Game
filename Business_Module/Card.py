class Card (object):
    def __init__(self, name = "Name", description = "Description"):
        "Abstract class of a card initialization"
        self.__mName = name
        self.__mDescription = description
    

    def get_name (self):
        "Get the name of the card"
        return self.__mName


    def get_description (self):
        "Get the description of the card"
        return self.__mDescription