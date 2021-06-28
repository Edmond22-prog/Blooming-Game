from Business_Module.Player import Player
from Business_Module.Party import Party
from Business_Module.Game_Functions import *


print("     ____________________________")
print("\n*-_.*| WELCOME TO BLOOMING GAME |*._-*\n")
print("     ----------------------------\n")
while(True):
    print("1 - CREATE A PARTY")
    print("2 - LOAD A PARTY \n")
    init_choice = input("Your choice between 1 or 2 : ")
    if(init_choice in ("1", "2")):
        break
if(init_choice == "2"):
    print("No saving party !\nEnd of the game.")
else:
    playerName = input("Enter your name or surname : ")
    player1 = Player(playerName)
    party = Party([player1])
    print("NOW, THE PARTY BEGIN !!")
    player1.status()
    while(not FIRST_VERIFICATION(player1)):
        choice = main_actions()
        if(choice == "1" or choice == "i"):
            dice = player1.roll_dice()
            party.set_player1Position(dice)
            RAT_RACE(player1, party.get_player1Position())
        elif(choice == "2" or choice == "ii"):
            player1.status()
        elif(choice == "3" or choice == "iii"):
            player1.pay_debt()
        elif(choice == "4" or choice == "iv"):
            debt = int(input("\nHow much do you want to borrow : "))
            player1.borrow(debt)
        else:
            print("You leave the party !")
            party.quit_party(player1)       # À modifier avec la classe playerDAO
            break
    print("END OF THE GAME !")
