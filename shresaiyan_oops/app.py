import streamlit as st
from bank_backend import Bank

bank = Bank()

st.title("🏦 Simple Bank Management System")

menu = st.sidebar.selectbox(
    "Choose Option",
    ["Create Account", "Deposit", "Withdraw", "Check Details"]
)

# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":
    st.header("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create"):
        success, result = bank.create_account(
            name, age, email, int(pin) if pin else 0
        )

        if success:
            st.success("Account Created Successfully!")
            st.write("Your Account Number:", result["accountNo"])
        else:
            st.error(result)


# ---------------- DEPOSIT ----------------
elif menu == "Deposit":
    st.header("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        success, result = bank.deposit(acc, int(pin), amount)

        if success:
            st.success(f"New Balance: ₹{result}")
        else:
            st.error(result)


# ---------------- WITHDRAW ----------------
elif menu == "Withdraw":
    st.header("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        success, result = bank.withdraw(acc, int(pin), amount)

        if success:
            st.success(f"Remaining Balance: ₹{result}")
        else:
            st.error(result)


# ---------------- DETAILS ----------------
elif menu == "Check Details":
    st.header("Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Check"):
        success, result = bank.get_details(acc, int(pin))

        if success:
            st.json(result)
        else:
            st.error(result)