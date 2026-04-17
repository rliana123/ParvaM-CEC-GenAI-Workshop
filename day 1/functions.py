# functions:
# Syntax:
# def function_name(parameters):
#   Rules of Function


# Parts of Function:
# 1) Function Declaration
# 2) Function Definition
# 3) Function Call


# function declaration
def greet():
    pass


# function definition
# function without parameters
def greet():
    print("Good Morning Sir!")


# function call
greet()
greet()
greet()


# function with parameters:
# variables within paranthesis while defining a function is called as parameters


# variables/values within paranthesis while calling a function is called as arguments


# name is a parameter
def sayHello(name):
    print(f"Hello, {name}!")


# Akshay Rao, Hari & Hemanth are examples of arguments
sayHello("R Liana")
sayHello("Hari")
sayHello("Swathi")


def sum(a, b):
    print(f"Sum of {a} & {b} is {a + b}")


sum(10, 20)
sum(25, 40)


# Default Parameter
def printDetails(name, company="City Eng College"):
    print(f"I'm {name}, studying at {company}.")


printDetails("R Liana")
printDetails("Prakash", "Infosys")


def sumOf2num(num1, num2=10):
    sum = num1 + num2
    print(f"Sum of given 2 numbers ({num1} & {num2}): {sum}")


sumOf2num(25)
sumOf2num(20, 30)
sumOf2num(25, 28)


# *args - Variable Positional Arguments
def findSum(*args):
    sum = 0
    for num in args:
        sum += num
    print(f"Sum of given numbers: {sum}")


findSum(20, 30)
findSum(20, 30, 50)
findSum(20, 30, 50, 60, 80)
findSum(20, 30, 50, 60, 80, 95, 108)


def findEvenOdd(*args):
    print("The given numbers are as follows:")
    for num in args:
        print(num)
   
    print("Even numbers out of given numbers are as follows:")
    for num in args:
        if num % 2 == 0:
            print(num)


    print("Odd numbers out of given numbers are as follows:")
    for num in args:
        if num % 2 != 0:
            print(num)


findEvenOdd(2, 4, 7, 9, 11)
findEvenOdd(1, 3, 6, 8, 11, 14, 16, 19)
findEvenOdd(5, 8, 11, 12, 18, 22, 23)


# **kwargs - Variable length keyword arguments
def printInfo(**person):
    print(f"She is {person["name"]}, she is studying at {person["company"]}")


printInfo(name="R Liana", age=21, company="City Eng College", address="Bengaluru")


printInfo(name="Swathi", company="City Eng College", address="Bengaluru", pincode=560090)


def userInfo(**user):
    print(f"User Details are as follows:")
    print(f"Name: {user["name"]}")
    print(f"Email ID: {user["email"]}")
    print(f"Phone Number: {user["phone"]}")


userInfo(name="R Liana", id=123, email="rliana@gmail.com", company="City Eng College", phone="9686275416", mode_of_transport="Bus")


userInfo(name="Swathi", id=456, email="swathi@gmail.com", company="City Eng College", phone="6364848049", mode_of_transport="Bus")