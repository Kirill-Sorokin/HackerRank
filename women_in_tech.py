# THIS IS A CHALLENGE FOR AN INTERNSHIP POSITION I COMPLETED.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMinOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Similar to case 1 (I am doing them in an order 1~3), a step-by-step guide is added within the code for you to better understand what tasks were carried out and how it reflects within the description. Just like before, the original comments are left untouched.

def getMinOperations(arr):
    # Maximum number of bit positions to check (31 for numbers up to 10^9)
    max_bits = 31
    # Get the number of elements in the array
    n = len(arr)
    # Initialise the minimum flips counter to zero
    min_flips = 0

    # Loop through each bit position from 0 up to max_bits - 1
    for bit in range(max_bits):
        count_ones = 0  # Counter for how many elements have this bit set to 1

        # Check each element in the array
        for number in arr:
            # If this bit is set in the number, increment the count of 1s
            if number & (1 << bit):
                count_ones += 1

        # Determine the minimum flips for this bit position:
        # - Either flip all ones to zeros or all zeros to ones
        # - The min() function picks the smaller count between count_ones and (n - count_ones)
        min_flips_for_bit = min(count_ones, n - count_ones)
        # Add the minimum flips required for this bit to the total minimum flips
        min_flips += min_flips_for_bit

    # Return the total minimum number of flips calculated
    return min_flips

# Main block that runs when the script is executed
if __name__ == '__main__':
    # Open a file for writing the output using an environment variable for the file path
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of elements in the array
    arr_count = int(input().strip())
    arr = []  # Initialise the array

    # Read each element and add it to the array
    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    # Call the function and get the result
    result = getMinOperations(arr)

    # Write the result to the file
    fptr.write(str(result) + '\n')
    # Close the file
    fptr.close()
