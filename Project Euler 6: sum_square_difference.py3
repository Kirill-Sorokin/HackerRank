def sum_square_difference(n):
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    square_of_sum = (n * (n + 1) // 2) ** 2
    return square_of_sum - sum_of_squares

# Read number of test cases
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(sum_square_difference(n))
