def largest_prime_factor(n):
    # Initialize the largest prime factor
    largest_factor = 1
    # Divide out the 2s
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    # Divide out other primes
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2
    # If n is a prime number greater than 2
    if n > 2:
        largest_factor = n
    return largest_factor

# Read the number of test cases
t = int(input().strip())

# For each test case, calculate and print the largest prime factor
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime_factor(n))
