"""
Bank Management System - Command Line Interface
Enhanced CLI with better user experience
"""

from bank_manager import Bank
from datetime import datetime
import os
import sys


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header(title):
    """Print formatted header"""
    print("\n" + "=" * 60)
    print(f"  {title}".center(60))
    print("=" * 60 + "\n")


def print_success(message):
    """Print success message"""
    print(f"\n✅ {message}\n")


def print_error(message):
    """Print error message"""
    print(f"\n❌ {message}\n")


def print_info(message):
    """Print info message"""
    print(f"\nℹ️  {message}\n")


def press_enter_to_continue():
    """Wait for user to press enter"""
    input("\nPress Enter to continue...")


def main_menu():
    """Display main menu"""
    clear_screen()
    print_header("🏦 BANK MANAGEMENT SYSTEM")
    
    print("📊 System Statistics:")
    print(f"   Total Accounts: {Bank.get_total_accounts()}")
    print(f"   Total Balance: ₹{Bank.get_total_balance():,.2f}\n")
    
    print("━" * 60)
    print("1️⃣  Create New Account")
    print("2️⃣  Deposit Money")
    print("3️⃣  Withdraw Money")
    print("4️⃣  View Account Details")
    print("5️⃣  Transaction History")
    print("6️⃣  Update Profile")
    print("7️⃣  Delete Account")
    print("0️⃣  Exit")
    print("━" * 60)


def create_account():
    """Create new account flow"""
    clear_screen()
    print_header("📝 CREATE NEW ACCOUNT")
    
    print("Please provide the following details:\n")
    
    try:
        name = input("Full Name: ").strip()
        if not name:
            print_error("Name cannot be empty!")
            press_enter_to_continue()
            return
        
        age = int(input("Age: "))
        
        email = input("Email: ").strip()
        if not email or '@' not in email:
            print_error("Please provide a valid email!")
            press_enter_to_continue()
            return
        
        pin = input("Create 4-digit PIN: ").strip()
        if len(pin) != 4 or not pin.isdigit():
            print_error("PIN must be exactly 4 digits!")
            press_enter_to_continue()
            return
        
        confirm_pin = input("Confirm PIN: ").strip()
        if pin != confirm_pin:
            print_error("PINs do not match!")
            press_enter_to_continue()
            return
        
        # Create account
        success, message, account_info = Bank.create_account(name, age, email, int(pin))
        
        if success:
            print_success(message)
            print("🎉 Account Details:")
            print("━" * 60)
            print(f"   Account Number: {account_info['accountNo']}")
            print(f"   Name: {account_info['name']}")
            print(f"   Email: {account_info['email']}")
            print(f"   Balance: ₹{account_info['balance']:.2f}")
            print("━" * 60)
            print("\n⚠️  IMPORTANT: Please save your account number safely!")
        else:
            print_error(message)
        
        press_enter_to_continue()
        
    except ValueError:
        print_error("Invalid input! Please enter correct data types.")
        press_enter_to_continue()
    except KeyboardInterrupt:
        print("\n\n🚫 Operation cancelled.")
        press_enter_to_continue()


def get_credentials():
    """Get and validate account credentials"""
    try:
        account_no = input("Account Number: ").strip()
        pin = input("PIN: ").strip()
        
        if not account_no or not pin:
            print_error("Account number and PIN are required!")
            return None, None
        
        if len(pin) != 4 or not pin.isdigit():
            print_error("PIN must be exactly 4 digits!")
            return None, None
        
        return account_no, int(pin)
    
    except ValueError:
        print_error("Invalid PIN format!")
        return None, None
    except KeyboardInterrupt:
        print("\n\n🚫 Operation cancelled.")
        return None, None


def deposit_money():
    """Deposit money flow"""
    clear_screen()
    print_header("💳 DEPOSIT MONEY")
    
    account_no, pin = get_credentials()
    if not account_no or not pin:
        press_enter_to_continue()
        return
    
    # First authenticate to show balance
    account = Bank.authenticate(account_no, pin)
    if not account:
        print_error("Invalid account number or PIN!")
        press_enter_to_continue()
        return
    
    print(f"\n💰 Current Balance: ₹{account['balance']:,.2f}")
    print_info("Maximum deposit per transaction: ₹10,000")
    
    try:
        amount = float(input("\nAmount to deposit: ₹"))
        
        if amount <= 0:
            print_error("Amount must be greater than 0!")
            press_enter_to_continue()
            return
        
        success, message = Bank.deposit_money(account_no, pin, amount)
        
        if success:
            print_success(message)
        else:
            print_error(message)
        
        press_enter_to_continue()
        
    except ValueError:
        print_error("Invalid amount! Please enter a valid number.")
        press_enter_to_continue()
    except KeyboardInterrupt:
        print("\n\n🚫 Operation cancelled.")
        press_enter_to_continue()


