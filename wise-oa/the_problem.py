# Maximum Array Correlation
# Medium–Hard (estimated)
# HackerRank-style coding problem

# Problem Description
# For two integer arrays a and b of equal length, 
# the array correlation is defined as the sum of all 
# values b[i] where b[i] is strictly greater than a[i].

# Given two integer arrays a and b of length n, you may rearrange the elements of 
# array b in any order to maximize the array correlation.

# Return the maximum possible array correlation value.

# Note: You are not allowed to rearrange the elements of array a.
# Example 1
# Input:
# a = [1, 2, 3, 4, 5]
# b = [3, 5, 4, 6, 2]



# Output:
# 20


# Explanation:

# Array b can be rearranged as:
# b = [2, 3, 4, 5, 6]



# Every element of b is greater than the corresponding element of a.
# Index	a[i]	b[i]	Contributes
# 0	    1	    2	    2
# 1	    2	    3	    3
# 2	    3	    4	    4
# 3	    4	    5	    5
# 4	    5	    6	    6

# The array correlation is:
# \[
# 2+3+4+5+6=20
# \]

# This is the maximum possible correlation.
# Function Signature
# def getMaxArrayCorrelation(a: list[int], b: list[int]) -> int:    # Your implementation



# Parameters:
# - a: The fixed-order integer array.
# - b: The integer array whose elements can be rearranged.
# Returns: An integer representing the maximum possible array correlation.
# Constraints
# - \(1 \le n \le 2 \times 10^5\)
# - \(1 \le a[i], b[i] \le 10^9\)
# - Both arrays have the same length.
# - Each element of b must be used exactly once.
# - An element b[i] contributes to the sum only if b[i] > a[i], not when they are equal.


def getMaxArrayCorrelation(a: list[int], b: list[int]) -> int:    
    a.sort(reverse=True)
    b.sort(reverse=True)
    i = 0
    total = 0
    # for num in b:
    bi = 0
    while bi < len(b):
        while i < len(b) and b[bi] <= a[i]:
            i += 1

        if i == len(b):
            break

        total += b[bi]
        bi += 1
        i += 1
    return total
    """
    ok what happened in here is, we sorted a and b in reverse
    and i is there to keep track of a
    and then the outer loop is there to iterate thorugh b (which we are allowed to rearrange)
    and i iterates through a, ok, inside we have the inner loop, in there we are checking
    if the condition is not met, meaning if current b is not greater than current a
    then we can just skip this i, since it is the biggest number there's, there's really no point
    in using it, so we skip the biggest useless ones, and we just add up the ones where b[bi] is greater than a[i]
    and we increment both i and bi since we have used them both
    and in case i reaches the end or gets outsdie the bounds, we break the outer loop"""

test_cases = [
    ([1, 2, 3, 4, 5], [3, 5, 4, 6, 2], 20),
    ([5], [5], 0),
    ([5], [6], 6),
    ([10], [3], 0),
    ([3, 3, 3], [4, 4, 4], 12),
    ([4, 4, 4], [2, 5, 6], 11),
    ([1, 2, 3], [2, 2, 2], 2),
    ([2, 5, 8], [3, 6, 9], 18),
    ([5, 6, 7], [1, 2, 8], 8),
    ([3, 8, 10], [4, 9, 9], 18),
    ([2, 2, 9, 9], [3, 3, 10, 10], 26),
    ([4, 7, 10], [5, 8, 100], 113),
]

for i, (a, b, expected) in enumerate(test_cases, 1):
    result = getMaxArrayCorrelation(a.copy(), b.copy())

    status = "PASS" if result == expected else "FAIL"

    print(
        f"Test {i}: {status} | "
        f"Expected: {expected}, Got: {result}"
    )
# getMaxArrayCorrelation()





def getMaxArrayCorrelation(a: list[int], b: list[int]) -> int:
    # Sort both arrays in descending order.
    # We prioritise larger values from b because we want
    # to maximise the SUM of successful matches.
    a.sort(reverse=True)
    b.sort(reverse=True)

    # i tracks the current target in a.
    # bi tracks the current value in b.
    i = 0
    bi = 0
    total = 0

    while bi < len(b):

        # If the current b cannot beat a[i], skip a[i].
        # Since b is sorted descending, all remaining b values
        # are <= b[bi], so none of them can beat this a[i].
        while i < len(a) and b[bi] <= a[i]:
            i += 1

        # No targets remain in a, so no more matches are possible.
        if i == len(a):
            break

        # Successful match: b[bi] > a[i].
        # Add this b value to our correlation sum.
        # We match it with the largest remaining a it can beat,
        # preserving smaller targets for smaller b values.
        total += b[bi]

        # Both elements are now used, so advance both pointers.
        bi += 1
        i += 1

    return total