import budget
import re
class Category:
  def __init__(self,nam):
    self.name = nam
    self.ledger = []
    self.balance = 0

  def get_balance(self):
    return self.balance

  def check_funds(self, amount):
    return True if amount <= self.balance else False

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount

  def withdraw(self, amount, description=""):
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": -amount, "description": description})
      self.balance -= amount
      return True
    else:
      return False
  
  def transfer(self, amount, category):
    if self.check_funds(amount) == True:
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False
  
  def __str__(self):
    string = ""
    string += self.name.center(30,'*') + '\n'
    for transaction in self.ledger:
        string += transaction["description"][:23]
        string += str(format(float(transaction["amount"]), '.2f')).rjust(30 - len(transaction["description"][:23]))
        string += '\n'
    string += "Total: " + str(format(float(self.balance), '.2f'))
    return string

  def print_ledger(self):
    print(self.name)
    print(self.ledger)

def create_spend_chart(categories):
  name_cat = []
  spending_all = []
  spending_by_cat = []
  perc_lst = []
  for category in categories:
    spending_all.append(re.findall(r'-\d*\.?\d+', str(category)))
    name_cat.append(re.findall('[A-Z][a-z]+', str(category)[:30]))
  # print(spending_all)
  # print(name_cat)
  for lst in spending_all:
    spending = 0
    for str_nb in lst:
      spending += float(str_nb)
    spending_by_cat.append(spending)
  # print(spending_by_cat)
  total_spending = sum(spending_by_cat)
  # print(total_spending)
  for spending in spending_by_cat:
    perc_lst.append(round(spending / total_spending * 10))
  # print(perc_lst)
  bar_chart = ""
  bar_chart += "Percentage spent by category\n"
  perc = 100
  while perc != 0:
    bar_chart += str(perc).rjust(3) + "|".ljust(len(name_cat) * 4 - 1) + 'END' + '\n'
    perc -= 10
  bar_chart += ' ' * 4 + '-' * (len(name_cat) * 3 + 1)
  for name in name_cat:
    for char in name:
      bar_chart += 
  # print("100|          " + "ENDhkjh")
  return bar_chart

# Percentage spent by category
# 100|          
#  90|          
#  80|          
#  70|          
#  60| o        
#  50| o        
#  40| o        
#  30| o        
#  20| o  o     
#  10| o  o  o  
#   0| o  o  o  
#     ----------
#      F  C  A  
#      o  l  u  
#      o  o  t  
#      d  t  o  
#         h     
#         i     
#         n     
#         g

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))
