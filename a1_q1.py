"""
CISC-121 2023W
Name: Kamana Chapagain
Student Number: 20342877
Email: 21kc77@queensu.ca
Date: 2023-01-12

I confirm that this assignment solution is my own work and conforms
to Queen’s standards of Academic Integrity
"""
import random
import math

def integer_generator():
    """
    This function generates a random integer between 0 and 100.
    :param: none
    :return: num, an integer that was randomly generated
    """

    num = (random.randint(0,100))
    print('the random number is', + num)
    return num

def check_differences(num_1, num_2):
    """
    This function checks the difference between the 2 intege and prints a statement that corresponds with the difference.
    :param num_1: first random integer
    :param num_2: second random integer
    :return: none
    """
    
    invalid = 'yes'
    while invalid == 'yes':
        if (abs(num_1 - num_2)) > 10 and (abs(num_1 - num_2)) < 50:
            print('The pair of integers is valid')
            invalid = 'no'
        else:
            print('This pair of integers is invalid')
            if (abs(num_1 - num_2)) < 10:
                if num_1 > num_2:
                    num_2 = num_2 * 2
                    print(num_1, num_2)
                else:
                    num_1 = num_1 * 2
                    print(num_1, num_2)
            else:
                if num_1 > num_2:
                    #round the number up
                    num_1 = math.ceil(num_1/3)
                    print(num_1, num_2)
                else:
                    num_2 = math.ceil(num_2/3)
                    print(num_1, num_2)

    print_num(num_1, num_2)
    
def print_num(num_1, num_2):
    """
    This function prints the 2 numbers in increasing order, or other words when certain conditions are satisfied.
    :param num_1: first integer
    :param num_2: second integer
    :return: none
    """
    if num_1 > num_2:
        for num in range(num_2, num_1 + 1):
            count = 0
            print('')
            if num % 5 == 0 and num != 0 and num != 1:
                print('apple',  end=" ")
                count += 1
            if num % 7 == 0 and num != 0 and num != 1:
                print('pen',  end=" ")
                count += 1
            if '3' in str(num):
                print('pineapple')
                count += 1
            if count == 0:
                print(num)
    else:
        for num in range(num_1, num_2 + 1):
            count = 0
            print('')
            if num % 5 == 0 and num != 0 and num != 1:
                print('apple',  end=" ")
                count += 1
            if num % 7 == 0 and num != 0 and num != 1:
                print('pen',  end=" ")
                count += 1
            if '3' in str(num):
                print('pineapple')
                count += 1
            if count == 0:
                print(num)
    
        

def main():
    """
    This implements the user interface for the program.
    :param: none
    :return: none
    """
    
    num_1 = (integer_generator())
    num_2 = (integer_generator())
    print(num_1)
    print(num_2)
    check_differences(num_1, num_2)

main()
