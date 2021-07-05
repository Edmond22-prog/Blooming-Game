from Business_Module.Card import Card
from random import choice

class Opportunity (Card):
    def __init__(self, name, description, cost = 0, cashFlow = 0):
        "Initialization of an opportunity"
        Card.__init__(self, name, description)
        self.__mCost = cost
        self.__mCashFlow = cashFlow
    

    def get_cost(self):
        "Get the cost of the opportunity"
        return self.__mCost


    def set_cashFlow(self, cashF):
        self.__mCashFlow = cashF


    def get_cashFlow(self):
        "Get the cash flow that the opportunity provides"
        return self.__mCashFlow


# ==================================================================================================================

class Small_Deals (Opportunity):
    def __init__(self, name, description, cost, cashFlow, trading_interval = (0,1), shares_owned = 1, payDown = 0):
        "Initialization of a small deal"
        Opportunity.__init__(self, name, description, cost, cashFlow)
        self.__mTradingInterval = trading_interval
        self.__mSharesOwned = shares_owned
        self.__mPayDown = payDown
    

    def set_cost(self, cost):
        self.__mCost = cost
    
    
    def set_shares(self, numberShares):
        "Set the shares put for this opportunity"
        self.__mSharesOwned = numberShares
    

    def get_shares(self):
        "Get the shares put for this opportunity"
        return self.__mSharesOwned


    def get_tradingInterval (self):
        return self.__mTradingInterval


    def get_payDown(self):
        "Get the pay down of the opportunity"
        return self.__mPayDown
    

    def display(self):
        "Display of a small deal to a player"
        print("SMALL DEALS : {}".format(self.get_name()))
        print(self.get_description())
        print("Cost : {} Fcfa".format(self.get_cost()))
        print("Cash Flow : {} Fcfa".format(self.get_cashFlow()))
        if(self.get_payDown() == 0):
            print("Trading range : {} Fcfa to {} Fcfa".format(self.__mTradingInterval[0], self.__mTradingInterval[1]))
            print("Shares owned : {}\n".format(self.get_shares()))
        else:
            print("Pay Down : {} Fcfa".format(self.get_payDown()))
        print("")


#======================================================================================================================

class Big_Deals (Opportunity):
    def __init__(self, name, description, cost, cashFlow, payDown = 0):
        "Initialization of a big deal"
        Opportunity.__init__(self, name, description, cost, cashFlow)
        self.__mPayDown = payDown


    def get_payDown(self):
        "Get the pay down of the opportunity"
        return self.__mPayDown

    
    def display(self):
        "Display of a big deal to a player"
        print("BIG DEALS : {}".format(self.get_name()))
        print(self.get_description())
        print("Cost : {} Fcfa".format(self.get_cost()))
        print("Cash Flow : {} Fcfa".format(self.get_cashFlow()))
        print("Pay Down : {} Fcfa\n".format(self.get_payDown()))

#========================================================================================================#
# SMALL DEALS

# Small_Deals (nom_opportunité, description_opportunité, prix_achat, cashflow, intervalle_trading)
name01 = "Rare Gold Coin"
description01 = "Boming market raises share price of this long time marker"
cost01 = 125000
cashFlow01 = 0
trading_interval01 = (12500,100000)
shares_owned01 = 0
payDown01 = 0


name02 = "Motor Taxi"
description02 = "Buy motorcycle to put in selling condition"
cost02 = 450000
cashFlow02 = 0
trading_interval02 = (250000,600000)
shares_owned02 = 0
payDown02 = 0


name03 = "Egg Selling"
description03 = "To by and sell avicol product"
cost03 = 10000
cashFlow03 = 0
trading_interval03 = (7500,12500)
shares_owned03 = 0
payDown03 = 0


name04 = "Barman"
description04 = "Sell local brewing products"
cost04 = 500000
cashFlow04 = 2500
trading_interval04 = (0,1)
shares_owned04 = 0
payDown04 = 500000


name05 = "Waste Recycling"
description05 = "Buy and recycle plastic bottles from household waste"
cost05 = 300
cashFlow05 = 0
trading_interval05 = (100,1000)
shares_owned05 = 0
payDown05 = 0


name06 = "Cocoa Farmer"
description06= "Produce, harvest and sell cocoa at international prices/kg"
cost06 = 2500
cashFlow06 = 0
trading_interval06 = (1000,5000)
shares_owned06 = 0
payDown06 = 0


name07 = "Junk Yard"
description07 = "Buy scrap by the tonne and resell it to the importer by the tonne"
cost07 = 10000
cashFlow07 = 0
trading_interval07 = (2000,20000)
shares_owned07 = 0
payDown07 = 0


