NUMBER_OF_ACCOUNTS = 0

class BankAccount:
    def __init__(self,client_name,phone_number,balance=0):
        self.name = client_name
        self.account_number = self.assign_account_number()
        self.phone_number = phone_number
        self.balance = balance

    def assign_account_number(self):
        global NUMBER_OF_ACCOUNTS
        NUMBER_OF_ACCOUNTS += 1
        return NUMBER_OF_ACCOUNTS

    def deposit(self, amount):
        self.balance += amount
        print('Thanks {}! Your balance is now ${}.'.format(self.name, self.balance))

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print('Thanks, {}! Your balance is now ${}.'.format(self.name, self.balance))
        else:
            print('Sorry, you can\'t withdraw that much.')

class BankAccountPlus(BankAccount):
    def __init__(self, client_name, phone_number):
        super().__init__(client_name, phone_number)

    def withdraw(self, amount):
        if self.balance - amount >= 100:
            self.balance -= amount
            print('Thanks {}! Your balance is now ${}.'.format(self.name, self.balance))
        elif 100 > self.balance - amount >= 0:
            print('Sorry, {}, that would put your balance under $100.'.format(self.name))
        else:
            print('Sorry, {}, you don\'t have enough money for that.'.format(self.name))

li_account = BankAccount('Li', '5035609924')
maggie_account = BankAccountPlus('Maggie', '5555555555')

maggie_account.deposit(150)
maggie_account.withdraw(30)
maggie_account.withdraw(60)
maggie_account.withdraw(300)
