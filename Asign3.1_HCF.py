# Python program to print Highest Common Factor (HCF) of two numbers
""" There are multiple ways to achive this. Various options listed:
1. Using math library: math.gcd()
2. The highest common factor is found by multiplying all the factors which appear in both lists
for example HCF of 38 and 12: we diving 38 by 12 and the reminder 2, which we again
divide by 12,and repeating this untill the reminder is zero.In this case, HCF is 12
We are also trying to use the swaping functionality in python"""

# import math
print("Hi, This program is to print Highest Common Factor (HCF) of two numbers")
def findhcf(num1,num2):
    while(num2):
        num1,num2 = num2, num1%num2
    return num1

while True:
    try:
        num1,num2 = map(int, input("Enter two numbers to find HCF: ").split())
        # print("The HCF of {} and {} is: {}".format(num1,num2,math.gcd(num1,num2)))
        print("The HCF of {} and {} is: {}".format(num1,num2,findhcf(num1,num2)))
        break
    except ValueError:
        print("Entered value is incorrect. Try again..")
