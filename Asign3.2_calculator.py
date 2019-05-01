# Python program to make a simple calculator that can add, subtract, multiply and division
""" This can be achieved using a simple technique without using any librabry function"""

print("Hi, This program adds, subtracts, multiplies and divides two numbers")
while True:
    try:
        choose_opt = int(input("choose one of the following options:\n"
        "1.Add\n"
        "2.Subtract\n"
        "3.Multiply\n"
        "4.Divide: "
        ))

        try:
            num1,num2 = map(int,input("\n\nEnter two number to perform the operation").split())
            if choose_opt == 1:
                print("\nThe sum of {} and {} is: {}".format(num1,num2,(num1+num2)))
            elif choose_opt == 2:
                print("\nThe subtraction of {} and {} is: {}".format(num1,num2,(num1-num2)))
            elif choose_opt == 3:
                print("\nThe multiplication of {} and {} is: {}".format(num1,num2,(num1*num2)))
            elif choose_opt == 4:
                print("\nThe division of {} and {} is: {}".format(num1,num2,(num1/num2)))
            else:
                print("\nInvalid choice {}".format(choose_opt))
            break
        except ValueError:
            print("\nChoose from one of the options. Try again..\n")
    except ValueError:
        print("\nChoose from one of the options. Try again..\n")
        continue
