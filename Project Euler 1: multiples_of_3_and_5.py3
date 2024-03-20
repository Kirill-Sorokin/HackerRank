def arithmetic_series_sum(a, d, n):
    "Return the sum of the arithmetic series starting with 'a', difference 'd', and 'n' terms."
    return n * (2 * a + (n - 1) * d) // 2

def sum_of_multiples(n):
    "Return the sum of multiples of 3 or 5 below 'n'."
    n -= 1  # Subtract 1 because we want multiples below n
    multiples_of_3 = n // 3
    multiples_of_5 = n // 5
    multiples_of_15 = n // 15
    
    sum_3 = arithmetic_series_sum(3, 3, multiples_of_3)
    sum_5 = arithmetic_series_sum(5, 5, multiples_of_5)
    sum_15 = arithmetic_series_sum(15, 15, multiples_of_15)
    
    return sum_3 + sum_5 - sum_15

# Existing code
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum_of_multiples(n))
