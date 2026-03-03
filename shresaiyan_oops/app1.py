"""
Bank Management System - Streamlit UI
Modern, user-friendly interface for banking operations
"""

import streamlit as st
from bank_manager import Bank
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        margin: 1rem 0;
    }
    .error-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        margin: 1rem 0;
    }
    .info-card {
        padding: 1.5rem;
        border-radius: 0.5rem;
        background-color: #f8f9fa;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .stat-card {
        padding: 1rem;
        border-radius: 0.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'account_no' not in st.session_state:
    st.session_state.account_no = None
if 'pin' not in st.session_state:
    st.session_state.pin = None

# Load data on startup
Bank.load_data()


def logout():
    """Logout user"""
    st.session_state.logged_in = False
    st.session_state.account_no = None
    st.session_state.pin = None
    st.rerun()


def login_page():
    """Login page for existing users"""
    st.markdown('<h1 class="main-header">🏦 Bank Management System</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### 🔐 Login to Your Account")
        
        with st.form("login_form"):
            account_no = st.text_input("Account Number", placeholder="Enter your account number")
            pin = st.text_input("PIN", type="password", placeholder="Enter 4-digit PIN", max_chars=4)
            
            col_a, col_b = st.columns(2)
            with col_a:
                login_btn = st.form_submit_button("🔓 Login", use_container_width=True)
            with col_b:
                create_btn = st.form_submit_button("➕ Create Account", use_container_width=True)
            
            if login_btn:
                if not account_no or not pin:
                    st.error("Please enter both account number and PIN")
                else:
                    try:
                        pin_int = int(pin)
                        account = Bank.authenticate(account_no, pin_int)
                        
                        if account:
                            st.session_state.logged_in = True
                            st.session_state.account_no = account_no
                            st.session_state.pin = pin_int
                            st.success("✅ Login successful!")
                            st.rerun()
                        else:
                            st.error("❌ Invalid account number or PIN")
                    except ValueError:
                        st.error("❌ PIN must be a 4-digit number")
            
            if create_btn:
                st.session_state.show_create = True
                st.rerun()
        
        # Show statistics
        st.markdown("---")
        col_stat1, col_stat2 = st.columns(2)
        with col_stat1:
            st.metric("Total Accounts", Bank.get_total_accounts())
        with col_stat2:
            st.metric("Total Deposits", f"₹{Bank.get_total_balance():,.2f}")


def create_account_page():
    """Create new account page"""
    st.markdown('<h1 class="main-header">🏦 Create New Account</h1>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### 📝 Account Registration")
        
        with st.form("create_account_form"):
            name = st.text_input("Full Name *", placeholder="Enter your full name")
            age = st.number_input("Age *", min_value=1, max_value=120, value=18)
            email = st.text_input("Email *", placeholder="your.email@example.com")
            pin = st.text_input("4-Digit PIN *", type="password", max_chars=4, 
                              placeholder="Create a 4-digit PIN")
            confirm_pin = st.text_input("Confirm PIN *", type="password", max_chars=4,
                                       placeholder="Re-enter your PIN")
            
            col_a, col_b = st.columns(2)
            with col_a:
                submit_btn = st.form_submit_button("✅ Create Account", use_container_width=True)
            with col_b:
                back_btn = st.form_submit_button("🔙 Back to Login", use_container_width=True)
        
        # Handle form submission OUTSIDE the form
        if submit_btn:
            if not all([name, email, pin, confirm_pin]):
                st.error("❌ Please fill all required fields")
            elif pin != confirm_pin:
                st.error("❌ PINs do not match!")
            else:
                try:
                    pin_int = int(pin)
                    success, message, account_info = Bank.create_account(name, age, email, pin_int)
                    
                    if success:
                        st.success(f"✅ {message}")
                        st.balloons()
                        
                        # Display account details
                        st.markdown("---")
                        st.markdown("### 🎉 Account Created Successfully!")
                        st.info(f"""
                        **Account Number:** `{account_info['accountNo']}`  
                        **Name:** {account_info['name']}  
                        **Email:** {account_info['email']}  
                        **Initial Balance:** ₹0.00
                        
                        ⚠️ **Important:** Please save your account number safely!
                        """)
                        
                        # Use a button OUTSIDE the form
                        if st.button("Continue to Login", key="continue_login"):
                            st.session_state.show_create = False
                            st.rerun()
                    else:
                        st.error(f"❌ {message}")
                except ValueError:
                    st.error("❌ PIN must be a 4-digit number")
        
        if back_btn:
            st.session_state.show_create = False
            st.rerun()


def dashboard_page():
    """Main dashboard for logged-in users"""
    # Get account details
    success, account, message = Bank.get_account_details(
        st.session_state.account_no, 
        st.session_state.pin
    )
    
    if not success:
        st.error("❌ Error loading account details")
        logout()
        return
    
    # Header
    st.markdown(f'<h1 class="main-header">Welcome, {account["name"]}! 👋</h1>', unsafe_allow_html=True)
    
    # Logout button
    col1, col2, col3 = st.columns([5, 1, 1])
    with col3:
        if st.button("🚪 Logout", use_container_width=True):
            logout()
    
    st.markdown("---")
    
    # Account summary cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <h3>💰 Balance</h3>
            <h2>₹{account['balance']:,.2f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <h3>🏦 Account</h3>
            <h4>{account['accountNo']}</h4>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        transactions = account.get('transactions', [])
        st.markdown(f"""
        <div class="stat-card">
            <h3>📊 Transactions</h3>
            <h2>{len(transactions)}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        created = datetime.fromisoformat(account['created_at']).strftime('%d %b %Y')
        st.markdown(f"""
        <div class="stat-card">
            <h3>📅 Member Since</h3>
            <h4>{created}</h4>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Sidebar for operations
    with st.sidebar:
        st.markdown("## 🎯 Quick Actions")
        operation = st.radio(
            "Select Operation:",
            ["💳 Deposit Money", "💸 Withdraw Money", "📜 Transaction History", 
             "👤 Account Details", "✏️ Update Profile", "🗑️ Delete Account"],
            label_visibility="collapsed"
        )
    
    # Main content area based on selected operation
    if operation == "💳 Deposit Money":
        deposit_section(account)
    
    elif operation == "💸 Withdraw Money":
        withdraw_section(account)
    
    elif operation == "📜 Transaction History":
        transaction_history_section()
    
    elif operation == "👤 Account Details":
        account_details_section(account)
    
    elif operation == "✏️ Update Profile":
        update_profile_section()
    
    elif operation == "🗑️ Delete Account":
        delete_account_section()


def deposit_section(account):
    """Deposit money section"""
    st.markdown("### 💳 Deposit Money")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("deposit_form"):
            amount = st.number_input(
                "Amount to Deposit (₹)", 
                min_value=1.0, 
                max_value=10000.0, 
                value=100.0,
                step=100.0
            )
            
            st.info("ℹ️ Maximum deposit per transaction: ₹10,000")
            
            submit = st.form_submit_button("💰 Deposit", use_container_width=True)
            
            if submit:
                success, message = Bank.deposit_money(
                    st.session_state.account_no,
                    st.session_state.pin,
                    amount
                )
                
                if success:
                    st.success(f"✅ {message}")
                    st.balloons()
                    st.rerun()
                else:
                    st.error(f"❌ {message}")
    
    with col2:
        st.markdown("#### 💡 Quick Amounts")
        if st.button("₹500", use_container_width=True):
            Bank.deposit_money(st.session_state.account_no, st.session_state.pin, 500)
            st.success("✅ ₹500 deposited!")
            st.rerun()
        if st.button("₹1,000", use_container_width=True):
            Bank.deposit_money(st.session_state.account_no, st.session_state.pin, 1000)
            st.success("✅ ₹1,000 deposited!")
            st.rerun()
        if st.button("₹5,000", use_container_width=True):
            Bank.deposit_money(st.session_state.account_no, st.session_state.pin, 5000)
            st.success("✅ ₹5,000 deposited!")
            st.rerun()


def withdraw_section(account):
    """Withdraw money section"""
    st.markdown("### 💸 Withdraw Money")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("withdraw_form"):
            amount = st.number_input(
                "Amount to Withdraw (₹)", 
                min_value=1.0, 
                max_value=float(account['balance']), 
                value=min(100.0, float(account['balance'])),
                step=100.0
            )
            
            st.info(f"ℹ️ Available balance: ₹{account['balance']:,.2f}")
            
            submit = st.form_submit_button("💸 Withdraw", use_container_width=True)
            
            if submit:
                success, message = Bank.withdraw_money(
                    st.session_state.account_no,
                    st.session_state.pin,
                    amount
                )
                
                if success:
                    st.success(f"✅ {message}")
                    st.rerun()
                else:
                    st.error(f"❌ {message}")
    
    with col2:
        st.markdown("#### 💡 Quick Amounts")
        if account['balance'] >= 500:
            if st.button("₹500", use_container_width=True, key="w500"):
                Bank.withdraw_money(st.session_state.account_no, st.session_state.pin, 500)
                st.success("✅ ₹500 withdrawn!")
                st.rerun()
        if account['balance'] >= 1000:
            if st.button("₹1,000", use_container_width=True, key="w1000"):
                Bank.withdraw_money(st.session_state.account_no, st.session_state.pin, 1000)
                st.success("✅ ₹1,000 withdrawn!")
                st.rerun()
        if account['balance'] >= 5000:
            if st.button("₹5,000", use_container_width=True, key="w5000"):
                Bank.withdraw_money(st.session_state.account_no, st.session_state.pin, 5000)
                st.success("✅ ₹5,000 withdrawn!")
                st.rerun()


def transaction_history_section():
    """Transaction history section"""
    st.markdown("### 📜 Transaction History")
    
    success, transactions, message = Bank.get_transaction_history(
        st.session_state.account_no,
        st.session_state.pin,
        limit=50
    )
    
    if not success or not transactions:
        st.info("ℹ️ No transactions yet. Start by depositing money!")
        return
    
    # Create DataFrame for better display
    df_data = []
    for trans in transactions:
        df_data.append({
            "Date & Time": datetime.fromisoformat(trans['timestamp']).strftime('%d %b %Y, %I:%M %p'),
            "Type": trans['type'].title(),
            "Amount (₹)": f"{trans['amount']:,.2f}",
            "Balance After (₹)": f"{trans['balance_after']:,.2f}"
        })
    
    df = pd.DataFrame(df_data)
    
    # Display as table
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
    
    # Summary statistics
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    deposits = [t for t in transactions if t['type'] == 'deposit']
    withdrawals = [t for t in transactions if t['type'] == 'withdrawal']
    
    with col1:
        total_deposits = sum(t['amount'] for t in deposits)
        st.metric("Total Deposits", f"₹{total_deposits:,.2f}", f"{len(deposits)} transactions")
    
    with col2:
        total_withdrawals = sum(t['amount'] for t in withdrawals)
        st.metric("Total Withdrawals", f"₹{total_withdrawals:,.2f}", f"{len(withdrawals)} transactions")
    
    with col3:
        net_change = total_deposits - total_withdrawals
        st.metric("Net Change", f"₹{net_change:,.2f}")


def account_details_section(account):
    """Account details section"""
    st.markdown("### 👤 Account Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="info-card">
            <h4>📋 Personal Information</h4>
            <p><strong>Name:</strong> {account['name']}</p>
            <p><strong>Age:</strong> {account['age']}</p>
            <p><strong>Email:</strong> {account['email']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        created = datetime.fromisoformat(account['created_at']).strftime('%d %B %Y, %I:%M %p')
        st.markdown(f"""
        <div class="info-card">
            <h4>🏦 Banking Information</h4>
            <p><strong>Account Number:</strong> {account['accountNo']}</p>
            <p><strong>Balance:</strong> ₹{account['balance']:,.2f}</p>
            <p><strong>Created:</strong> {created}</p>
        </div>
        """, unsafe_allow_html=True)


def update_profile_section():
    """Update profile section"""
    st.markdown("### ✏️ Update Profile")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("update_form"):
            st.info("ℹ️ Leave fields empty to keep current values")
            
            name = st.text_input("New Name (optional)", placeholder="Enter new name")
            email = st.text_input("New Email (optional)", placeholder="Enter new email")
            new_pin = st.text_input("New PIN (optional)", type="password", max_chars=4,
                                   placeholder="Enter new 4-digit PIN")
            confirm_pin = st.text_input("Confirm New PIN", type="password", max_chars=4,
                                       placeholder="Re-enter new PIN")
            
            submit = st.form_submit_button("💾 Update Profile", use_container_width=True)
            
            if submit:
                # Validate PIN confirmation if provided
                if new_pin and new_pin != confirm_pin:
                    st.error("❌ PINs do not match!")
                    return
                
                # Convert PIN to int if provided
                pin_to_update = None
                if new_pin:
                    try:
                        pin_to_update = int(new_pin)
                    except ValueError:
                        st.error("❌ PIN must be a 4-digit number")
                        return
                
                # Update account
                success, message = Bank.update_account(
                    st.session_state.account_no,
                    st.session_state.pin,
                    name=name if name else None,
                    email=email if email else None,
                    new_pin=pin_to_update
                )
                
                if success:
                    st.success(f"✅ {message}")
                    
                    # Update session PIN if changed
                    if pin_to_update:
                        st.session_state.pin = pin_to_update
                        st.info("🔐 Your PIN has been updated. Please remember your new PIN!")
                    
                    st.rerun()
                else:
                    st.error(f"❌ {message}")


def delete_account_section():
    """Delete account section"""
    st.markdown("### 🗑️ Delete Account")
    
    st.warning("⚠️ **Warning:** This action cannot be undone!")
    
    with st.form("delete_form"):
        st.markdown("""
        Are you sure you want to delete your account? All your data will be permanently removed.
        
        Please confirm by typing **DELETE** below:
        """)
        
        confirmation = st.text_input("Type DELETE to confirm")
        
        col1, col2 = st.columns(2)
        with col1:
            delete_btn = st.form_submit_button("🗑️ Delete Account", use_container_width=True, type="primary")
        with col2:
            cancel_btn = st.form_submit_button("❌ Cancel", use_container_width=True)
        
        if delete_btn:
            if confirmation == "DELETE":
                success, message = Bank.delete_account(
                    st.session_state.account_no,
                    st.session_state.pin
                )
                
                if success:
                    st.success(f"✅ {message}")
                    st.info("Your account has been deleted. Redirecting to login page...")
                    st.session_state.logged_in = False
                    st.session_state.account_no = None
                    st.session_state.pin = None
                    st.rerun()
                else:
                    st.error(f"❌ {message}")
            else:
                st.error("❌ Please type DELETE to confirm account deletion")


# Main app logic
def main():
    """Main application logic"""
    
    # Check if user wants to create account
    if hasattr(st.session_state, 'show_create') and st.session_state.show_create:
        create_account_page()
    # Check if user is logged in
    elif st.session_state.logged_in:
        dashboard_page()
    # Show login page
    else:
        login_page()


if __name__ == "__main__":
    main()