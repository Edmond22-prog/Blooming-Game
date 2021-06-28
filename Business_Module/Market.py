from Business_Module.Card import Card

class Market (Card):
    def __init__(self, name, description, opportunityTarget, gain = 0):
        "Initialization of a market"
        Card.__init__(self, name, description)
        self.__mGain = gain
        self.__mOpportunityTarget = opportunityTarget


    def display(self):
        "Display the market to the player"
        print("MARKET : {}".format(self.__mName))
        print(self.get_description())
        print("Investment/Fund target : {}".format(self.get_opportunityTarget()))
        print("Gain : {} Fcfa".format(self.get_gain()))


    def get_gain(self):
        return self.__mGain


    def get_opportunityTarget(self):
        return self.__mOpportunityTarget.get_name()