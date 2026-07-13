class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
    
    def display_individual_balace(self):
        print(f"{self.name}'s balance: ${self.balance}")
    
    @classmethod
    def display_accounts(cls):
        print(f"Total Accounts: {cls.total_accounts}")
        print(f"Total Balance: ${cls.total_balance}")


# TODO: Create two accounts
# TODO: Print the information using the mentioned format

alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 2000)

alice_account.display_individual_balace()
bob_account.display_individual_balace()
BankAccount.display_accounts()