def withdraw_money():
    """Withdraw money flow"""
    clear_screen()
    print_header("💸 WITHDRAW MONEY")
    
    account_no, pin = get_credentials()
    if not account_no or not pin:
        press_enter_to_continue()
        return
    
    # First authenticate to show balance
    account = Bank.authenticate(account_no, pin)
    if not account:
        print_error("Invalid account number or PIN!")
        press_enter_to_continue()
        return
    
    print(f"\n💰 Available Balance: ₹{account['balance']:,.2f}")
    
    try:
        amount = float(input("\nAmount to withdraw: ₹"))
        
        if amount <= 0:
            print_error("Amount must be greater than 0!")
            press_enter_to_continue()
            return
        
        success, message = Bank.withdraw_money(account_no, pin, amount)
        
        if success:
            print_success(message)
        else:
            print_error(message)
        
        press_enter_to_continue()
        
    except ValueError:
        print_error("Invalid amount! Please enter a valid number.")
        press_enter_to_continue()
    except KeyboardInterrupt:
        print("\n\n🚫 Operation cancelled.")
        press_enter_to_continue()


def view_account_details():
    """View account details flow"""
    clear_screen()
    print_header("👤 ACCOUNT DETAILS")
    
    account_no, pin = get_credentials()
    if not account_no or not pin:
        press_enter_to_continue()
        return
    
    success, account, message = Bank.get_account_details(account_no, pin)
    
    if not success:
        print_error(message)
        press_enter_to_continue()
        return
    
    print("\n📋 Personal Information")
    print("━" * 60)
    print(f"   Name: {account['name']}")
    print(f"   Age: {account['age']}")
    print(f"   Email: {account['email']}")
    
    print("\n🏦 Banking Information")
    print("━" * 60)
    print(f"   Account Number: {account['accountNo']}")
    print(f"   Balance: ₹{account['balance']:,.2f}")
    
    created = datetime.fromisoformat(account['created_at']).strftime('%d %B %Y, %I:%M %p')
    print(f"   Member Since: {created}")
    
    transactions = account.get('transactions', [])
    print(f"   Total Transactions: {len(transactions)}")
    print("━" * 60)
    
    press_enter_to_continue()


def view_transaction_history():
    """View transaction history flow"""
    clear_screen()
    print_header("📜 TRANSACTION HISTORY")
    
    account_no, pin = get_credentials()
    if not account_no or not pin:
        press_enter_to_continue()
        return
    
    success, transactions, message = Bank.get_transaction_history(account_no, pin, limit=50)
    
    if not success:
        print_error(message)
        press_enter_to_continue()
        return
    
    if not transactions:
        print_info("No transactions yet. Start by depositing money!")
        press_enter_to_continue()
        return
    
    print(f"\n📊 Showing last {len(transactions)} transactions:\n")
    print("━" * 80)
    print(f"{'Date & Time':<25} {'Type':<12} {'Amount':<15} {'Balance After':<15}")
    print("━" * 80)
    
    for trans in transactions:
        date_time = datetime.fromisoformat(trans['timestamp']).strftime('%d %b %Y, %I:%M %p')
        trans_type = trans['type'].title()
        amount = f"₹{trans['amount']:,.2f}"
        balance = f"₹{trans['balance_after']:,.2f}"
        
        print(f"{date_time:<25} {trans_type:<12} {amount:<15} {balance:<15}")
    
    print("━" * 80)
    
    # Summary statistics
    deposits = [t for t in transactions if t['type'] == 'deposit']
    withdrawals = [t for t in transactions if t['type'] == 'withdrawal']
    
    print("\n📈 Summary:")
    print(f"   Total Deposits: ₹{sum(t['amount'] for t in deposits):,.2f} ({len(deposits)} transactions)")
    print(f"   Total Withdrawals: ₹{sum(t['amount'] for t in withdrawals):,.2f} ({len(withdrawals)} transactions)")
    print(f"   Net Change: ₹{sum(t['amount'] for t in deposits) - sum(t['amount'] for t in withdrawals):,.2f}")
    
    press_enter_to_continue()


