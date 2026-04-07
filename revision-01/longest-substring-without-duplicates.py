class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using map 
        # the idea is to use a map of char : last_seen index
        # if char is in chars we update the value of it(the index)
        # and shrink our window (l += 1)
        chars = dict()
        l = 0
        max_length = 0
        for r in range(len(s)):
            if s[r] in chars:
                l = max(l, chars[s[r]] + 1)
            chars[s[r]] = r
            max_length = max(max_length, r - l + 1)
        return max_length

        
        
        # l = 0
        # max_length = 0
        # chars = set()
        # for r in range(len(s)):
        #     while s[r] in chars:
        #         chars.remove(s[l])
        #         l += 1

        #     chars.add(s[r])
        #     max_length = max(max_length, r - l + 1)
        # return max_length

# # ChatGPT Notes - Longest Substring Without Repeating Characters

# ## 🔹 Problem

# Find the length of the longest substring without repeating characters.

# ---

# # ✅ Approach 1: Sliding Window + Set (Shrink)

# ## Idea

# * Maintain a window using a set
# * If duplicate appears → shrink window step by step
# * Always keep window valid (no duplicates)

# ## Code

# ```python
# def lengthOfLongestSubstring(s: str) -> int:
#     chars = set()
#     l = 0
#     max_length = 0

#     for r in range(len(s)):
#         while s[r] in chars:
#             chars.remove(s[l])
#             l += 1

#         chars.add(s[r])
#         max_length = max(max_length, r - l + 1)

#     return max_length
# ```

# ## Key Insight

# * Use `while`, NOT `if`
# * Keep removing until window is valid

# ## Mistake I Made

# * Used `if` instead of `while`
#   → caused inconsistent window → KeyError

# ## Mental Model

# * Expand right
# * Shrink left until valid
# * Window always contains unique chars

# ---

# # ✅ Approach 2: Sliding Window + HashMap (Jump)

# ## Idea

# * Store last seen index of each character
# * When duplicate found → jump `l` forward

# ## Code

# ```python
# def lengthOfLongestSubstring(s: str) -> int:
#     char_index = {}
#     l = 0
#     max_length = 0

#     for r in range(len(s)):
#         if s[r] in char_index:
#             l = max(l, char_index[s[r]] + 1)

#         char_index[s[r]] = r
#         max_length = max(max_length, r - l + 1)

#     return max_length
# ```

# ---

# ## 🔑 Key Concepts

# ### 1. Why `+1`?

# * Previous duplicate is invalid
# * Must move past it

# Example:

# ```
# abba
#    ↑ duplicate b
# last seen = 1 → l = 2
# ```

# ---

# ### 2. Why `max(l, ...)`?

# * Prevents moving `l` backwards

# Example:

# ```
# tmmzuxt
# ```

# Without `max` → window breaks

# ---

# ## 🔍 Dry Run (abba)

# ```
# s = "abba"

# r = 0 → a
# map = {a:0}
# l = 0 → len = 1

# r = 1 → b
# map = {a:0, b:1}
# l = 0 → len = 2

# r = 2 → b (duplicate)
# l = max(0, 1+1) = 2
# map = {a:0, b:2}
# len = 1

# r = 3 → a (duplicate)
# l = max(2, 0+1) = 2
# map = {a:3, b:2}
# window = "ba"
# len = 2
# ```

# ---

# ## ❗ Important Clarification (My Confusion)

# I thought:

# > “we are starting a new substring”

# Correct understanding:

# > We are adjusting the window to keep it valid

# * `l` is NOT a restart
# * `l` is just the left boundary

# ---

# ## 🧠 Comparison

# | Approach | Strategy            | Difficulty |
# | -------- | ------------------- | ---------- |
# | Set      | Shrink step-by-step | Easy       |
# | HashMap  | Jump directly       | Medium     |

# ---

# ## 🔥 Final Takeaways

# * Always keep window valid
# * Set → shrink with `while`
# * HashMap → jump with `l = max(l, last_seen + 1)`
# * `+1` → skip duplicate
# * `max` → prevent going backwards

# ---

# ## 🧠 One-line Summary

# > Set = shrink, HashMap = jump
