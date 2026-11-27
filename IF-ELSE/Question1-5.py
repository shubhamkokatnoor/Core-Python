# Q) Age = 18 to get answer is eligible to vote show this condition.

age = int(input("enter your age :"))

if age>=18:
    print("Person is eligible to vote")
else:
    print("Person is not eligible to vote")
#---------------------------------------------------------------
# Q) Write a program a given number is even or odd.

num = int(input("Enter a number to check even or odd :"))

if num%2==0:
    print("Number is Even")
else:
    print("Number is Odd")
#---------------------------------------------------------------
# Q) Find max number between two numbers.

a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

if a>b:
    print(a,"is max")
else:
    print(b,"is max")
#---------------------------------------------------------------
# Q) Write a program to check number is divisible by 5 or not.

num = int(input("enter a number :"))

if num%5==0:
    print(num,"Number is divisible by 5")
else:
    print(num,"Number is not divisible by 5")
#---------------------------------------------------------------
# Q) Write a program to check a given number is even but number is positive integer.

num = int(input("Enter a number :"))

if num%2==0 and num>0:
    print("Number is even and positive integer")
else:
    print("Number is not even or not positive integer")