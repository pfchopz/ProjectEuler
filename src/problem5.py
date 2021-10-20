#!/usr/bin/env python3
from time import time

def main():
    # Record start time
    startTime = time()
    
    # Multiples to check, 1 to number
    number = 20

    # Find smallest multiple and print it out
    smallMul = smallestMultiple(number)
    print(f'The answer is {smallMul}')

    # Record end time, print total run time
    endTime = time()
    print(f'Runtime of the program is {endTime - startTime}')

def smallestMultiple(num):
    answer = 10
    
    # Loop until solution found
    while True:
        # Check each number 1 to num to see if it is multiple of answer
        for i in range(1, num + 1):
            if answer % i != 0:
                break
            else:
                if i == num:
                    return answer
            
        answer += 10

if __name__ == '__main__':
    main()