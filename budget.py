class Category:
  ledger = []
  balance = 30
  def __init__(self,nam):
    self.name = nam
    print(self.name.center(30,'*'))
  def get_balance(self):
    print(self.balance)
    return self.balance
  def check_funds(self, amount):
    if amount > self.balance:
      print('check: False')
      return False
    else:
      print('check: True')
      return True
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.balance += amount
    print(self.ledger)
  def withdraw(self, amount, description=""):
    if self.check_funds(amount) == True:
      self.ledger.append({"amount": -amount, "description": description})
      self.balance -= amount
      print(self.ledger)
      return True
    else:
      print(self.ledger)
      return False
  def transfer(self, amount, category):
    if self.check_funds(amount) == False:
      return False
    else:
      self.withdraw(amount, "Transfer to " + category)
      self.deposit(amount, "Transfer from " + category)
      return True
  print(ledger)


q = Category('Food')

q.get_balance()
q.check_funds(8783)
q.check_funds(10)
q.deposit(450)
q.deposit(550, 'gift')
q.withdraw(10)
q.withdraw(20, 'groceries')

# def create_spend_chart(categories):
# class PartyAnimal:
#     x = 0
#     name = ''
#     def __init__(self, nam):
#         self.name = nam
#         print(self.name,'constructed')
#     def party(self):
#         self.x = self.x + 1
#         print(self.name,'party count',self.x)

# q = PartyAnimal('Quincy')
# m = PartyAnimal('Miya')

# q.party()
# m.party()
# q.party()