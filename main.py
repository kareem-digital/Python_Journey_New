# If- elif ladder
# You cna also create if elif ladder using multiple conditions of elif
# take the input of temperature in celsius
"""
    - Below 0°C → "Freezing Cold 
    - 0°C to 10°C → "Very Cold 
    - 10°C to 20°C → "Cold 
    - 20°C to 30°C → "Pleasant 
    - 30°C to 40°C → "Hot 
    - Above 40°C → "Very Hot "
"""
temp = int(input("please tell your temperature:- "))
if temp < 0:
    print("Freezing Cold")
elif temp >= 0 and temp < 10:
    print(f"Very Cold")
elif temp >=10 and temp < 20:
    print(f"Cold")
elif temp >=20 and temp < 30:
    print(f"Pleasant")
elif temp >=30 and temp < 40:
    print(f"Hot")
else:
    print("Very Hot")    
    

# Q5. Accept a year and check if it a leap year or not
# year = int(input("please enter a year:- "))
# if year % 100 == 0 and year % 400 == 0:
#     print(f"{year} is a leap year")
# elif year % 100 != 0 and year % 4 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")





# Accept name and age from the user. Check if the user is a valid voter or not.
# Ex- “hello shery you are a valid voter”

# name = input("please enter your name:- ")
# age = int(input("please enter your age:- "))
# if age >= 18:
#     print(f"Hello, {name} you are a valid voter")
# else:
#     print(f"Hello, {name} you are not a valid voter")

# Accept an integer and check whether it is an even number or odd.
# num = int(input("please enter a number:- "))
# if num % 2 == 0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")



# Accept the gender from the user as char and print the respective greeting message
# Ex: Good Morning Sir (on the basis of gender)
# gender = input("please tell your gender as Character (M or F):- ")
# if gender == "M" or gender == "m":
#     print("Good Morning SIR")
# elif gender == "F" or gender == "f":
#     print("Good Morning MAM")
# else:
#     print("Please type correct input")



# Accept 2 numbers and print the greatest b/w them
# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# if num1 > num2:
#     print(f"{num1} is a greater than {num2}")
# else:
#     print(f"{num2} is a greater than {num1}")