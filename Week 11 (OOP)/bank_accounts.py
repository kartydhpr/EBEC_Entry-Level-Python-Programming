################################################################################
# Author: Karteikay Dhuper
# Date: April 25th 2021
# Description  This program emulates a bank acocunt where you can deposit and
# withdraw money from the account and also accrue interest.
################################################################################

class Account: # parent class created

    def __init__ (self, balance): # constructor method
        self.balance = balance

    def deposit(self, amount):
        self.amount = amount # initializes amount attribute in method
        self.balance += self.amount # modifies balance amount
        return f"Deposit: ${self.amount:.2f}"

    def withdraw(self, amount):
        self.amount = amount # initializes amount attribute in method
        self.balance -= self.amount # modifies balance amount
        return f"Withdraw: ${self.amount:.2f}"

    def get_balance(self):

        if self.balance <= 0:
            self.balance += self.amount # if balance is less than 0 after withdrawal then add back the amount withdrawn to the account
            output = "Insufficient funds. Withdrawal canceled." + f"\nBalance: ${self.balance:.2f}" # and inform user that withdrawal was cancelled

        else:
            output = f"Balance: ${self.balance:.2f}" # Otherwise if bank balance is more than 0 then just print the balance
        return output

class Savings(Account): # child class created that inherits from parent

    statement = "New account balance: $200.00"

    def __init__ (self, balance, interest_rate):
        self.interest_rate = interest_rate
        Account.__init__(self,balance)

    #statement = f"New account balance: ${balance:.2f}"


    def accrue_interest(self):
        interestPayment = (self.balance * self.interest_rate)
        self.balance += interestPayment # adds the interest payment to the bank account
        return f"Interest payment: ${interestPayment:.2f}"

def main():

    obj1 = Savings(200,0.10) # creates instance "obj1" of savings class

    # manipulation of savings instance with various methods
    print(obj1.statement)
    print(obj1.get_balance())
    print(obj1.deposit(12.34))
    print(obj1.get_balance())
    print(obj1.withdraw(40))
    print(obj1.get_balance())
    print(obj1.withdraw(200))
    print(obj1.get_balance())
    print(obj1.accrue_interest())
    print(obj1.accrue_interest())
    print(obj1.accrue_interest())
    print(obj1.withdraw(200))
    print(obj1.get_balance())

if __name__ == '__main__':
    main()
