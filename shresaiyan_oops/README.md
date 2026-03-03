# 🏦 Bank Management System

A modern, secure bank management application with both **Command Line Interface (CLI)** and **Web UI (Streamlit)** support.

## ✨ Features

### 🔐 Security
- **PIN Hashing**: All PINs are hashed using SHA-256 (never stored in plain text)
- **Authentication**: Secure login system
- **Email Validation**: Prevents duplicate accounts

### 💰 Banking Operations
- **Create Account**: Register new users with validation
- **Deposit Money**: Add funds (up to ₹10,000 per transaction)
- **Withdraw Money**: Withdraw funds with balance check
- **Transaction History**: Track all deposits and withdrawals
- **Account Details**: View complete account information
- **Update Profile**: Change name, email, or PIN
- **Delete Account**: Permanently remove account with confirmation

### 📊 Additional Features
- Transaction timestamp tracking
- Balance after each transaction
- Account creation date tracking
- Total accounts and deposits statistics
- Modern, responsive UI with Streamlit

## 📁 Project Structure

```
bank-management/
│
├── bank_manager.py      # Core business logic (Bank class)
├── app.py              # Streamlit web interface
├── cli.py              # Command-line interface
├── requirements.txt    # Python dependencies
├── data.json          # Database (auto-created)
└── README.md          # Documentation
```

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Create a project folder and navigate to it:**
```bash
mkdir bank-management
cd bank-management
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Option 1: Web UI (Streamlit) - Recommended

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will automatically open in your browser at `http://localhost:8501`

### Option 2: Command Line Interface (CLI)

Run the CLI version:
```bash
python cli.py
```

## 📖 User Guide

### Creating an Account

**Web UI:**
1. Click "➕ Create Account" on login page
2. Fill in all required fields:
   - Full Name
   - Age (must be 18+)
   - Email (unique)
   - 4-digit PIN
3. Click "✅ Create Account"
4. Save your account number!

**CLI:**
1. Select option `1`
2. Enter your details when prompted
3. Note down your account number

### Login

**Web UI:**
1. Enter your account number
2. Enter your 4-digit PIN
3. Click "🔓 Login"

**CLI:**
1. Select the desired operation (2-6)
2. Enter account number and PIN when prompted

### Depositing Money

**Web UI:**
1. After login, go to "💳 Deposit Money"
2. Enter amount or use quick buttons (₹500, ₹1000, ₹5000)
3. Click "💰 Deposit"

**CLI:**
1. Select option `2`
2. Enter account number and PIN
3. Enter amount to deposit

### Withdrawing Money

**Web UI:**
1. Go to "💸 Withdraw Money"
2. Enter amount (cannot exceed balance)
3. Click "💸 Withdraw"

**CLI:**
1. Select option `3`
2. Enter account number and PIN
3. Enter amount to withdraw

### Viewing Transaction History

**Web UI:**
1. Go to "📜 Transaction History"
2. View all transactions in a formatted table
3. See summary statistics

**CLI:**
Currently available through account details (option 4)

### Updating Profile

**Web UI:**
1. Go to "✏️ Update Profile"
2. Enter new values (leave blank to keep current)
3. Click "💾 Update Profile"

**CLI:**
1. Select option `5`
2. Enter new values or press Enter to skip
3. Confirm changes

### Deleting Account

**Web UI:**
1. Go to "🗑️ Delete Account"
2. Type **DELETE** to confirm
3. Click "🗑️ Delete Account"

**CLI:**
1. Select option `6`
2. Press `y` to confirm deletion

## 🔒 Security Features

### PIN Security
```python
# PINs are hashed before storage
Original PIN: 1234
Stored Hash: 03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4
```

### Validation Rules
- **Age**: Must be 18 or older
- **PIN**: Exactly 4 digits
- **Email**: Must be unique and valid format
- **Amount**: Deposit max ₹10,000, must be positive

## 📊 Data Structure

