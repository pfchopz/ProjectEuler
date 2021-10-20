#!/usr/bin/env python3
from time import time

def main():
    # Record start time
    startTime = time()
    
    # Print all primes up to primeCount
    primeCount = 1000000
    printPrimes(primeCount)

    # Record end time, print total run time
    endTime = time()
    print(f'Runtime of the program is {endTime - startTime}')

# Primality test using trial divsion with 6k+-1 optimization
def isPrime(num):
    if num <= 3:  # Basically check if number is 2 or 3
        return num > 1
    if num % 2 == 0 or num % 3 == 0:  # Check if number is divisible by 2 or 3
        return False
    i = 5
    while i ** 2 <= num:  # Use 6k+-1 to check rest of possible divisors
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Return all primes up to limit
def printPrimes(limit):
    # Declare initial count variable
    primeCount = 1
    number = 2

    # Find and print all primes up to limit
    while primeCount <= limit:
        if isPrime(number):
            print(f'Prime {primeCount}:   {number}')
            primeCount += 1
        number += 1

if __name__ == '__main__':
    main()