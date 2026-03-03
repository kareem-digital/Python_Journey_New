"""
Enhanced Bank Management System
Core business logic with improved security and error handling
"""

import json
import random
import string
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List


class Bank:
    """Bank management system with secure account operations"""
    
    database = 'data.json'
    data = []
    
    @classmethod
    def load_data(cls) -> bool:
        """Load data from JSON file with error handling"""
        try:
            if Path(cls.database).exists():
                with open(cls.database, 'r') as fs:
                    content = fs.read()
                    if content.strip():
                        cls.data = json.loads(content)
                        return True
                    else:
                        cls.data = []
                        return True
            else:
                cls.data = []
                with open(cls.database, 'w') as fs:
                    fs.write('[]')
                return True
        except json.JSONDecodeError as err:
            print(f"Error reading database (corrupted JSON): {err}")
            cls.data = []
            return False
        except Exception as err:
            print(f"An exception occurred: {err}")
            cls.data = []
            return False
    
    @classmethod
    def save_data(cls) -> bool:
        """Save data to JSON file"""
        try:
            with open(cls.database, 'w') as fs:
                json.dump(cls.data, fs, indent=4)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    
    @staticmethod
    def hash_pin(pin: int) -> str:
        """Hash PIN for security"""
        return hashlib.sha256(str(pin).encode()).hexdigest()
    
    @staticmethod
    def generate_account_number() -> str:
        """Generate unique account number"""
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spclchar = random.choices("!@#$%^&*", k=1)
        id_parts = alpha + num + spclchar
        random.shuffle(id_parts)
        return "".join(id_parts)
    
    @classmethod
    def validate_pin(cls, pin: int) -> tuple[bool, str]:
        """Validate PIN format"""
        if not isinstance(pin, int):
            return False, "PIN must be a number"
        if len(str(pin)) != 4:
            return False, "PIN must be exactly 4 digits"
        return True, "Valid PIN"
    
    @classmethod
    def create_account(cls, name: str, age: int, email: str, pin: int) -> tuple[bool, str, Optional[Dict]]:
        """
        Create a new bank account
        Returns: (success, message, account_info)
        """
        # Validate inputs
        if not name or not name.strip():
            return False, "Name cannot be empty", None
        
        if age < 18:
            return False, "You must be 18 or older to create an account", None
        
        if not email or '@' not in email:
            return False, "Please provide a valid email address", None
        
        is_valid, msg = cls.validate_pin(pin)
        if not is_valid:
            return False, msg, None
        
        # Check if email already exists
        if any(acc['email'] == email for acc in cls.data):
            return False, "An account with this email already exists", None
        
        # Create account
        account_info = {
            "name": name.strip(),
            "age": age,
            "email": email.strip().lower(),
            "pin": cls.hash_pin(pin),  # Store hashed PIN
            "accountNo": cls.generate_account_number(),
            "balance": 0,
            "created_at": datetime.now().isoformat(),
            "transactions": []
        }
        
        cls.data.append(account_info)
        cls.save_data()
        
        return True, "Account created successfully!", account_info
    
    @classmethod
    def authenticate(cls, account_no: str, pin: int) -> Optional[Dict]:
        """Authenticate user and return account data"""
        hashed_pin = cls.hash_pin(pin)
        for account in cls.data:
            if account['accountNo'] == account_no and account['pin'] == hashed_pin:
                return account
        return None
    
    @classmethod
    def deposit_money(cls, account_no: str, pin: int, amount: float) -> tuple[bool, str]:
        """Deposit money into account"""
        account = cls.authenticate(account_no, pin)
        
        if not account:
            return False, "Invalid account number or PIN"
        
        if amount <= 0:
            return False, "Amount must be greater than 0"
        
        if amount > 10000:
            return False, "Maximum deposit amount is ₹10,000 per transaction"
        
        # Update balance
        account['balance'] += amount
        
        # Add transaction record
        transaction = {
            "type": "deposit",
            "amount": amount,
            "timestamp": datetime.now().isoformat(),
            "balance_after": account['balance']
        }
        
        if 'transactions' not in account:
            account['transactions'] = []
        account['transactions'].append(transaction)
        
        cls.save_data()
        return True, f"₹{amount:,.2f} deposited successfully! New balance: ₹{account['balance']:,.2f}"
    
    @classmethod
    def withdraw_money(cls, account_no: str, pin: int, amount: float) -> tuple[bool, str]:
        """Withdraw money from account"""
        account = cls.authenticate(account_no, pin)
        
        if not account:
            return False, "Invalid account number or PIN"
        
        if amount <= 0:
            return False, "Amount must be greater than 0"
        
        if amount > account['balance']:
            return False, f"Insufficient balance. Available: ₹{account['balance']:,.2f}"
        
        # Update balance
        account['balance'] -= amount
        
        # Add transaction record
        transaction = {
            "type": "withdrawal",
            "amount": amount,
            "timestamp": datetime.now().isoformat(),
            "balance_after": account['balance']
        }
        
        if 'transactions' not in account:
            account['transactions'] = []
        account['transactions'].append(transaction)
        
        cls.save_data()
        return True, f"₹{amount:,.2f} withdrawn successfully! New balance: ₹{account['balance']:,.2f}"
    
    @classmethod
    def get_account_details(cls, account_no: str, pin: int) -> tuple[bool, Optional[Dict], str]:
        """Get account details"""
        account = cls.authenticate(account_no, pin)
        
        if not account:
            return False, None, "Invalid account number or PIN"
        
        # Return copy without PIN
        account_copy = account.copy()
        account_copy.pop('pin', None)
        
        return True, account_copy, "Account details retrieved successfully"
    
    @classmethod
    def update_account(cls, account_no: str, pin: int, name: str = None, 
                      email: str = None, new_pin: int = None) -> tuple[bool, str]:
        """Update account details"""
        account = cls.authenticate(account_no, pin)
        
        if not account:
            return False, "Invalid account number or PIN"
        
        # Update fields if provided
        if name and name.strip():
            account['name'] = name.strip()
        
        if email and email.strip():
            # Check if email already exists for another account
            if any(acc['email'] == email.lower() and acc['accountNo'] != account_no 
                   for acc in cls.data):
                return False, "Email already in use by another account"
            account['email'] = email.strip().lower()
        
        if new_pin:
            is_valid, msg = cls.validate_pin(new_pin)
            if not is_valid:
                return False, msg
            account['pin'] = cls.hash_pin(new_pin)
        
        cls.save_data()
        return True, "Account details updated successfully!"
    
    @classmethod
    def delete_account(cls, account_no: str, pin: int) -> tuple[bool, str]:
        """Delete account"""
        account = cls.authenticate(account_no, pin)
        
        if not account:
            return False, "Invalid account number or PIN"
        
        # Find and remove account
        cls.data = [acc for acc in cls.data if acc['accountNo'] != account_no]
        cls.save_data()
        
        return True, "Account deleted successfully!"
    
    @classmethod
    def get_transaction_history(cls, account_no: str, pin: int, limit: int = 10) -> tuple[bool, List, str]:
        """Get recent transaction history"""
        account = cls.authenticate(account_no, pin)
        
        if not account:
            return False, [], "Invalid account number or PIN"
        
        transactions = account.get('transactions', [])
        recent_transactions = transactions[-limit:] if transactions else []
        recent_transactions.reverse()  # Most recent first
        
        return True, recent_transactions, "Transaction history retrieved"
    
    @classmethod
    def get_total_accounts(cls) -> int:
        """Get total number of accounts"""
        return len(cls.data)
    
    @classmethod
    def get_total_balance(cls) -> float:
        """Get total balance across all accounts"""
        return sum(acc.get('balance', 0) for acc in cls.data)