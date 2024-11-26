class Account:
    def __init__(self, account_number, account_name, initial_balance):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f} into account {self.account_number}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}")

    def check_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance:.2f}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_name, initial_balance):
        if account_number in self.accounts:
            print("Account number already exists")
        else:
            new_account = Account(
                account_number, account_name, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account {account_number} created successfully")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def list_accounts(self):
        print("List of accounts:")
        for account_number, account in self.accounts.items():
            print(f"Account Number: {account_number}, Account Name: {
                  account.account_name}")


def main():
    bank = Bank()

    while True:
        print("Banking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. List Accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_name = input("Enter account name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, account_name, initial_balance)
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(account_number)
            if account:
                account.deposit(amount)
            else:
                print("Account not found")
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found")
        elif choice == "4":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                account.check_balance()
            else:
                print("Account not found")
        elif choice == "5":
            bank.list_accounts()
        elif choice == "6":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
