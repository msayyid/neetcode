class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = []
        for i in range(len(word1) + len(word2)):
            if i < len(word1):
                final.append(word1[i])
            if i < len(word2):
                final.append(word2[i])
        return "".join(final)
    
# Test cases
test_cases = [
    ("abc", "pqr"),
    ("ab", "pqrs"),
    ("abcd", "pq"),
    ("a", "z"),
    ("hello", "world"),
    ("", "abc"),
    ("abc", ""),
    ("", ""),
    ("x", "yz"),
    ("longword", "hi"),
    ("ab", "abbxxc")
]

# Testing code
sol = Solution()

for idx, (word1, word2) in enumerate(test_cases, 1):
    try:
        result = sol.mergeAlternately(word1, word2)
        print(f"Test {idx}: word1={word1!r}, word2={word2!r} -> {result!r}")
    except Exception as e:
        print(f"Test {idx}: word1={word1!r}, word2={word2!r} -> ERROR: {type(e).__name__}: {e}")