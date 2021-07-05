from Business_Module.Player import Player
from Business_Module.Party import Party
from Business_Module.Game_Functions import *
from Business_Module.Dreams import provide_dream
from Dao_Module.PartyDAO import PartyDAO


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
    dao_impl = PartyDAO("db_blooming_game.sq3")
    dao_impl.show_Parts()
else:
    playerName = input("\nPlayer 1, enter your name or surname : ")
    player1 = Player(playerName)
    party = Party([player1])
    INITIAL_PRESENTATION(player1)
    playerDream = provide_dream()
    player1.set_dream(playerDream)
    while(True):
        print("Do you want to add another players ? (Y/N)")
        reponse = input("Decision : ")
        if(reponse in ("Y","y","N","n")):
            break
    if (reponse in ("Y","y")):
        while(True):
            number_players = input("How many players : ")
            try:
                number_players = int(number_players)
                if(number_players > 0 and number_players <= 2):
                    for i in range (1,number_players+1):
                        player_name = input("Player {}, enter your name or surname : ".format(i+1))
                        player = Player(player_name)
                        party.add_player(player)
                        INITIAL_PRESENTATION(player)
                        dream = provide_dream()
                        player.set_dream(dream)
                    break
                else:
                    print("Enter a valid number !\nThe max of players for a game is 3")
            except:
                print("Enter a number, please.")
    print("\nNOW, THE PARTY BEGIN !!")
    turn = 1    # Compteur de tour
    while (len(party.get_players()) != 0):
        print("\nTURN {}".format(turn))
        for player in party.get_players():
            print("\nIs the turn of {}".format(player.get_pseudo()))
            if(IS_DOWNSIZED(player)):
                print("Can't play now, He/She is downsized !")
            ### RAT RACE ###
            while(not CONGRATULATION_RAT_RACE(player) and not IS_DOWNSIZED(player)):
                # Actions principales du joueur lorsque c'est son tour de jouer
                choice = main_actions()
                if(choice == "1" or choice == "i"):
                    dice = player.roll_dice()
                    party.set_playerPosition(player, dice)
                    RAT_RACE(player, party.get_playerPosition(player))
                    # Actions secondaires du joueur après avoir lancer le dé
                    while (True):
                        choicein = second_actions()
                        if(choicein in ("i", "1")):
                            player.status()
                        elif(choicein in ("ii", "2")):
                            player.pay_debt()
                        elif(choicein in ("iii", "3")):
                            while (True):
                                debt = input("\nHow much do you want to borrow : ")
                                try:
                                    # La somme prêtée doit être un multiple de 100000
                                    summ = int(debt)
                                    if (summ > 100000 and summ%100000 == 0):
                                        player.borrow(debt)
                                        break
                                    else:
                                        print("Enter a valid sum !\nThe sum must be a multiple of 100000")
                                except:
                                    print("Enter a sum !")
                        elif(choicein in ("iv", "4")):
                            print("End of the turn of {}".format(player.get_pseudo()))
                            break
                        else:
                            while(True):
                                print("\nARE YOU SURE, YOU WANT TO QUIT THE PARTY ? (Y/N)")
                                decision = input("Your decision : ")
                                if (decision in ("Y","y","N","n")):
                                    break
                            if(decision in ("Y","y")):
                                party.quit_party(player)       # À modifier avec la classe playerDAO
                                break
                            else:
                                print("Continue the game !")
                    break     
                elif(choice == "2" or choice == "ii"):
                    player.status()
                elif(choice == "3" or choice == "iii"):
                    player.pay_debt()
                elif(choice == "4" or choice == "iv"):
                    while (True):
                        debt = input("\nHow much do you want to borrow : ")
                        try:
                            # La somme prêtée doit être un multiple de 100000
                            summ = int(debt)
                            if (summ > 100000 and summ%100000 == 0):
                                player.borrow(debt)
                                break
                            else:
                                print("Enter a valid sum !\nThe sum must be a multiple of 100000")
                        except:
                            print("Enter a sum !")
                else:
                    while(True):
                        print("\nARE YOU SURE, YOU WANT TO QUIT THE PARTY ? (Y/N)")
                        decision = input("Your decision : ")
                        if (decision in ("Y","y","N","n")):
                            break
                    if(decision in ("Y","y")):
                        '''while(True):
                            print("\nDO YOU WANT TO SAVE THE PARTY ? (Y/N)")
                            decision = input("Your decision : ")
                            if (decision in ("Y","y","N","n")):
                                break
                        if(decision in ("Y","y")):
                            dao_impl = PartyDAO("db_blooming_game.sq3")
                            dao_impl.save_Party(party)'''
                        party.quit_party(player)       # À modifier avec la classe playerDAO
                        break
                    else:
                        print("Continue the game !")
        turn += 1
        party.set_turn(turn)
    print("END OF THE GAME !")
