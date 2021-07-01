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
        print("\n=== OPTIONS ===")
        print("i - Status")
        print("ii - Pay a debt")
        print("iii - Borrow")
        print("iv - End the turn")
        print("v - Quit the party")
        choice = input("Your choice : ")
        if (choice in ("1","2","3","4","5","i","ii","iii","iv","v")):
            break
    return choice

    
# Fonction qui vérifie si le joueur est sorti de la RAT RACE
def CONGRATULATION_RAT_RACE (player):
    "Verify if the player get out of the RAT RACE"
    if(player.get_cashFlow() >= player.get_sum_monthExpenses()):
        print("\nCongratulations, {} get out of the RAT RACE".format(player.get_pseudo()))
        return True
    else:
        return False


# Fonction qui vérifie si le joueur est en faillite
def BANKRUPTCY (player):
    "Verify if the player is Bankruptcy"
    if (player.get_cash() < 0 and player.get_salary() + player.get_cashFlow() < player.get_sum_monthExpenses()):
        print("\nYou are bakrupt !")
        return True
    else:
        return False


# Fonction lançant les opérations nécessaire lorsque le joueur est en faillite
def actions_for_BANKRUPTCY (player):
    "Actions to be taken in case of bankruptcy"
    if (BANKRUPTCY(player)):
        a = False
        while (player.get_salary() + player.get_cashFlow() < player.get_sum_monthExpenses() or player.get_cash() < 0):
            if (len(player.get_investments()) != 0):
                while(True):
                    print("\nWhat big opportunity do you want to sell ?\nThe down payment will be reduced by 2 when you sell")
                    i = 1
                    for invest in player.get_investments():
                        print("{} - {} : {} Fcfa".format(i,invest.get_name(), invest.get_payDown()))
                    choice = input("Your choice : ")
                    if(int(choice) in range(1,len(player.get_investments()))):
                        break
                # Réduction de 1/2 du pay down de l'opportunité avant vente à la banque 
                player.get_investments()[int(choice)-1].set_payDown(0.5*player.get_investments()[int(choice)-1].get_payDown())
                player.sell_investment(player.get_investments()[int(choice)-1]) # Vente de l'opportunitée
            elif(len(player.get_funds() != 0)):
                while(True):
                    print("\nWhat small opportunity do you want to sell ?\nThe cost will be reduced by 2 when you sell")
                    i = 1
                    for fund in player.get_funds():
                        print("{} - {} : {} Fcfa".format(i,fund.get_name(), fund.get_cost()))
                    choice = input("Your choice : ")
                    if(int(choice) in range(1,len(player.get_funds()))):
                        break
                # Réduction de 1/2 du prix de l'opportunité avant vente à la banque 
                player.get_funds()[int(choice)-1].set_cost(0.5*player.get_funds()[int(choice)-1].get_cost())
                player.sell_funds(player.get_funds()[int(choice)-1]) # Vente de l'opportunitée  
            else:
                if(not a):
                    n = 0
                    for tupl in player.get_liabilities():   # Opérations pour réduire la somme des liabilities 2 et 3 de 1/2
                        if (tupl[0] != "Home Mortgage"):    # On ne modifie pas le Home Mortgage
                            tupl[1] = 0.5*tupl[1]
                            n += 1
                            if (n == 3):    # Lorsqu'on a modifié le 2 et le 3, on sort de la boucle
                                break
                    m = 0
                    for tupl in player.get_monthExpenses(): # Opérations pour réduire la somme des dépenses mensuelles 3 et 4 de 1/2
                        if (tupl[0] != "Taxes" and tupl[0] != "Home Mortgage Payment"):     
                            tupl[1] = 0.5*tupl[1]
                            m += 1
                            if (m == 4):
                                break
                    a = True
                else:
                    print("You are very bankrupt, quit the party !")


def IS_DOWNSIZED (player):
    # Cette première condition est nécessaire car cette fonction sera dans le while du Blooming game avec la fonction CONGRATULATIONS
    if (player.mDownsized):     # Si le joueur est tombé sur la case Downsized alors
        if (player.compteur < 6):       # Début du nombre de tour dans la situation, le compteur va augmenter à chaque appel de la fonction
            player.compteur += 1
            if (player.compteur == 6):      # Si il a déjà fait 3 tours dans cette situation, alors il sort du Downsized (donc on remet aux valeurs initiales)
                player.mDownsized = False
                player.compteur = 0
            return True         # Ce renvoi c'est pour dire que sa situation n'est pas finie
        else:
            return False    # Ce renvoi c'est pour dire que sa situation est finie
    else:
        return False


def INITIAL_PRESENTATION (player):
    "Presentation of the player profil in the game start"
    print("\nPRESENTATION PLAYER {}".format(player.get_pseudo()))
    print("You are a {}.".format(player.get_profession().get_name()))
    print("Your starting salary is {} Fcfa.".format(player.get_salary()))
    print("You have {} Fcfa in savings.".format(player.get_profession().get_savings()))
    print("This means you begin with {} Fcfa.".format(player.get_cash()))
    print("")



def RAT_RACE (player, player_position):
    ### Attérissage sur une case Opportunités
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
    ### Attérissage sur la case Marchés
    elif (player_position in (8,16,24)):
        print("\nYou lands on Markets")
        # A mettre à jour lorsque les cartes market seront fait
        print("No market for the moment")
    ### Attérissage sur la case Doodads
    elif(player_position in (2,10,18)):
        print("\nYou lands on Doodads")
        doodad = provide_doodads()
        doodad.display()
        actions_for_BANKRUPTCY(player)
        player.pay(doodad.get_toPay())
    ### Attérissage sur la case Charité
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
            player.do_a_charity()
        else:
            print("")
    ### Attérissage sur la case PAY CHECK
    elif(player_position in (6,14,22)):
        print("\nYou lands on PAY CHECK")
        # Le monthly_cash est la somme que le joueur reçoit à chaque PAY CHECK
        monthly_cash_flow = player.get_salary() + player.get_cashFlow() - player.get_sum_monthExpenses()
        player.receive(monthly_cash_flow)
        print("You receive your monthly cash flow !")
    ### Attérissage sur la case Bébé
    elif(player_position == 12):
        print("\nYou lands on Baby.\nCongrats, you have a baby !!")
        player.has_a_baby()
    ### Attérissage sur la case Downsized
    elif(player_position == 20):
        print("\nYou lands on Downsized.\nPay all your total expenses")
        actions_for_BANKRUPTCY(player)
        player.pay(player.get_sum_monthExpenses())
        player.mDownsized = True
        player.mCharity = False
        player.compteur = 0
    else:
        print("!!! ERROR !!!")



# def FAST_RACE (player, player_position):