class Category:
  ledger = []
  balance = 30
  def __init__(self,nam):
    self.name = nam
    print(self.name.center(30,'*'))
  def get_balance(balance):
    print(balance)
    # return balance
  def check_funds(amount):
    if amount > balance:
      return False
    else:
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