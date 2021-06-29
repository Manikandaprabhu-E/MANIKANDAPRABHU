# number = 7
#
# if number > 1:
#     for i in range(2, number):
#         if (number % i == 0):
#             print("This is not prime number")
#             print(i, "times", number//i, "is", number)
#             break
#     else:
#         print("This number is prime")

number =int(input("Enter the number to check whether its Prime number:"))
if number >1:
    for i in range(2, number): # from 2 only prime number starting hence we have given 2 as range
        if(number % i == 0): #modulus
            print("This is not a prime number")
            print(i, "times", number//i, "is", number)
            break
    else:
        print("%d is a prime number" % (number))


