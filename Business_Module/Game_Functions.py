from Business_Module.Doodads import provide_doodads 
from Business_Module.Opportunity import provide_bigDeal, provide_smallDeal


def main_actions ():
    while(True):
        print("\n=== OPTIONS ===")
        print("i - Roll the dice")
        print("ii - Status")
        print("iii - Pay a debt")
        print("iv - Borrow")
        print("v - Quit the party")
        choice = input("Your choice : ")
        if (choice in ("1","2","3","4","5","i","ii","iii","iv","v")):
            break
    return choice


def second_actions ():
    while(True):
        print("=== OPTIONS ===")
        print("i - Status")
        print("ii - Pay a debt")
        print("iii - Borrow")
        print("iv - End the turn")
        print("v - Quit the party")
        choice = input("Your choice : ")
        if (choice in ("1","2","3","4","5","i","ii","iii","iv","v")):
            break
    return choice

    

def CONGRATULATION_RAT_RACE (player):
    "Verify if the player get out of the RAT RACE"
    if(player.get_cashFlow() >= player.get_sum_monthExpenses()):
        print("\nCongratulations, {} get out of the RAT RACE".format(player.get_pseudo()))
        return True
    else:
        return False



def BANKRUPTCY (player):
    "Verify if the player is Bankruptcy"
    if (player.get_cash() < 0 and player.get_salary() + player.get_cashFlow() < player.get_sum_monthExpenses()):
        return True
    else:
        return False



def actions_for_BANKRUPTCY (player):
    "Actions to be taken in case of bankruptcy"
    




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
            print("Your cash = {} Fcfa".format(player.get_cash()))
            while (True):
                print("\n(A) - BUY\t(B) - CANCEL")
                choicein = input("Your choice : ")
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
            print("Your cash = {} Fcfa".format(player.get_cash()))
            while (True):
                print("\n(A) - BUY\t(B) - CANCEL")
                choicein = input("Your choice : ")
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
    elif(player_position == 4):
        print("\nYou lands on Charity")
        print("\nDo you want to do charity ? If you accept, in exchange for 10%\n"+
        "of your total entries you will receive 2 dice for 3 rounds")
        while(True):
            print("(A) - ACCEPT\t(B) - REFUSE")
            choicein = input("Your choice : ")
            if (choicein in ("A","a","1","B","b","2")):
                break
        if (choicein in ("A","a","1")):
            charity = (player.get_salary() + player.get_cashFlow())*0.1
            player.pay(charity)
            print("You have 2 dice in the next 3 rounds.")
        else:
            print("")
    elif(player_position in (6,14,22)):
        print("\nYou lands on PAY CHECK")
        # Le monthly_cash est la somme que le joueur reçoit à chaque PAY CHECK
        monthly_cash_flow = player.get_salary() + player.get_cashFlow() - player.get_sum_monthExpenses()
        player.receive(monthly_cash_flow)
        print("You receive your monthly cash flow !")
    elif(player_position == 12):
        print("\nYou lands on Baby.\nCongrats, you have a baby !!")
        player.has_a_baby()
    elif(player_position == 20):
        print("\nYou lands on Downsized.\nPay all your total expenses")
        player.pay(player.get_sum_monthExpenses())
    else:
        print("!!! ERROR !!!")