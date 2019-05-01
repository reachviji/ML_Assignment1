# Python Program to display all prime numbers within an interval
""" In this case, we are going to use sympy library to find the list of
prime numbers, within a given interval"""
import sympy as sp
print("Hi, this program will display all prime numbers within an interval")
while True:
    try:
        num1, num2 = map(int, input("Enter a 2 numbers: ").split())
        # if(num1.isdigit() and num2.isdigit()):
        print("The prime numbers between {} and {} are: {}".format(num1, num2,list(sp.primerange(num1,num2))))
        break
    except ValueError:
        print("Enter only 2 numbers, try again")
