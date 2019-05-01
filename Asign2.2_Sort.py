# Python Program to Sort Words in Alphabetic Order?
""" This program sort list of words in a given word in aphabetic order"""

print("Hi,program sort list of words in a given word in aphabetic order ")
while True:
    num_list = list(input("Enter a list of words to be sorted: ").split())
    if len(num_list) == 1:
        print("To sort the words, enter more than 1 word. Printing given word: {}".format(num_list))
    else:
        print("Sorting given words in alhabetic order are : {}".format(sorted(num_list)))
        break
