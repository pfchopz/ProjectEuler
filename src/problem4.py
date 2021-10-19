#!/usr/bin/env python3
from time import time
from math import floor

def main():
    # Record start time
    startTime = time()
    
    # Calculate and print largest palindrome
    largestPal = largestPalindrome(999)
    print(f'The largest Palindrome is {largestPal}')

    # Record end time, print total run time
    endTime = time()
    print(f'Runtime of the program is {endTime - startTime}')

def isPalindrome(number):
    # Declare local variables
    originalNumber = number
    digit = 0
    reverse = 0

    # Loop every digit of number and create a reverse of it
    while number > 0:
        digit = number % 10
        reverse = (reverse * 10) + digit
        number = floor(number / 10)

    # Compare reversed number to orignal
    if reverse == originalNumber:
        return True
    else:
        return False

def largestPalindrome(num):
    # Declare initial locals
    num1 = num
    num2 = num
    largestPal = 0

    for i in range(num1, 0, -1):
        for j in range(num2, 0 , -1):
            temp = i * j
            if isPalindrome(temp):
                # print(f'{i} * {j} = {temp}')
                if temp > largestPal:
                    largestPal = temp
                break

    return largestPal

if __name__ == '__main__':
    main()