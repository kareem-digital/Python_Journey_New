def pallindrome(st):
    rev = ""
    for i in range(len(st) -1 , -1 , -1):
        rev += st[i]

    if rev == st:
        print(f"{st} is Pallindrome")
    else:
        print(f"{st} is not a pallindrome")

pallindrome("NAMAN")
pallindrome("FARMAN")

# def arithmetic(num1, num2):
#     add = num1 + num2
#     sub = num1 - num2
#     multiply = num1 * num2
#     division = num1 / num2
#     # return four values
#     return add, sub, multiply, division

# # read four return values in four variables
# a, b, c, d = arithmetic(10, 2)

# print("Addition: ", a)
# print("Subtraction: ", b)
# print("Multiplication: ", c)
# print("Division: ", d)


# def is_even(list1):
#     even_num = []
#     for n in list1:
#         if n % 2 == 0:
#             even_num.append(n)
#     # return a list
#     return even_num

# # Pass list to the function
# even_num = is_even([2, 3, 42, 51, 62, 70, 5, 9])
# print("Even numbers are:", even_num)



# def information(**kwargs):
#     for key , value in kwargs.items():
#         print(f"{key} : {value}")
# information(name="john",age=25 , city="India")


# def addition(*numbers):
#     total = 0 
#     for num in numbers:
#         total += num 
#     print(f"Sum is: {total}")

# addition()
# addition(10 , 15 , 5 , 6)
# addition(45 , 25 , 2.5)