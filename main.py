class Customer(object):

  def __init__(self, customer_id, name):
    self.customer_id = customer_id
    self.name = name
    self.accounts = {}

  def addAccount(self, account, account_type):
    self.accounts[account.account_number] = account_type
    return self.accounts

class Account(object):

  def __init__(self, account_number, initial_balance = 0):
    self.account_number = account_number
    self.balance = initial_balance

  def deposit(self, amount):
    self.balance += amount

    return 'Your balance is {}'.format(self.balance)

  def getfunds(self):
    return self.balance

  def withdraw(self, amount):

    if amount > self.balance:
      return 'You do not have enough funds'

    self.balance = self.balance - amount
    return self.balance

  def __str__(self):
    return 'The funds for this account are {}'.format(self.getfunds())

class Bank(object):

  def __init__(self):
    self.customers = {}

  def addCustomer(self, bank_customer):
    self.customers[bank_customer.customer_id] = bank_customer  