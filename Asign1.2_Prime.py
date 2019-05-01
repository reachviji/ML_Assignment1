# Python Program to check given number is Prime number or not
""" this functionality can be achieved by math using for loop, however;
in current case, I am trying to achive the same using python library"""

import sympy as sp
print("Hi, welcome to assignment 1.2: Program to check if number is prime or not")
while True:
    try:
        in_value = int(input("Enter a number: "))
        print("Is the entered value {} prime? : {}".format(in_value,sp.isprime(in_value)))
        break
    except ValueError:
        print("Entered value is incorret, Try again..")
