#!/usr/bin/env python3
from time import time
from math import sqrt
from sys import setrecursionlimit
import threading


def main():
    # Record start time
    startTime = time()

    # Set starting number
    number = 600851475143

    # Print largest prime factor
    print(largestPrimeFactor(number))

    # Record end time, print total run time
    endTime = time()
    print(f'Runtime of the program is {endTime - startTime}')

# Function to check for factors
def isFactor(number, temp):
    if number % temp == 0:
        return True    
    else:
        return False

# Function to check for primes
def isPrime(number, temp = 2):
    # Checking if prime
    if temp == number:
        return True
    elif number % temp == 0:
        return False

    # Last call before crashing in Windows
    if temp == 1405:
        pass
    
    # Recursion until all integars are checked
    return isPrime(number, temp + 1)

# Function to find largest prime factor
def largestPrimeFactor(number):
    # Set start point for factor checking
    temp = round(sqrt(number))

    # Check for prime factors by counting down
    while temp > 0:
        if isFactor(number, temp):
            print(f'Checking if {temp} is prime.')
            if isPrime(temp):
                print ('Is Prime!')
                return temp
        
        # Decrement temp by 1
        temp -= 1
    
    # Return 0 if no prime factor was found
    return 0

if __name__ == '__main__':
    # Increase recurssion limit and thread stack size to facilitate large number
    setrecursionlimit(800000)
    threading.stack_size(0x2000000)

    # Run main() in custom thread with large stack size
    t = threading.Thread(target=main())
    t.start()
    t.join()