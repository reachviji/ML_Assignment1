# Python program to display the Fibonacci sequence up to nth term using recursive function
"""Fibonacci is a sequence of number in which each number is the sum of two preceeding number.
In this program, I am using swap technique of python"""

print("Hi, This program will tell you the Fibonacci Series for a given number")
def fibonacci(in_val):
    n_first, n_second = 0, 1
    fibo = []
    while n_first < in_val:
        fibo.append(n_first)
        n_first,n_second = n_second, n_first+n_second
    print(fibo)

while True:
    try:
        in_val = int(input("Enter a integer: "))
        if in_val > 1:
            print("Fibonacci Series: ")
            fibonacci(in_val)
            break
        elif in_val <= 1:
            print("Entered value is incorrect, Try again..")
    except ValueError:
        print("Entered value is incorrect, Try again..")