def update_profile():
    """Update profile flow"""
    clear_screen()
    print_header("✏️ UPDATE PROFILE")
    
    account_no, pin = get_credentials()
    if not account_no or not pin:
        press_enter_to_continue()
        return
    
    # Verify credentials first
    account = Bank.authenticate(account_no, pin)
    if not account:
        print_error("Invalid account number or PIN!")
        press_enter_to_continue()
        return
    
    print("\nℹ️  Leave fields empty to keep current values\n")
    print(f"Current Name: {account['name']}")
    print(f"Current Email: {account['email']}")
    print()
    
    try:
        new_name = input("New Name (press Enter to skip): ").strip()
        new_email = input("New Email (press Enter to skip): ").strip()
        new_pin = input("New 4-digit PIN (press Enter to skip): ").strip()
        
        # Validate new PIN if provided
        if new_pin:
            if len(new_pin) != 4 or not new_pin.isdigit():
                print_error("PIN must be exactly 4 digits!")
                press_enter_to_continue()
                return
            
            confirm_pin = input("Confirm New PIN: ").strip()
            if new_pin != confirm_pin:
                print_error("PINs do not match!")
                press_enter_to_continue()
                return
            
            new_pin = int(new_pin)
        else:
            new_pin = None
        
        # Update account
        success, message = Bank.update_account(
            account_no,
            pin,
            name=new_name if new_name else None,
            email=new_email if new_email else None,
            new_pin=new_pin
        )
        
        if success:
            print_success(message)
            if new_pin:
                print_info("🔐 Your PIN has been updated. Please remember your new PIN!")
        else:
            print_error(message)
        
        press_enter_to_continue()
        
    except KeyboardInterrupt:
        print("\n\n🚫 Operation cancelled.")
        press_enter_to_continue()


def delete_account():
    """Delete account flow"""
    clear_screen()
    print_header("🗑️ DELETE ACCOUNT")
    
    print("⚠️  WARNING: This action cannot be undone!\n")
    
    account_no, pin = get_credentials()
    if not account_no or not pin:
        press_enter_to_continue()
        return
    
    # Verify credentials first
    account = Bank.authenticate(account_no, pin)
    if not account:
        print_error("Invalid account number or PIN!")
        press_enter_to_continue()
        return
    
    print(f"\n📋 Account to be deleted:")
    print(f"   Name: {account['name']}")
    print(f"   Account Number: {account['accountNo']}")
    print(f"   Balance: ₹{account['balance']:,.2f}")
    
    print("\n" + "━" * 60)
    confirmation = input("\nType 'DELETE' in capital letters to confirm: ").strip()
    
    if confirmation == "DELETE":
        success, message = Bank.delete_account(account_no, pin)
        
        if success:
            print_success(message)
            print_info("Your account has been permanently deleted.")
        else:
            print_error(message)
    else:
        print_info("Account deletion cancelled.")
    
    press_enter_to_continue()


def main():
    """Main program loop"""
    # Load data on startup
    Bank.load_data()
    
    while True:
        try:
            main_menu()
            
            choice = input("\nEnter your choice (0-7): ").strip()
            
            if choice == '1':
                create_account()
            elif choice == '2':
                deposit_money()
            elif choice == '3':
                withdraw_money()
            elif choice == '4':
                view_account_details()
            elif choice == '5':
                view_transaction_history()
            elif choice == '6':
                update_profile()
            elif choice == '7':
                delete_account()
            elif choice == '0':
                clear_screen()
                print("\n" + "=" * 60)
                print("  Thank you for using Bank Management System! 👋".center(60))
                print("=" * 60 + "\n")
                sys.exit(0)
            else:
                print_error("Invalid choice! Please select 0-7.")
                press_enter_to_continue()
        
        except KeyboardInterrupt:
            print("\n\n" + "=" * 60)
            print("  Exiting... Thank you! 👋".center(60))
            print("=" * 60 + "\n")
            sys.exit(0)
        except Exception as e:
            print_error(f"An unexpected error occurred: {e}")
            press_enter_to_continue()


if __name__ == "__main__":
    main()