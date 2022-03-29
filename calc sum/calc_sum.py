# Title: Calc Sum Program
# Program created by William Schaeffer
# CPS 313
# P. 627, Exercise 6, Calc Sum Program
# 03.15.22

# This program will test a recursive function that adds all integers up to and including inputted integer

# import for function

import sys

# functions

def recursive(num):

    if num == 1:                                                # base case
        return num
    else:
        return num + recursive(num - 1)                         # general case will reduce num until base case is met

# Main Function

def main():
   
    #number = int(input('Please enter an integer: '))            # for testing
    number = int(sys.argv[1])                                   # for input via command prompt
    print(f'Passing {number} to recursive function now.')

    print(f'The sum of all the integers leading up to and including {number} is {recursive(number)}')


if __name__ == '__main__':
    main()                                                      # call main function


