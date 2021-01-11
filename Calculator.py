#Calcultor 
import math
def add(x, y):
    return x+y
def differnce(x, y):
    return x-y
def multiply(x, y):
    return x*y
def divide(x, y):
    return x/y
def square(a):
    return a*a
def sq(a):
    return math.sqrt(a)
try:
    f=input("What you want to do.\nPress : \na for addition , \nd for differnce,\nm for multiplication , \ndi for divison, \ns for square  \nsqt for squareroot : ")
except Exception as e:
    print("You enteres an unknown value :")
# c=int(input("Enter the number :"))
# d=int(input("Enter the number :"))
# e=int(input("Enter the number :"))
try:
    if f=="a":
        c=int(input("Enter the number :"))
        d=int(input("Enter the number :"))
        print(f"The sum of {c} and {d} is {add(c, d)}")
except Exception as e:
    print("You entered an unknown value")
try:
    if f=="d":
        c=int(input("Enter the number :"))
        d=int(input("Enter the number :"))
        print(f"The differnce  of {c} and {d} is {differnce(c, d)}")
except Exception as e:
    print("You entered an unknown value")
try:
    if f=="m":
        c=int(input("Enter the number :"))
        d=int(input("Enter the number :"))
        print(f"The product of {c} and {d} is {multiply(c, d)}")
except Exception as e:
    print("You entered an unknown value")
try:
    if f=="di":
        c=int(input("Enter the number :"))
        d=int(input("Enter the number :"))
    # if d==0:
    #     print(" 0 can't be divided at the denominator")
        print(f"The quotient of {c} and {d} is {divide(c, d)}")
    # if d==0:
    #     print(" 0 can't be divided at the denominator")
except Exception as e:
    print("You entered a wrong or uncalulatable value value")
try:
    if f=="s":
        c=int(input("Enter the number :"))
        print(f"The square of {c} is {square(c)}")
except Exception as e:
    print("You entered an unknown value")
try:
    if f=="sqt":
         c=int(input("Enter the number :"))
         print(f"The squareroot of {c} is {sq(c)}")
except Exception as e:
    print("You entered an unknown value")