### Account Object
```json
{
  "name": "John Doe",
  "age": 25,
  "email": "john@example.com",
  "pin": "hashed_pin_value",
  "accountNo": "a3B@5c1",
  "balance": 5000,
  "created_at": "2024-03-15T10:30:00",
  "transactions": [
    {
      "type": "deposit",
      "amount": 5000,
      "timestamp": "2024-03-15T10:31:00",
      "balance_after": 5000
    }
  ]
}
```

## 🎨 UI Features (Streamlit)

### Dashboard
- **Balance Card**: Current balance with formatted display
- **Account Card**: Account number at a glance
- **Transaction Counter**: Total number of transactions
- **Member Since**: Account creation date

### Quick Actions
- Sidebar navigation for all operations
- Quick amount buttons (₹500, ₹1000, ₹5000)
- Real-time balance updates
- Transaction history with filters

### Design Elements
- Gradient stat cards
- Color-coded success/error messages
- Responsive layout for all screen sizes
- Modern, clean interface

## 🐛 Error Handling

The application handles:
- Invalid account numbers or PINs
- Insufficient balance for withdrawals
- Invalid PIN formats
- Duplicate email addresses
- Corrupted JSON database
- File access errors
- Invalid input types

## 📝 Code Improvements from Original

### 1. **Security**
- ✅ PIN hashing (SHA-256)
- ✅ No plain text PIN storage
- ✅ Better authentication flow

### 2. **Data Integrity**
- ✅ Transaction history tracking
- ✅ Timestamps for all actions
- ✅ Balance after each transaction
- ✅ Account creation tracking

### 3. **Error Handling**
- ✅ Try-catch blocks everywhere
- ✅ Detailed error messages
- ✅ Input validation
- ✅ Type checking

### 4. **Code Quality**
- ✅ Type hints for better IDE support
- ✅ Docstrings for all methods
- ✅ Separation of concerns (business logic vs UI)
- ✅ DRY principle (Don't Repeat Yourself)

### 5. **User Experience**
- ✅ Modern web UI with Streamlit
- ✅ Visual feedback (success/error messages)
- ✅ Progress indicators
- ✅ Statistics dashboard
- ✅ Transaction history visualization

### 6. **Features**
- ✅ Transaction history
- ✅ Quick amount buttons
- ✅ Account statistics
- ✅ Email uniqueness check
- ✅ Better update flow

## 🔧 Troubleshooting

### Issue: "streamlit: command not found"
**Solution:**
```bash
pip install --upgrade streamlit
```

### Issue: "Permission denied" when accessing data.json
**Solution:**
```bash
chmod 644 data.json
```

### Issue: Can't login after creating account
**Solution:**
- Check that account number is copied correctly
- Ensure PIN is exactly 4 digits
- Verify data.json file exists and is not empty

### Issue: Corrupted database
**Solution:**
```bash
# Backup current file
mv data.json data.json.backup

# Create fresh database
echo "[]" > data.json
```

## 📈 Future Enhancements

Potential features to add:
- [ ] Interest calculation
- [ ] Loan management
- [ ] Multiple account types (Savings, Current)
- [ ] Fund transfers between accounts
- [ ] Email notifications
- [ ] Export transactions to PDF/Excel
- [ ] Admin dashboard
- [ ] Account statements
- [ ] Multi-currency support
- [ ] Two-factor authentication

## 🤝 Contributing

To contribute improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Developer Notes

### Key Classes and Methods

**Bank Class** (`bank_manager.py`)
- `load_data()`: Load accounts from JSON
- `save_data()`: Save accounts to JSON
- `create_account()`: Create new account
- `authenticate()`: Verify credentials
- `deposit_money()`: Add funds
- `withdraw_money()`: Remove funds
- `get_account_details()`: Fetch account info
- `update_account()`: Modify account
- `delete_account()`: Remove account
- `get_transaction_history()`: Fetch transactions

### Database Schema
The `data.json` file stores an array of account objects. Each operation modifies this file through the `save_data()` method.

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review error messages carefully
3. Ensure all dependencies are installed
4. Verify Python version (3.8+)

---

**Made with ❤️ using Python and Streamlit**