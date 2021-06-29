import calculator
print("Enter the value x :")
x=int(input())
print("Enter the value y :")
y=int(input())
z=int(input("Slect any value between 1 to 4 : "))
if z==1:
    print("Addition value is :",calculator.addme(x,y))
if z==2:
    print("Subraction value is :",calculator.subme(x,y))

if z==3:
    print("Multiplication value is :",calculator.multme(x,y))
if z==4:
    print("division value is :",calculator.divme(x,y))