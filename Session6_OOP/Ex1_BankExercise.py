# Create a Bank, an Account, and a Customer class.
    # All classes should be in a single file.
    # The bank class should be able to hold many account.
    # You should be able to add new accounts.
    # The Account class should have relevant details.
    # The Customer class Should also have relevant details.
# Stick to the techniques we have covered so far.

# Add the abillity for your __init__ method to handle different inputs (parameters).
 
class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)


class Account(Bank, Customer):
    def __init__(self, first_name, last_name, bank_name, account_number, reg_number):
        Bank.__init__(self, bank_name)
        Customer.__init__(self, first_name, last_name)
        self.account_number = account_number
        self.reg_number = reg_number
        
b1 = Bank('Dansk Bank') 

c1 = Customer('Christina', 'Bartholomæussen')
c2 = Customer('Frederik', 'Petersen')

b1.add_customer(c1)
b1.add_customer(c2)


c1.add_account(Account(c1.first_name, c1.last_name, b1.bank_name, '123456789', '1234'))
c1.add_account(Account(c1.first_name, c1.last_name, b1.bank_name, '456789123', '4877'))
c2.add_account(Account(c2.first_name, c2.last_name, b1.bank_name, '987654321', '1598'))

for c in b1.customers:
    print(f'{c.first_name} {c.last_name}')


for c in b1.customers:
    for a in c.accounts:
        print(f'{c.first_name} {c.last_name} {a.account_number} {a.reg_number}')