name08 = "Buy And Sell"
description08 = "Buy perishable agricultural products and get the best cost out of them according to their and condition"
cost08 = 20000
cashFlow08 = 0
trading_interval08 = (1000,100000)
shares_owned08 = 0
payDown08 = 0


small_Deals01 = Small_Deals(name01, description01, cost01, cashFlow01, trading_interval01, shares_owned01, payDown01)
small_Deals02 = Small_Deals(name02, description02, cost02, cashFlow02, trading_interval02, shares_owned02, payDown02)
small_Deals03 = Small_Deals(name03, description03, cost03, cashFlow03, trading_interval03, shares_owned03, payDown03)
small_Deals04 = Small_Deals(name04, description04, cost04, cashFlow04, trading_interval04, shares_owned04, payDown04)
small_Deals05 = Small_Deals(name05, description05, cost05, cashFlow05, trading_interval05, shares_owned05, payDown05)
small_Deals06 = Small_Deals(name06, description06, cost06, cashFlow06, trading_interval06, shares_owned06, payDown06)
small_Deals07 = Small_Deals(name07, description07, cost07, cashFlow07, trading_interval07, shares_owned07, payDown07)
small_Deals08 = Small_Deals(name08, description08, cost08, cashFlow08, trading_interval08, shares_owned08, payDown08)

list_Of_Small_Deals = [small_Deals01, small_Deals02, small_Deals03, small_Deals04, small_Deals05, small_Deals06, small_Deals07, small_Deals08]

def provide_smallDeal ():
    "Choose a small opportunity to a player"
    return choice(list_Of_Small_Deals)


# BIG DEALS

# Big_Deals (nom_opportunité, description_opportunité, prix_vente, cash flow, prix_achat)

name1 = "Construction Parthner"
description1 = "Looking for a partner to build a wing of the hospital"
cost1 = 1250000
cashFlow1 = 50000
payDown1 = 1250000


name2 = "House For Sale"
description2 = "Transferred skilled tradesman kept this  house in excellent condition, soit commands top XAF rentals in older neighborhood"
cost2 = 3350000
cashFlow2 = 20000
payDown2 = 600000


name3 = "Car Repaire"
description3 = "Purchase of a modern car garage with a good reputation"
cost3 = 10000000
cashFlow3 = 135000
payDown3 = 2000000


name4 = "Inter-city Transport Investment"
description4 = "An urban transport agency needs an investor to develop its activities in more cities"
cost4 = 11000000
cashFlow4 = 85000
payDown4 = 2000000


name5 = "Farm Investment"
description5 = "Production of beef, pork and chicken"
cost5 = 8000000
cashFlow5 = 50000
payDown5 = 1500000


name6 = "Telecom Business"
description6 = "buy and resell mobile phone services under license from National Telecom"
cost6 = 22000000
cashFlow6 = 50000
payDown6 = 8000000


name7 = "Agricultural Production"
description7 = "Production and export of corn and wheat"
cost7 = 90000000
cashFlow7 = 150000
payDown7 = 50000000


name8 = "Restaurant Business"
description8 = "Create a big cheptel of fastfood in country"
cost8 = 25000000
cashFlow8 = 75000
payDown8 = 15000000


name9 = "Sell Car"
description9 ="Open a massive place to selling car and main space to repair car"
cost9 = 50000000
cashFlow9 = 450000
payDown9 = 35000000


big_Deals1 = Big_Deals(name1, description1, cost1, cashFlow1, payDown1)
big_Deals2 = Big_Deals(name2, description2, cost2, cashFlow2, payDown2)
big_Deals3 = Big_Deals(name3, description3, cost3, cashFlow3, payDown3)
big_Deals4 = Big_Deals(name4, description4, cost4, cashFlow4, payDown4)
big_Deals5 = Big_Deals(name5, description5, cost5, cashFlow5, payDown5)
big_Deals6 = Big_Deals(name6, description6, cost6, cashFlow6, payDown6)
big_Deals7 = Big_Deals(name7, description7, cost7, cashFlow7, payDown7)
big_Deals8 = Big_Deals(name8, description8, cost8, cashFlow8, payDown8)
big_Deals9 = Big_Deals(name9, description9, cost9, cashFlow9, payDown9)

list_Of_Big_Deals = [big_Deals1, big_Deals2, big_Deals3, big_Deals4, big_Deals5, big_Deals6, big_Deals7, big_Deals8, big_Deals9]

def provide_bigDeal():
    "Choose a big opportunity to a player"
    return choice(list_Of_Big_Deals)