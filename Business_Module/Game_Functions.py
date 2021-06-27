from Business_Module.Doodads import provide_doodads 
from Business_Module.Opportunity import provide_bigDeal, provide_smallDeal


def main_actions ():
    while(True):
        print("i - Roll the dice")
        print("ii - Status")
        print("iii - Pay a debt")
        print("iv - Borrow")
        print("v - Quit the party")
        choice = input("Your choice : ")
        if (choice in ("1","2","3","4","5","i","ii","iii","iv","v")):
            break
    return choice


def RAT_RACE (player, player_position):
    if (player_position in (1,3,5,7,9,11,13,15,17,19,21,23)):
        print ("\nYou lands on Opportunities")
        while (True):
            print ("What kind of opportunity do you want to seize ?")
            print ("1 - SMALL DEALS")
            print ("2 - BIG DEALS")
            choice = input("Your choice : ")
            if (choice in ("1","2")):
                break
        if (choice == "1"):
            small = provide_smallDeal()
            print("")
            small.display()
            while (True):
                print("(A) - BUY\t(B) - CANCEL")
                choicein = ("Your choice : ")
                if (choicein in ("A", "a", "1", "B", "b", "2")):
                    break
            if (choicein in ("A", "a", "1")):
                if (small.get_payDown() == 0):
                    while(True):
                        print("How many shares you want ?")
                        sharesStr = input("Shares : ")
                        try:
                            shares = int(sharesStr)
                            if (shares > 0):
                                if (player.get_cash() < small.get_cost()*shares):
                                    print("Number of shares too high compared to cash")
                                else:
                                    small.set_shares(shares)
                                    player.buy_funds(small)
                                    break
                            else:
                                print("Enter a valid number !")
                        except:
                            print("Enter a number !")
                else:
                    player.buy_funds(small)
            else:
                print("")
        if (choice == "2"):
            big = provide_bigDeal()
            print("")
            big.display()
            while (True):
                print("(A) - BUY\t(B) - CANCEL")
                choicein = ("Your choice : ")
                if (choicein in ("A", "a", "1", "B", "b", "2")):
                    break
            if (choicein in ("A", "a", "1")):
                player.buy_investment(big)
            else:
                print("")
    elif (player_position in (8,16,24)):
        print("\nYou lands on Markets")
        # A mettre à jour lorsque les cartes market seront fait
        print("No market for the moment")
    elif(player_position in (2,10,18)):
        print("\nYou lands on Doodads")
        doodad = provide_doodads()
        doodad.display()
        player.pay(doodad.get_toPay())