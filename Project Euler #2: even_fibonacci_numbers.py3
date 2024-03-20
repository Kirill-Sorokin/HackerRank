def even_fib_sum(n):
    # Initialize the first two even Fibonacci numbers
    # and their sum
    a, b = 0, 2
    sum_even_fib = a + b
    
    # Calculate the next even Fibonacci numbers
    while True:
        c = 4 * b + a
        if c > n:
            break
        sum_even_fib += c
        a, b = b, c
    
    return sum_even_fib

# Read the number of test cases
t = int(input().strip())

# For each test case, calculate and print the sum
for a0 in range(t):
    n = int(input().strip())
    print(even_fib_sum(n))
