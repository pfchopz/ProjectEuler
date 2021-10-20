#!/usr/bin/env python3
from time import time

def main():
    # Record start time
    startTime = time()
    
    # Number to sum against
    number = 100

    # Calculate answer
    answer = squareOfSums(number) - sumOfSquares(number)
    print(f'The answer is {answer}')

    # Record end time, print total run time
    endTime = time()
    print(f'Runtime of the program is {endTime - startTime}')

def sumOfSquares(num):
    # Declare initial variable
    answer = 0

    # Loop all integars up to num and square then sum
    for i in range(1, num + 1):
        answer += pow(i, 2)
    
    return answer

def squareOfSums(num):
    # Declare initial variable
    answer = 0

    # Loop all integars up to num and sum then square
    for i in range(1, num + 1):
        answer += i
    answer = pow(answer, 2)

    return answer

if __name__ == '__main__':
    main()