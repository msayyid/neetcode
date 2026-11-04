# # Final State of Switches

# Medium–Hard (estimated)

# Array · Range Operations

# ## Problem Description

# Imagine an infinite row of switches, numbered starting from `1`. Initially, every switch is OFF.

# You are given a 2D integer array `operations`, where `operations[i] = [l, r]` 
# represents an operation that flips the state of every switch from index `l` to index `r`, inclusive.

# Flipping a switch means:

# - If the switch is OFF, it becomes ON.
# - If the switch is ON, it becomes OFF.

# After applying all operations, return the sum of the indices of every switch that is ON.

# You must process all operations. A switch may be flipped multiple times.

# ## Example 1

# Input:

# ```
# operations = [[1, 3], [2, 4]]
# ```

# Output:

# ```
# 5
# ```

# Explanation:

# Initially, all switches are OFF.

# Initially

# Step 1 of 3

# Switch 1

# OFF

# Switch 2

# OFF

# Switch 3

# OFF

# Switch 4

# OFF

# &#x20;Previous

# Sum of ON indices: 0

# Next&#x20;

# After both operations, switches `1` and `4` are ON.

# Therefore:

# \\[ 1+4=\boxed{5} \\]

# ## Example 2

# Input:

# ```
# operations = [[1, 1]]
# ```

# Output:

# ```
# 1
# ```

# Explanation: Only switch `1` is flipped, so the sum is `1`.

# ## Example 3

# Input:

# ```
# operations = [[2, 5], [2, 5]]
# ```

# Output:

# ```
# 0
# ```

# Explanation: Switches `2`, `3`, `4`, and `5` are flipped twice, returning all of them to OFF.

# ## Example 4

# Input:

# ```
# operations = [[1, 5], [3, 7]]
# ```

# Output:

# ```
# 18
# ```

# Explanation: Switches `1`, `2`, `6`, and `7` remain ON.

# Their sum is `1 + 2 + 6 + 7 = 16`.

# Correction: The output for Example 4 is 16.

# ## Constraints

# These are reconstructed practice constraints, not confirmed original Wise limits.

# - \\(1 \leq \text{operations.length} \leq 10^5\\)
# - `operations[i].length == 2`
# - \\(1 \leq l \leq r \leq 10^9\\)
# - The result may be larger than a 32-bit integer.

# ## Function Signature

# ```
# def finalStateOfSwitches(operations: list[list[int]]) -> int:    # Your implementation
# ```

# ## Your task

# Implement `finalStateOfSwitches` to return the sum of all ON switch indices after performing every operation.

# Follow-up: Can you solve the problem efficiently even when the interval endpoints are as large as \\(10^9\\)?

# I won't provide hints or the algorithm yet. Try your own approach first, 
# then send me your code and I'll review its correctness, edge cases, 
# and time complexity—just like we've been doing with your other LeetCode problems.


def finalStateOfSwitches(operations: list[list[int]]) -> int:

    # find the last switch that any operation touches
    max_r = max(r for l, r in operations)

    flips = [0] * (max_r + 2)

    # mark where each operation starts and ends
    for l, r in operations:
        flips[l] += 1 # this means one more operation starts affecting switches here
        flips[r + 1] -= 1 # means one operation stops affecting switches here

    total = 0
    active_flips = 0

    # calculate the number of flips affecting each switch
    for i in range(1, max_r + 1):
        # take the number of operations that were affecting us, and add any operations 
        # that start or stop at this position
        active_flips += flips[i]

        # odd flips = ON
        if active_flips % 2 == 1:
            total += i

    return total

    # max_r = max(r for [l, r] in operations)

    # total = 0
    # my_map = {}
    # for i in range(1, max_r + 1):
    #     my_map[i] = False
    # for start, end in operations:
    #     for i in range(start, end + 1):
    #         if my_map[i] == False:
    #             my_map[i] = True
    #         else:
    #             my_map[i] = False

    # for key, val in my_map.items():
    #     if val is True:
    #         total += key
    # return total

test_cases = [
    ([[1, 3], [2, 4]], 5),
    ([[1, 1]], 1),
    ([[2, 5], [2, 5]], 0),
    ([[1, 5], [3, 7]], 16),
    ([[1, 2], [5, 6]], 14),
    ([[1, 5], [2, 4]], 6),
    ([[1, 5], [2, 4], [3, 3]], 9),
    ([[1, 3], [3, 5]], 12),
    ([[1, 3], [1, 3], [1, 3]], 6),
    ([[2, 2], [4, 4], [2, 4]], 3),
    ([[5, 10], [1, 3], [3, 7]], 34),
    ([[1000000, 1000000]], 1000000)
    # ([[1, 1000000000], [1, 1000000000]], 0),
    # ([[1, 1000000000]], 500000000500000000),
]

for i, (operations, expected) in enumerate(test_cases, 1):
    result = finalStateOfSwitches(operations)

    status = "PASS" if result == expected else "FAIL"

    print(
        f"Test {i}: {status} | "
        f"Expected: {expected}, Got: {result}"
    )