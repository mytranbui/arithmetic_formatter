import budget
class Category:
  def __init__(self,nam):
    self.name = nam
    self.ledger = []
    self.balance = 0
  def get_balance(self):
    return self.balance
  def check_funds(self, amount):
    # return True if amount <= self.balance else False
    if amount > self.balance:
      return False
    else:
      return True
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
    if self.check_funds(amount) == False:
      return False
    else:
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
  def __str__(self):
    string = ""
    string += self.name.center(30,'*') + '\n'
    for transaction in self.ledger:
        string += transaction["description"][:23] + str(format(float(transaction["amount"]), '.2f')).rjust(30 - len(transaction["description"][:23])) + '\n'
    string += "Total: " + str(format(float(self.balance), '.2f'))
    return string
  def print_ledger(self):
    print("print:\n")
    print(self.name)
    print(self.ledger)

def create_spend_chart(categories):
  print('lol')

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
