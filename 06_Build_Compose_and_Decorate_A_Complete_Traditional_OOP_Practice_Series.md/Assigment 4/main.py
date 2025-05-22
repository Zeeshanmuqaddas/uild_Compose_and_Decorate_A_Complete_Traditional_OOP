class Bank:
    # Class variable
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")


# Create instances
account1 = Bank("Alice")
account2 = Bank("Bob")

# Display initial info
print("Before changing bank name:")
account1.display_info()
account2.display_info()

# Change the bank name using class method
Bank.change_bank_name("Future Bank")

# Display info after change
print("\nAfter changing bank name:")
account1.display_info()
account2.display_info()
