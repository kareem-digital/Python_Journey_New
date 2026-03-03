import json # Convert Python data to/from JSON format (for saving to files)
import random # Generate random values (for account numbers)
import string # Access letters, digits, special characters
from pathlib import Path # Check if files exist (modern way)

class Bank:
    database = 'data.json' #  File name where accounts are stored
    data = [] # List that holds ALL accounts in memory (shared across all Bank objects)

    @classmethod
    def load_data(cls):
        """Load data from JSON file"""
        try:
            if Path(cls.database).exists():
                with open(cls.database, 'r') as fs:
                    content = fs.read()
                    if content.strip():  # Check if file is not empty
                        cls.data = json.loads(content)
                        print(f"Loaded {len(cls.data)} accounts from database")
                    else:
                        print("Database file is empty, starting fresh")
                        cls.data = []
            else:
                print('Database file does not exist, creating new one')
                cls.data = []
                # Create empty file
                with open(cls.database, 'w') as fs:
                    fs.write('[]')
        except json.JSONDecodeError as err:
            print(f"Error reading database (corrupted JSON): {err}")
            cls.data = []
        except Exception as err:
            print(f"An exception occurred: {err}")
            cls.data = []

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)  # Better formatting

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spclchar = random.choices("!@#$%^&*", k=1)
        id = alpha + num + spclchar 
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        info = {
            "name": input("Tell your name :- "),
            "age": int(input("Tell your age :- ")),
            "email": input("Tell your email :- "),
            "pin": int(input("Tell your 4 number pin :- ")),
            "accountNo": Bank.__accountgenerate(),
            "balance": 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print('Sorry! you cannot create account (must be 18+ and PIN must be 4 digits)')
        else:
            print("Account has been created successfully")
            for key, value in info.items():
                print(f"{key}: {value}")
            print("Please note down your account number")

            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your pin :- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print('Sorry! No data found! Please check your account number and PIN.')
            print(f"DEBUG: Total accounts in system: {len(Bank.data)}")
        else:
            amount = int(input("How much money you want to deposit :- "))
            if amount > 10000 or amount <= 0:
                print("Sorry! The amount must be between 1 and 10000")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print(f"Amount deposited successfully! New balance: {userdata[0]['balance']}")

    def withdrawmoney(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your pin :- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print('Sorry! No data found! Please check your account number and PIN.')
            print(f"DEBUG: Total accounts in system: {len(Bank.data)}")
        else:
            amount = int(input("How much money you want to withdraw :- "))
            if userdata[0]['balance'] < amount:
                print("Sorry! Insufficient balance")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print(f"Amount withdrew successfully! New balance: {userdata[0]['balance']}")


    def showdetails(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your pin :- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        print("------------ User Information are -----------------")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")


    def updatedetails(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your pin :- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print('Sorry! No data found!')
        else:
            print("You can not change the age, accountNo, balance")
            print("Fill the details for change or leave it empty if no change")

            newData = {
                "name" : input("please tell new name or press enter :- "), 
                "email" : input("please tell your new Email or press enter to skip :- "), 
                "pin" : input("enter new pin or press enter to skip :- ")
            }

            if newData["name"] == "":
                newData["name"] = userdata[0]["name"]
            if newData["email"] == "":
                newData["email"] = userdata[0]["email"]
            if newData["pin"] == "":
                newData["pin"] = userdata[0]["pin"]

            newData['age'] = userdata[0]['age']
            newData['accountNo'] = userdata[0]['accountNo']
            newData['balance'] = userdata[0]['balance']

            if type(newData['pin']) == str:
                newData['pin'] = int(newData['pin'])

            for i in newData:
                if newData[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newData[i]

            Bank.__update()
            print('Details update sucessfully!')

    def deleteaccount(self):
        accnumber = input("Please tell your account number :- ")
        pin = int(input("Please tell your pin :- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if not userdata:
            print("Sorry! no data found")
        else:
            check = input("press y if you actually you want to delete the account or press n :- ")
            if check == 'n' or check == 'N':
                print("bypassed") 
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)

                print("Account deleted successfully")
                Bank.__update()


# Load data BEFORE creating user
Bank.load_data()

user = Bank()
print("\npress 1 for creating an account")
print("press 2 for depositing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response :- "))

if check == 1:
    user.createaccount()
if check == 2:
    user.depositmoney()
if check == 3:
    user.withdrawmoney()
if check == 4:
    user.showdetails()
if check == 5:
    user.updatedetails()
if check == 6:
    user.deleteaccount()