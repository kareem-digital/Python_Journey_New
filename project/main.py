# File Handling CRUD project / task
from pathlib import Path 
import os 

# check the files and folder in current directory
def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i , item in enumerate(items):
        print(f"{i + 1} : {item}")


# CREATE
def createFile():
    try:    
        readFileAndFolder()
        name = input("please tell your file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p , 'w') as fs:
                data = input("What you want to write in this file :- ")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY!!")
        else:
            print("This file already exist")

    except Exception as err:
        print(f"An error occured as: {err}")

# READ
def readFile():
    try:
        readFileAndFolder()
        name = input('which file you want to read :- ')
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p , 'r') as fs:
                data = fs.read()
                print(data)
            print("READ FILE SUCCESSFULLY")
        else:
            print("file does not exist!!")
    except Exception as err:
        print(f"An error occured as : {err}")


# UPDATE 
def updateFile():
    try:
        readFileAndFolder()
        name = input("tell me, which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file :- ")
            print("press 2 for overwriting the data of your file :- ")
            print("press 3 for appending some content in your file :- ")

            res = int(input("tell your response :- "))

            if res == 1:
                name2 = input("tell your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p , 'w') as fs:
                    data = input("tell what you want to write this will overwrite the data :- ")
                    fs.write(data)

            if res == 3:
                with open(p , 'a') as fs:
                    data = input("tell what you want to append :- ")
                    fs.write(" " + data)

    except Exception as err:
        print(f"An error occured as: {err}")



# DELETE
def deleteFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("FILE DELETE SUCCESSFULLY")
        else:
            print("No such file exist!")

    except Exception as err:
        print(f"An error occured as : {err}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deletion a file")

check = int(input("please tell your response :- "))

if check == 1:
    createFile()

if check == 2:
    readFile()

if check == 3:
    updateFile()

if check == 4:
    deleteFile()