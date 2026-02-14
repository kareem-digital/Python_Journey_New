# ATM
class Atm:
    # constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0 
        self.menu()

    # atm menu
    def menu(self):
        user_input = input("""
            Hi how i can help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 check balance
            4. Press 4 to withdraw
            5. Anything else to exit 
        """)

        if user_input == "1":
            # create pin
            self.create_pin()
        elif user_input == "2":
            # change pin
            self.change_pin()
        elif user_input == "3":
            # check balance 
            self.check_balane()
        elif user_input == "4":
            # withdraw
            self.withdraw()
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter your pin ")
        self.pin = user_pin

        user_balance = int(input("Enter your balance "))
        self.balance = user_balance

        print('pin created successfully')
        self.menu()

    def change_pin(self):
        old_pin = input("Enter old pin ")
        if old_pin == self.pin:
            # let him change the pin 
            new_pin = input("Enter new pin ")
            self.pin = new_pin 
            print("pin change successfully!")
            self.menu()
        else:
            print("Not possible! at this time")
            self.menu()

    def check_balane(self):
        user_pin = input("enter your pin ")
        if user_pin == self.pin:
            print(f"Your balance is {self.balance}")
        else:
            print("Wrong pin, Try again")
        

    def withdraw(self):
        user_pin = input("enter your pin ")
        if user_pin == self.pin:
            # allow to withdraw
            amount = int(input("enter the amount "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print('Withdrawl Successful')
                print(f"Remaining Balance: {self.balance}")
            else:
                print("Insufficient Balance")
        else:
            print("Wrong pin, Try again")
        self.menu()

obj = Atm()