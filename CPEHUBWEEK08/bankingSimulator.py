# Core Banking System Simulator - Week 08 Project

import json
import os

# ---------- BASE CLASS ----------

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = "Base"

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        # base version, child classes override this with their own rules
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def get_balance(self):
        return self.balance

    def to_dict(self):
        # used when saving to file
        return {
            "account_number": self.account_number,
            "account_holder": self.account_holder,
            "balance": self.balance,
            "account_type": self.account_type
        }


# ---------- CHILD CLASSES ----------

class SavingsAccount(BankAccount):
    MIN_BALANCE = 1000

    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)
        self.account_type = "Savings"

    def withdraw(self, amount):
        # block withdrawal if it drops balance below minimum
        if self.balance - amount < self.MIN_BALANCE:
            print(f"Cannot withdraw. Balance must stay above {self.MIN_BALANCE}.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def add_interest(self, rate):
        interest = self.balance * rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=5000):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
        self.account_type = "Current"

    def withdraw(self, amount):
        # allow going negative up to the overdraft limit
        if self.balance - amount < -self.overdraft_limit:
            print(f"Cannot withdraw. Overdraft limit of {self.overdraft_limit} exceeded.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def to_dict(self):
        # extend the parent's dict to include overdraft_limit
        data = super().to_dict()
        data["overdraft_limit"] = self.overdraft_limit
        return data


# ---------- FILE HANDLING ----------

def save_data(accounts_list, file_format):
    if file_format == "json":
        data = [acc.to_dict() for acc in accounts_list]
        with open("bank_data.json", "w") as f:
            json.dump(data, f, indent=2)
        print("Data saved to bank_data.json")

    elif file_format == "txt":
        with open("bank_data.txt", "w") as f:
            for acc in accounts_list:
                if acc.account_type == "Current":
                    f.write(f"{acc.account_number},{acc.account_holder},{acc.balance},{acc.account_type},{acc.overdraft_limit}\n")
                else:
                    f.write(f"{acc.account_number},{acc.account_holder},{acc.balance},{acc.account_type}\n")
        print("Data saved to bank_data.txt")


def load_data(file_format):
    accounts = []

    if file_format == "json":
        if not os.path.exists("bank_data.json"):
            print("No existing data found. Starting fresh.")
            return accounts

        with open("bank_data.json", "r") as f:
            data = json.load(f)

        for entry in data:
            if entry["account_type"] == "Savings":
                acc = SavingsAccount(entry["account_number"], entry["account_holder"], entry["balance"])
            elif entry["account_type"] == "Current":
                acc = CurrentAccount(entry["account_number"], entry["account_holder"], entry["balance"], entry["overdraft_limit"])
            else:
                continue
            accounts.append(acc)

    elif file_format == "txt":
        if not os.path.exists("bank_data.txt"):
            print("No existing data found. Starting fresh.")
            return accounts

        with open("bank_data.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                acc_number, holder, balance, acc_type = parts[0], parts[1], float(parts[2]), parts[3]

                if acc_type == "Savings":
                    acc = SavingsAccount(acc_number, holder, balance)
                elif acc_type == "Current":
                    overdraft = float(parts[4])
                    acc = CurrentAccount(acc_number, holder, balance, overdraft)
                else:
                    continue
                accounts.append(acc)

    print(f"Loaded {len(accounts)} account(s).")
    return accounts


# ---------- TERMINAL INTERFACE ----------

def find_account(accounts, acc_number):
    for acc in accounts:
        if acc.account_number == acc_number:
            return acc
    return None


def main():
    print("Welcome to the Core Banking System Simulator")
    file_format = input("Choose storage format (json/txt): ").strip().lower()

    while file_format not in ["json", "txt"]:
        file_format = input("Invalid choice. Choose json or txt: ").strip().lower()

    accounts = load_data(file_format)

    while True:
        print("\n--- Main Menu ---")
        print("1. Open New Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit (Saves Data)")

        choice = input("\nChoose an option: ")

        if choice == "1":
            acc_number = input("Enter new account number: ")
            holder = input("Enter account holder name: ")
            acc_type = input("Account type (savings/current): ").strip().lower()

            if acc_type == "savings":
                new_acc = SavingsAccount(acc_number, holder)
            elif acc_type == "current":
                new_acc = CurrentAccount(acc_number, holder)
            else:
                print("Invalid account type.")
                continue

            accounts.append(new_acc)
            print(f"{acc_type.capitalize()} account created for {holder}.")

        elif choice == "2":
            acc_number = input("Enter account number: ")
            acc = find_account(accounts, acc_number)
            if acc:
                amount = float(input("Enter deposit amount: "))
                acc.deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            acc_number = input("Enter account number: ")
            acc = find_account(accounts, acc_number)
            if acc:
                amount = float(input("Enter withdrawal amount: "))
                acc.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            acc_number = input("Enter account number: ")
            acc = find_account(accounts, acc_number)
            if acc:
                print(f"Balance: {acc.get_balance()}")
            else:
                print("Account not found.")

        elif choice == "5":
            save_data(accounts, file_format)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()