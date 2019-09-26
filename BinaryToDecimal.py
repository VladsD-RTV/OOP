#converting decimal to binary and then changing binary back to decimal
#Author:Vlads Drobovics
#Date:26/09/2019
#Program:PyCharm
number = int(input("Enter any Decimal Number: "))

if number<0:
    print("Number is Negative")

    quit
else:
    #display the binary conversion
    print("Equivalent Binary Number: ", bin(number))

binary=bin(number)

decimal=int(binary,2)
print(binary ,"the value is ", decimal)