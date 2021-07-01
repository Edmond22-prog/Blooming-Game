from random import choice

class Profession (object):
  def __init__(self, name = "Name_profession", salary = 0, savings = 0, liabilities = [], monthExpenses = []):
    "Initialisation of a profession"
    self.mName = name
    self.mSalary = salary
    self.mSavings = savings
    self.mLiabilities = liabilities     # Représente toutes les dettes du Joueur
    self.mMonthExpenses = monthExpenses     # Représente les dettes du joueur reparties par mois

  def get_name(self):
    return self.mName

  def get_salary(self):
    return self.mSalary

  def get_savings(self):
    return self.mSavings

  def get_liabilities(self):
    return self.mLiabilities

  def get_monthExpenses(self):
    return self.mMonthExpenses

#=================================================================================================================

name1, salary1, savings1 = "Programmer", 350000, 25000
liabilities1 = [
  ("Home Mortgage", 1500000),
  ("Car Loans", 1000000),
  ("Credit Card", 400000)
]
monthExpenses1 = [
  ("Taxes", 30000),
  ("Home Mortgage Payment", 25000),
  ("Car Loans Payment", 20000),
  ("Credit Card Payment", 10000),
  ("Other Expenses", 80000),
  ("Child(s) Expenses", 0)
]
profession1 = Profession(name1, salary1, savings1, liabilities1, monthExpenses1)

name2, salary2, savings2 = "Primary School Teacher", 200000, 20000
liabilities2 = [
  ("Home Mortgage", 1500000),
  ("Car Loans", 1000000),
  ("Credit Card", 50000)
]
monthExpenses2 = [
  ("Taxes", 20000),
  ("Home Mortgage Payment", 15000),
  ("Car Loans Payment", 20000),
  ("Credit Card Payment", 5000),
  ("Other Expenses", 50000),
  ("Child(s) Expenses", 0)
]
profession2 = Profession(name2, salary2, savings2, liabilities2, monthExpenses2)

name3, salary3, savings3 = "Secondary School Teacher", 300000, 25000
liabilities3 = [
  ("Home Mortgage", 1500000),
  ("Car Loans", 1000000),
  ("Credit Card", 200000)
]
monthExpenses3 = [
  ("Taxes", 30000),
  ("Home Mortgage Payment", 25000),
  ("Car Loans Payment", 20000),
  ("Credit Card Payment", 10000),
  ("Other Expenses", 60000),
  ("Child(s) Expenses", 0)
]
profession3 = Profession(name3, salary3, savings3, liabilities3, monthExpenses3)

name4, salary4, savings4 = "University Teacher", 450000, 30000
liabilities4 = [
  ("Home Mortgage", 3000000),
  ("Car Loans", 3000000),
  ("Credit Card", 200000)
]
monthExpenses4 = [
  ("Taxes", 35000),
  ("Home Mortgage Payment", 30000),
  ("Car Loans Payment", 35000),
  ("Credit Card Payment", 15000),
  ("Other Expenses", 80000),
  ("Child(s) Expenses", 0)
]
profession4 = Profession(name4, salary4, savings4, liabilities4, monthExpenses4)

name5, salary5, savings5 = "Nurse", 200000, 20000
liabilities5 = [
  ("Home Mortgage", 1500000),
  ("Car Loans", 1000000),
  ("Credit Card", 50000)
]
monthExpenses5 = [
  ("Taxes", 15000),
  ("Home Mortgage Payment", 22000),
  ("Car Loans Payment", 20000),
  ("Credit Card Payment", 3000),
  ("Other Expenses", 40000),
  ("Child(s) Expenses", 0)
]
profession5 = Profession(name5, salary5, savings5, liabilities5, monthExpenses5)

name6, salary6, savings6 = "Medical Doctor", 500000, 40000
liabilities6 = [
  ("Home Mortgage", 3000000),
  ("Car Loans", 3000000),
  ("Credit Card", 200000)
]
monthExpenses6 = [
  ("Taxes", 35000),
  ("Home Mortgage Payment", 50000),
  ("Car Loans Payment", 50000),
  ("Credit Card Payment", 10000),
  ("Other Expenses", 80000),
  ("Child(s) Expenses", 0)
]
profession6 = Profession(name6, salary6, savings6, liabilities6, monthExpenses6)

name7, salary7, savings7 = "Charted Accountant", 500000, 40000
liabilities7 = [
  ("Home Mortgage", 4000000),
  ("Car Loans", 3000000),
  ("Credit Card", 200000)
]
monthExpenses7 = [
  ("Taxes", 35000),
  ("Home Mortgage Payment", 50000),
  ("Car Loans Payment", 50000),
  ("Credit Card Payment", 10000),
  ("Other Expenses", 85000),
  ("Child(s) Expenses", 0)
]
profession7 = Profession(name7, salary7, savings7, liabilities7, monthExpenses7)

name8, salary8, savings8 = "Carpenter", 200000, 25000
liabilities8 = [
  ("Home Mortgage", 1000000),
  ("Car Loans", 0),
  ("Credit Card", 40000)
]
monthExpenses8 = [
  ("Taxes", 35000),
  ("Home Mortgage Payment", 20000),
  ("Car Loans Payment", 0),
  ("Credit Card Payment", 2000),
  ("Other Expenses", 23000),
  ("Child(s) Expenses", 0)
]
profession8 = Profession(name8, salary8, savings8, liabilities8, monthExpenses8)

name9, salary9, savings9 = "Plumber", 100000, 10000
liabilities9 = [
  ("Home Mortgage", 1000000),
  ("Car Loans", 0),
  ("Credit Card", 30000)
]
monthExpenses9 = [
  ("Taxes", 10000),
  ("Home Mortgage Payment", 15000),
  ("Car Loans Payment", 0),
  ("Credit Card Payment", 3000),
  ("Other Expenses", 32000),
  ("Child(s) Expenses", 0)
]
profession9 = Profession(name9, salary9, savings9, liabilities9, monthExpenses9)

name10, salary10, savings10 = "Builder", 150000, 30000
liabilities10 = [
  ("Home Mortgage", 500000),
  ("Car Loans", 0),
  ("Credit Card", 50000)
]
monthExpenses10 = [
  ("Taxes", 15000),
  ("Home Mortgage Payment", 10000),
  ("Car Loans Payment", 0),
  ("Credit Card Payment", 2000),
  ("Other Expenses", 43000),
  ("Child(s) Expenses", 0)
]
profession10 = Profession(name10, salary10, savings10, liabilities10, monthExpenses10)

name11, salary11, savings11 = "Building Architect", 400000, 40000
liabilities11 = [
  ("Home Mortgage", 2000000),
  ("Car Loans", 3000000),
  ("Credit Card", 100000)
]
monthExpenses11 = [
  ("Taxes", 20000),
  ("Home Mortgage Payment", 50000),
  ("Car Loans Payment", 35000),
  ("Credit Card Payment", 10000),
  ("Other Expenses", 55000),
  ("Child(s) Expenses", 0)
]
profession11 = Profession(name11, salary11, savings11, liabilities11, monthExpenses11)

# Ajouter chaque profession créée dans la liste 
list_of_Profession = [profession1, profession2, profession3, profession4, profession5, profession6, profession7, profession8, profession9, profession10, profession11]

# Ne pas toucher !!!!!!!0000
def provide_profession():
  "Fonction that returns a profession"
  return choice(list_of_Profession) 