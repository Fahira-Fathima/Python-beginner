# program for determining odd or even by gettiong an input and dealing with errors
print( "enter the number : ")
try:
    number = int(input())
except:
    print("only number allowed")
else:
    if number % 2 ==0:
        print("number is even")
    else:
        print("number is odd")
 '''try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
else:
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")'''
