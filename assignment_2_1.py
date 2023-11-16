"""
Assignment 2_1: Write a program that will find the 450th prime number. After every 50 prime numbers in the search for the 450th, print the number of prime numbers found up to that point to the console. Include an explanation of what the iteration means (i.e., 150 prime numbers found so far). When you have identified the 450th prime number, print a statement to the console that indicates what this program was looking for and the solution.
September 17, 2023
Aaman Bhandari
"""

"""
EXPLANATION:
Initialize Necessary Variables:


Start with a list containing just the prime number 2 since it's the only even prime number.

Initialize a counter to keep track of the number of prime numbers found. Set it to 1 since we already have 2 in our list.

Start with the first odd number, 3, and test for primality.


Check for Primality:


To check if a number n is prime, we need to ensure that it's not divisible by any prime number less than or equal to the square root of n. This is because if n is divisible by some number greater than its square root, then it must also be divisible by a number smaller than its square root. For example, if n is divisible by 10 (which is greater than the square root of numbers up to 100), then n must also be divisible by 2, which is less than the square root of 100.

Use the modulo operation to check for divisibility.


Track the Count:

Every time we find a prime number, we'll increment our counter.

If the counter is a multiple of 50 (i.e., 50, 100, 150, etc.), we'll print a message to the console indicating how many prime numbers we've found so far.


End Condition:

We'll continue our search until our counter reaches 450. At that point, we'll print the 450th prime number and end the search.
"""

def find_nth_prime(n):
    # Step 1: Initialize necessary variables
    primes = [2]
    count = 1
    number = 3

    while count < n:
        is_prime = True
        
        # Step 2: Check for primality
        for prime in primes:
            if prime * prime > number:  # No need to check further, the number is prime
                break
            if number % prime == 0:     # The number is divisible by another prime
                is_prime = False
                break
        
        if is_prime:
            primes.append(number)
            count += 1
            
            # Step 3: Track the count
            if count % 50 == 0:
                print(f"{count} prime numbers found so far. The {count}th prime number is:", primes[-1])
        
        # Move on to the next odd number
        number += 2

    # Step 4: End Condition
    return primes[-1]

# Find the 450th prime number
nth_prime = find_nth_prime(450)
print("The 450th prime number is:",nth_prime)
