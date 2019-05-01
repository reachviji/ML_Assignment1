# Assignment 1: Python program to find the largest element among three Numbers
print("Hi, Welcome to the first assignment to find the largest element among three Numbers")
while True:
    try:
        num1, num2, num3 = input('Enter 3 numbers:').split()
        # Procced only if all the entered numbers are integers
        if (num1.isdigit() and num2.isdigit() and num3.isdigit()):
            list = [num1, num2, num3]
            print("The largest Number of the three entered is: {}".format(max(list)))
            break
        else:
            # Continue asking the user.
            print("Enter a valid Number, Try again..")
    except ValueError:
        print("Enter only 3 Numbers, Try again..")
