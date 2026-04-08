from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            min_length = min(len(prefix), len(strs[i]))
            cur_check = strs[i]
            for j in range(min_length):
                if prefix[j] != cur_check[j]:
                    prefix = prefix[:j]
                    break
            if len(prefix) > len(cur_check):
                prefix = cur_check
        return prefix



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]