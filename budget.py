class Category:
  ledger = []
  balance = 30
  def __init__(self,nam):
    self.name = nam
    print(self.name.center(30,'*'))
  def get_balance(self):
    print(self.balance)
    # return balance
  def check_funds(self, amount):
    if amount > self.balance:
      print('check: False')
      return False
    else:
      print('check: True')
      return True
  def deposit(amount,description):
    ledger.append(amount)
    ledger.append(description)
  def withdraw(amount,description):
    if funds > amount:
      ledger.append('-', amount)
      ledger.append(description)
      return True
    else:
      ledger.append(description)
      return False
  print(ledger)
  # def transfer(amount, category):

q = Category('Food')

q.get_balance()
q.check_funds(8783)
q.check_funds(10)

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