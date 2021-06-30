from Business_Module.Card import Card
from random import choice


class Doodads (Card):
    def __init__(self, name = None, description = "Description", toPay = 0):
        "Initialisation of a doodad"
        Card.__init__(self, name, description)
        self.__mToPay = toPay


    def display(self):
        "Display the doodads to the player"
        print("DOODADS")
        print(self.get_description())
        print("To pay : {} Fcfa".format(self.get_toPay()))
    

    def get_toPay(self):
        return self.__mToPay


#=======================================================================================================#
description1, topay1 = "Loss of a sports bet" , 5000
doodad1 = Doodads(description = description1, toPay = topay1)

description2, topay2 = "Makeover your home", 20000
doodad2 = Doodads(description = description2, toPay = topay2)

description3, topay3 = "Redo wardrobe", 35000
doodad3 = Doodads(description = description3, toPay = topay3)

description4, topay4 = "Unnecessary expenses", 2000
doodad4 = Doodads(description = description4, toPay = topay4)  

description5, topay5 = "Agression", 10000
doodad5 = Doodads(description = description5, toPay = topay5)

description6, topay6 = "Two weeks of illness", 7000
doodad6 = Doodads(description = description6, toPay = topay6)

description7, topay7 = "Accident road", 10000
doodad7 = Doodads(description = description7, toPay = topay7)

description8, topay8 = "Burglary, loss of valuable jewelry", 90000
doodad8 = Doodads(description = description8, toPay = topay8)

description9, topay9 = "Birthday organization", 30000
doodad9 = Doodads(description = description9, toPay = topay9)


list_doodads = [doodad1, doodad2, doodad3, doodad4, doodad5, doodad6, doodad7, doodad8, doodad9]

def provide_doodads ():
    return choice(list_doodads)