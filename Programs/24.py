"""

Task 24 Bank Account Class:- Create a BankAccount class with a constructor and methods for deposit, withdrawal and balance
checking. Prevent invalid transactions and insufficient-balance withdrawals

"""

try:
    class Bankacc:
        def __init__(self,name,accno,balance):
            self.name = name
            self.accno = accno
            self.balance = balance
            
        def deposit(self,dep):
            if dep <= 0:
                print("Invalid Deposit Amount!!")
            else:
                self.balance += dep
                print(f"Successfully Deposited {dep}")
                print(f"Updated Balance:-",self.balance)
        
        def withdrawal(self,wit):
            if wit <= 0:
                print("Invalid Withdrawal Amount!!")
            elif self.balance < wit:
                print("Insufficient Balance!!")
            else:
                self.balance -= wit  
                print(f"Successfully Withdrawn {wit}")
                print(f"Updated Balance:-",self.balance)
        
        def checkbal(self):
            print(f"Name:-",self.name)
            print(f"Account No.:-",self.accno)
            print(f"Current Balance:-",self.balance)
            
    b1 = Bankacc("Raj",12345678,3000)
    b1.checkbal()
    b1.deposit(4000)     
    b1.withdrawal(7000)  

except Exception as e:
    print("Error", e)