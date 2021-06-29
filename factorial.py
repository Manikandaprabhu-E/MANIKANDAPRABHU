# fact= int(input("Enter the number to identify factorial :"))
#
# factorial =1
#
# if fact < 0:
#     print("We dnt calculate negative value in factorial")
# elif fact == 0:
#     print("The factorial value is 1")
# else:
#     for i in range(1,fact+1):
#         factorial= factorial*i
#     print("The factorial number is ", factorial)


#Reverese

# fact= int(input("Enter the number to identify factorial :"))
#
# factorial =1
#
# if fact < 0:
#     print("We dnt calculate negative value in factorial")
# elif fact == 0:
#     print("The factorial value is 1")
# else:
#     for i in range(fact,1,-1):
#         factorial= factorial*i
#     print("The factorial number is ", factorial)


#Without Range

number = int(input("Enter the number to identify factorial :"))

i=number
fact = 1

if(number < 0):
    print("We dnt calculate negative value in factorial")
elif(number == 0):
    print("The factorial value is 1")
else:
    while i > 1:
        fact = fact * i
        i = i -1
    print("Factorial is: ", fact)



