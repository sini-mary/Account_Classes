class Account:
    bankAcc="Equity"
    def __init__(self,balance,accNumber,userName, withdrawals) :
        self.balance=balance
        self.accNumber=accNumber
        self.userName=userName
        self.deposits=[]
        self.withdrawls=withdrawals
        self.loanBalance=0   
    def checkbalance(self):
        return f"{self.balance}"
    
    def deposit(self,amount):
        transaction={
        "amount":amount,
        "narration":"deposit"
        }
        self.deposits.append(transaction)
        print(transaction)
    def transactions(self):
        for transaction in self.deposits:
            print(transaction)
    
   
bank=Account(1234,"sini",22,11)
ban=Account(1234,"sini",22,11)

bank.deposit(19)
ban.deposit(1)

bank.transactions
# Add a new method  print_statement which combines both deposits and withdrawals into one list and,
# using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500
def print_statement(self):
        combined_list=self.deposits+self.withdrawals
        print(combined_list)
        for c in combined_list:
            print(f"{c['narration']} - {c['amount']}")
# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount
def borrow_loan(self,loan_amount):
        total_deposits = sum(transaction["amount"] for transaction in self.deposits)
        if self.loan_balance==0 and loan_amount>100 and len(self.deposits)>=10 and loan_amount > total_deposits / 3:
           return
        self.loan_balance+=loan_amount
        self.balance+=loan_amount
# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance
def repay_loan(self,amount):
        self.loan_balance-=amount
        if amount>self.loan_balance:
            extra=self.loan_balance-amount
            self.balance+=extra
# Add a transfer method which accepts two attributes (amount and instance of another account).
# If the amount is less than the current instances balance, the method transfers the requested amount from the
# current account to the passed account. The transfer is accomplished by reducing the current account balance
# and depositing the requested amount to the passed account.
def transfer(self,amount,other_account):
        other_account=Account
        if self.balance> amount:
            return
        self.balance -= amount
        other_account.check_deposit(self,amount)
        
        