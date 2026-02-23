def longestCommonPrefix(strs) -> str:
    prefix = strs[0]
    for i in range(1, len(strs)):
        for j in range(min(len(prefix), len(strs[i]))):
            
            if prefix[j] == strs[i][j]:
                # print(prefix[j], strs[i][j])
                
                continue
            else: 
                prefix = strs[i][:j]
                break
        if len(strs[i]) < len(prefix):
            prefix = strs[i]
                
    return prefix
                
                
            

strs = ["bat","bag","bank","band"]
result = longestCommonPrefix(strs)
print(result)

strs = ["neet","neetst"]
result = longestCommonPrefix(strs)
print(result)

# My approach: Take the first word as the starting prefix, then loop through every other word comparing character 
# by character using the index j. If characters match, continue. If they don't, 
# update the prefix to the current word up to (not including) position j and break.

# Mistakes I made:

# Used == instead of = for assignment (comparison vs assignment bug)
# Had the wrong slice — used [:j+1] instead of [:j] since j is where the mismatch happened, 
# so we don't include it
# Only ran the inner loop when lengths were different — should always run it, 
# just loop until min(len(prefix), len(strs[i]))
# Forgot the edge case: when the current word is shorter than the prefix and all characters match, 
# the loop ends without a break and prefix never updates — fixed by adding if len(strs[i]) < len(prefix): prefix = strs[i] after the inner loop

# New things I learned:

# break only exits the inner loop, code after it (but still in the outer loop) still runs
# min() on two integers is O(1)
# When two variables represent different things (number of strings vs length of strings), 
# use separate names like n and m — saying O(n²) would wrongly imply they're the same

# Complexities:

# Time: O(n * m) — n = number of strings, m = length of strings. Optimal because you must check every character at least once.
# Space: O(m) — only storing the prefix, which is at most the length of a string