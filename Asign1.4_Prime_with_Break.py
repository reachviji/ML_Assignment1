# Python Program to check given number is Prime number or not (using break)
""" In Assignment 1.2 we used Python library sympy
In this case we will achieve the same using the regular for loop and break statement"""

print("Hi, welcome to assignment 1.4: Program to check if number is prime or not using break")
while True:
    try:
        in_value = int(input("Enter a number: "))
        if in_value <= 1:
            print("The entered value {}, is not a prime number ".format(in_value))
        for i in range(2,in_value//2):
            if(in_value % i) == 0:
                print("Entered value {} is not a prime number".format(in_value))
                break
        else:
            print("Entered value",in_value,"is a prime number")
            break

    except ValueError:
        print("Entered value is incorret, Try again..")
