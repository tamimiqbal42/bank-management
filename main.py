
class Banking:
    def __init__(self, holder_name, initial_balance):
        self.holder_name = holder_name
        self.balance = initial_balance
        
    def deposit(self):
        amount = float(input("Enter your Deposit Amount: "))
        if amount > 100:
            self.balance += amount
            print(f"Deposit successful! {amount} added to your account.")
        else:
            print("Deposit amount must be greater than 100.")              
            
    def get_balance(self):
        return self.balance
        
    def withdraw(self):
        amount = float(input("Enter your Withdrawal Amount: "))
        if amount > self.balance:
            print("Insufficient balance! Withdrawal failed.")
        elif amount > 100:
            self.balance -= amount
            print(f"Withdrawal successful! {amount} deducted from your account.")
        else:
            print("Withdrawal amount must be greater than 100.")
        
        
transaction = Banking("Tamim Iqbal", 50000)
print(f"Account Name: {transaction.holder_name}")
print(f"Initial Balance: {transaction.balance}")

transaction.deposit()
print(f"After deposit, your balance is: {transaction.balance}")

transaction.withdraw()
print(f"After withdrawal, your balance is: {transaction.balance}")

