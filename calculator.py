"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

def singlecalcs():
    if operator == "square":
        print square(num1)
    elif operator == "cube":
        print cube(num1)

def doublecalcs():
    if operator == "+":
        print add(num1,num2)
    elif operator == "-":
        print subtract(num1,num2)
    elif operator == "*":
        print multiply(num1,num2)
    elif operator == "/":
        print divide(num1,num2)
    elif operator == "pow":
        print power(num1,num2)
    elif operator == "mod":
        print mod(num1,num2)
    else: 
        print "This is not a valid calculation!"

while True:
    input = raw_input("Please type in your calculation:\n")
    tokens = input.split(" ")
    splitnumber = len(tokens)

    if splitnumber == 3:
        operator = tokens[0]
        num1 = int(tokens[1])
        num2 = int(tokens[2])
        for num1 in int and num 2 in int: #Something like that
            doublecalcs()
    elif splitnumber == 2:
        operator = tokens[0]
        num1 = int(tokens[1])
        singlecalcs()
    

