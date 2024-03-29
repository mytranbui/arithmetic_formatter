from nis import cat
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

  # def print_ledger(self):
  #   print(self.name)
  #   print(self.ledger)

def longest_len_str(lst):
  longest = ""
  for str in lst:
    if len(str) > len(longest):
      longest = str
  return len(longest)

def create_spend_chart(categories):
  name_cat = []
  spending_all = []
  spending_by_cat = []
  perc_lst = []
  # print(str(categories))
  for category in categories:
    spending_all.append(re.findall(r'-\d*\.?\d+', str(category)))
    name_cat.append(re.findall('\*([A-Z][a-z]+)', str(category)[:30]))
  # name_cat.append(re.findall('[A-Z][a-z]+', str(categories[0-3])))
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
    perc_lst.append((spending / total_spending) * 100)
  # print(perc_lst)
  bar_chart = ""
  bar_chart += "Percentage spent by category\n"
  lst = []
  i = 0
  while i < len(name_cat):
    lst.append(name_cat[i][0])
    i += 1
  perc = 100
  while perc != -10:
    bar_chart += str(perc).rjust(3) + "| "
    for perc_cat in perc_lst:
      if perc_cat >= perc:
        bar_chart += "o".ljust(3)
      else:
        bar_chart += '   '
    bar_chart += '\n'
    perc -= 10
  bar_chart += ' ' * 4 + '-' * (len(lst) * 3 + 1) + '\n'
  longest_cat = longest_len_str(lst)
  vertical_cat = ""
  for i in range(longest_cat):
    vertical_cat += "    "
    for name in lst :
      try :
        vertical_cat += name[i].center(3)
      except IndexError:
        vertical_cat += "   "
    vertical_cat += " "
    if i != longest_cat -1 :
      vertical_cat += "\n"
  bar_chart += vertical_cat
  return bar_chart

# food = budget.Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# # print(food.get_balance())
# clothing = budget.Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = budget.Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(food)
# print(clothing)
# print(auto)
# print(create_spend_chart([food, clothing, auto]))

# business = budget.Category("Business")
# food = budget.Category("Food")
# entertainment = budget.Category("Entertainment")
# food.deposit(900, "deposit")
# entertainment.deposit(900, "deposit")
# business.deposit(900, "deposit")
# food.withdraw(105.55)
# entertainment.withdraw(33.40)
# business.withdraw(10.99)
# print(business)
# print(food)
# print(entertainment)
# print(create_spend_chart([business, food, entertainment]))