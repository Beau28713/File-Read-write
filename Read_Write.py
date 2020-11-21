import sys
import collections

choice = 0

#use this function to enter numbers to file manually
def enter_nums():
    num = [int(x) for x in input("\nEnter the numbers seperated with a space: ").split()]
    print("\n")

    string_map = map(str, num)
    string_join = " ".join(string_map)

    file = open("lotto_numbers.txt", "a")
    file.write(string_join)
    file.write("\n")

    file.close()
    
#Use this function to find a sigle number in the file  
def find_number():
    number = input("\nEnter number you are looking for: ")
    
    file = open("lotto_numbers.txt", "r")
    
    if number in file.read():
        print("\nyes\n")

    else:
        print("\nno\n")
        
#Use this function to count the most common 6 numbers in the file
def count_numbers():
    file = open("lotto_numbers.txt", "r")

    x = file.read()
    y = x.split()
        
    print("\n")
    
    print(collections.Counter(y).most_common(6))
    
    print("\n")
        
while choice != 4:
    choice = input("""would you like to read from file or input numbers?
press 1 and enter to read from file
press 2 and enter to input numbers
press 3 and enter count numbers in file
press 4 and enter to quit
Please make your selection: """)

    if choice == "1":
        find_number()

    elif choice == "2":
        enter_nums()
        
    elif choice == "3":
        count_numbers()

    else:
        sys.exit()
