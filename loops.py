# While loop questions =================================


# Create a random number guessing game with python.
import random 
num = random.randint(1 , 10)
tries = 0

while True:
    guess = int(input("please guess your number b/w 1 and 10:- "))

    if num == guess:
        tries += 1
        print(f"you are right! Successfully you guessed the number in {tries} tries")
        break
    elif num < guess:
        print("go a little lower")
        tries += 1
    elif num > guess:
        print("go a little higher")
        tries += 1
    else:
        tries += 1
        print("Sorry, try again")





# Accept a number and check if it is a pallindromic number (If number and its reverse are equal?
# n = int(input("enter a number:- ")) 
# copy = n
# rev = 0 
# while n > 0:
#     rev = rev * 10 + n % 10 
#     n = n // 10 
# if copy == rev:
#     print(f"{copy} is a palindrome")
# else:
#     print(f"{copy} is not a palindrome")



# Accept a number and print its reverse
# n = int(input("enter a number:- "))
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n // 10
# print(rev)




# Separate each digit of a number and print it on the new line
# a = int(input("tell your number: "))
# while a > 0:
#     print(a % 10)
#     a = a // 10














# ================= For loop questions
# Count all letters, digits, and special symbols from a given string
# Given: str1 = "P@#yn26at^&i5ve" 
"""
Expected Outcome:
Total counts of chars, digits, and symbols
Chars = 8
Digits = 3
Symbol = 4
"""
# str1 = "P@#yn26at^&i5ve"
# char = 0
# dig = 0 
# spcl_chr = 0

# for i in str1:
#     if i.isdigit():
#         dig += 1
#     elif i.isalpha():
#         char += 1
#     else:
#         spcl_chr += 1
# print("Total counts of chars, digits, and symbols ============")
# print(f"Your Digits are:- {dig}")
# print(f"Your Characters are:- {char}")
# print(f"Your Spcl Characters are:- {spcl_chr}")




# Check string is Pallindrome or not
# Ex: NAMAN is a Pallindrome
# a = "NAMAN"
# b = ""
# for i in range(len(a) - 1 , -1 , -1):
#     b += a[i]
# if b == a:
#     print(f"{a} is a Pallindrome")
# else:
#     print(f"{a} is not a Pallindrome")





# Reverse a string without using in build functions
# char = "PYTHON"
# char1 = ""
# # char1 = " IS COOL"
# # print(char[::-1])

# for i in range(len(char)-1, -1 , -1):
#     char1 += char[i]
# print(char1)





# Check wether the number is prime or not
# num = int(input("check your number is prime or not :- "))
# count = 0
# for i in range(1 , num + 1):
#     if num % i == 0:
#         count += 1

# if count == 2:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")




# Accept a number and check if it a perfect number or not.
# A number whose sum of factors is equal to the number itself
# Ex - 6 = 1, 2, 3 
# num = int(input("check your number is perfect or not :- "))
# sum = 0
# for i in range(1 , num):
#     if num % i == 0:
#         sum += i

# if sum == num:
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} is not a perfect number")



# Print all the factors of a number
# num = int(input("which number factors you want :- "))
# for i in range(1 , num + 1):
#     if num % i == 0:
#         print(i)



# Print the sum of all even & odd numbers in a range separately
# even = odd = 0 
# for i in range(1 , num + 1):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print(f"your even and odd sum are {even} , {odd}")



# Factorial of a number
# fact = 1 # dont use 0 here
# for i in range(1 , num + 1):
#     fact *= i 
# print(fact)


# Sum up to n terms
# sum = 0
# for i in range(1 , num + 1):
#     sum = sum + i
# print(f"your sum is: {sum}")


# Take a number as input and print its table
# for i in range(1 , 11):
#     print(f"{num} * {i} = {num * i}")


# Reverse for loop. Print n to 1
# for i in range(num , 0, -1):
#     print(i)

# Print natural number up to n
# for i in range(1 , num):
#     print(i)


# Accept an integer and Print hello world n times
# for i in range(1, num):
#     print("Hello world")








# a = "Nature"

# for char in a:
#     print(char)

# for i in range(len(a)):
#     print(a[i])


# for i in range(1 , 6):
#     print(i)

# break , continue , else
# for i in range(1 , 21):
#     if i == 56:
#         print("Break Statement is executed")
#         break
#     print(i)
# else:
#     print("Break Statement is not executed")