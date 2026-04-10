class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # freq = {}
        max_length = 0
        for i in range(len(s)):
            char_set = set()
            for j in range(i, len(s)):
                if s[j] in char_set:
                    break
                char_set.add(s[j])
            max_length = max(max_length, len(char_set))
        return max_length
# On^2 time and Om space


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_length = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length

# set On time Om space


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = dict()
        l = 0
        max_length = 0
        for r in range(len(s)):
            if s[r] in char_index:
                l = max(l, char_index[s[r]] + 1)

            char_index[s[r]] = r
            max_length = max(max_length, r - l + 1)

        return max_length
