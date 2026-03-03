import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"

    def __init__(self):
        self.data = self.load_data()

    # ----------------------------
    # Load & Save Data
    # ----------------------------
    def load_data(self):
        if Path(self.database).exists():
            try:
                with open(self.database, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_data(self):
        with open(self.database, "w") as f:
            json.dump(self.data, f, indent=4)

    # ----------------------------
    # Utility Methods
    # ----------------------------
    def generate_account_number(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def find_user(self, account_no, pin):
        for user in self.data:
            if user["accountNo"] == account_no and user["pin"] == pin:
                return user
        return None

    # ----------------------------
    # Core Features
    # ----------------------------
    def create_account(self, name, age, email, pin):
        if age < 18:
            return False, "Age must be 18+"

        if len(str(pin)) != 4:
            return False, "PIN must be exactly 4 digits"

        account = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": self.generate_account_number(),
            "balance": 0
        }

        self.data.append(account)
        self.save_data()

        return True, account

    def deposit(self, account_no, pin, amount):
        user = self.find_user(account_no, pin)
        if not user:
            return False, "Invalid Account or PIN"

        if amount <= 0:
            return False, "Amount must be greater than 0"

        user["balance"] += amount
        self.save_data()
        return True, user["balance"]

    def withdraw(self, account_no, pin, amount):
        user = self.find_user(account_no, pin)
        if not user:
            return False, "Invalid Account or PIN"

        if amount > user["balance"]:
            return False, "Insufficient Balance"

        user["balance"] -= amount
        self.save_data()
        return True, user["balance"]

    def get_details(self, account_no, pin):
        user = self.find_user(account_no, pin)
        if not user:
            return False, "Invalid Account or PIN"

        return True, user