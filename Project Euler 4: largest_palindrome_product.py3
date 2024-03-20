# Function to check if a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Function to find the largest palindrome product which is less than N
def largest_palindrome_less_than_N(N):
    max_palindrome = 0
    for i in range(100, 1000):  # Loop through 3-digit numbers
        for j in range(i, 1000):  # Loop through 3-digit numbers
            product = i * j
            if is_palindrome(product) and product < N:
                max_palindrome = max(max_palindrome, product)
    return max_palindrome

# Read the number of test cases from stdin
t = int(input().strip())

# For each test case, read N and print the largest palindrome product less than N
for _ in range(t):
    n = int(input().strip())
    print(largest_palindrome_less_than_N(n))
