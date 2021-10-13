#!/usr/bin/env python3
from time import time

def main():
    # Record start time
    startTime = time()
    
    # Declare initial variables
    sumTotal = 2
    beforeLastNum = 1
    lastNum = 2

    # Loop until break
    while True:
        # Find next Fibonacci number
        num = lastNum + beforeLastNum

        # Check if number exceeds 4 million or is even
        if num > 4000000:
            break
        elif num % 2 == 0:
            sumTotal += num   # Add to sum if even
        
        # resest last numbers for next calculation
        beforeLastNum = lastNum
        lastNum = num

    # print result
    print(sumTotal)

    # Record end time, print total run time
    endTime = time()
    print(f'Runtime of the program is {endTime - startTime}')

if __name__ == '__main__':
    main()