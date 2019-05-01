# Python program to display the Fibonacci sequence up to nth term using recursive function
"""Fibonacci is a sequence of number in which each number is the sum of two preceeding number.
In this program, I am using swap technique of python"""

print("Hi, This program will tell you the Fibonacci Series for a given number using recursion")
def fibo_seq(value):
    if(value <= 1):
        return value
    else:
        return (fibo_seq(value-1) + fibo_seq(value-2))

in_val = int(input("Enter a integer:"))

print("Fibonacci sequence using Recursion :")
for iter in range(0,in_val):
    print(fibo_seq(iter))
