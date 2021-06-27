from Business_Module.Player import Player
from Business_Module.Party import Party

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
    while(True):
        while(True):
            print("i - Roll the dice")
            print("ii - Pay a debt")
            print("iii - Borrow")
            print("iv - Quit the party")
            choice = input("Your choice : ")
            if(choice in ("1","2","3","4","i","ii","iii","iv")):
                break
        if(choice == "1" or choice == "i"):
            player1.roll_dice()
            print("You land on Baby\nCongrats, you have a child !!")
            player1.has_a_baby()
            player1.status()
        elif(choice == "2" or choice == "ii"):
            player1.pay_debt()
            player1.status()
        elif(choice == "3" or choice == "iii"):
            debt = int(input("\nHow much do you want to borrow : "))
            player1.borrow(debt)
            player1.status()
        else:
            print("You leave the party !")
            party.quit_party(player1)
            break
    print("END OF THE GAME !")
