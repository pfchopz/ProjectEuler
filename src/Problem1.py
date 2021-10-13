#!/usr/bin/env python3
from time import time

def main():
    # Record start time
    startTime = time()
    
    # Variable for sum
    sumTotal = 0

    # Loop numbers 1-1000 checking if divisible by 3 or 5
    for number in range(1,1000000000):
        if number % 3  == 0:
            sumTotal += number
        elif number % 5 == 0:
            sumTotal += number

    # Print result
    print(sumTotal)

    # Record end time, print total run time
    endTime = time()
    print(f'Runtime of the program is {endTime - startTime}')

if __name__ == '__main__':
    main()