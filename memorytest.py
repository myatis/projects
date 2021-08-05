#It's designed to play from terminal in VsCode.


import os
import sys
import secrets

print("Welcome to memory test.")
print("In order to win you must find all the numbers in a selected range")
print("If you select a number that you selected before you lost.")
level = int(input("Now, enter a number to determine the range. But remember. Higher the number,higher the difficulty.\n-"))

test_list = []

chosen_list = []

for i in range(1,level+1):
    test_list.append(i)

first_number = secrets.choice(test_list)
chosen_list.append(first_number)
test_list.remove(first_number)

print(f"First number is selected by computer and its '{first_number}'. You need to find the rest.")
print(f"Numbers to find: {test_list}\nGOOD LUCK AND HAVE FUN")

while len(test_list) != 0:
    n_test = secrets.choice(test_list)
    n_chosen = secrets.choice(chosen_list)
    print(f"{len(test_list)} numbers to go.")
    answer = int(input(f"Find the next number: {n_test}, {n_chosen}\n--"))

    if answer == n_test:
        chosen_list.append(n_test)
        test_list.remove(n_test)
        os.system('cls')
    elif answer == n_chosen:
        print(f"'{n_chosen}' is already selected.")
        sys.exit( "You lost.")
    else:
        print("That's nat a valid answer.")
        sys.exit("You lost.")

print("Good job! You have the memory of an elephant.")
sys.exit()
