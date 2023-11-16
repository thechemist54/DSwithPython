"""
Assignment 2_2: Write a program that evaluates the numbers between 2 and n to determine if the number is a prime number. If it is, find the logarithm of the prime number. Add all logarithms of the prime numbers between 2 and n. After iterating over the values between 2 and n, print out the sum, the number n, and the ratio of these two quantities. The ratio of the sum and n should converge on the number one. Evaluate the results with multiple values for n to demonstrate this convergence.
September 17, 2023
Aaman Bhandari
"""

"""
Identify Prime Numbers: For each number i between 2 and n, check if it's prime.

Compute Logarithm of Prime Numbers: If a number is identified as prime, calculate its natural logarithm using math.log().

Sum the Logarithms: Keep a running sum of the logarithms of all identified prime numbers.

Compute the Ratio: After iterating over all numbers between 2 and n, compute the ratio of the sum of the logarithms to n.

Output: Print the sum of the logarithms, the number n, and the computed ratio.

Test with Multiple n Values: We'll evaluate the above for several values of n to observe the convergence of the ratio to 1.
"""

import math

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_logarithm_ratio(n):
    """Calculate the sum of logarithms of prime numbers between 2 and n, and their ratio with n."""
    log_sum = 0
    
    # Iterate over numbers between 2 and n
    for i in range(2, n+1):
        if is_prime(i):
            log_sum += math.log(i)
            
    # Calculate the ratio
    ratio = log_sum / n
    print(f"For n = {n}:")
    print(f"\tSum of Logarithms: {log_sum:.3f}")
    print(f"\tValue of n: {n}")
    return log_sum, ratio

# List of n values
n_values = [10, 30, 50, 100, 500, 1000, 1500, 5000, 10000]

# Running the calculations
results = []

for n in n_values:
    log_sum, ratio = prime_logarithm_ratio(n)
    results.append((n, log_sum, ratio))
    print(f"\tConvergence Ratio: {ratio:.3f}\n")
