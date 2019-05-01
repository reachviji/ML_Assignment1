# Python Program to Check where a String is Palindrome or not?
""" This can be achieved using two options:
1. using var[::-1] : This reverses the word
2. using ''.join(reversed(in_str)) : This reverses the word
In this program we will go with option 1 """

print("Hi, This program is check if a string is Palindrome or not?")
def reverse(s):
    return s[::-1]

in_str = str(input("Enter a string to check for Palindrome: "))
rev_str = reverse(in_str)
# Option 2: rev = ''.join(reversed(in_str)) ; print(rev)
if in_str == rev_str:
    print("Entered string {} is a palindrome".format(in_str))
else:
    print("Entered string {} is not a palindrome".format(in_str))
