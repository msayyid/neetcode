from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] # bat, ba
        for i in range(1, len(strs)):
            cur_word = strs[i] # bag; bank
            for j in range(min(len(cur_word), len(prefix))): # 0 > 2
                if prefix[j] != cur_word[j]: # b == b, ba == ba, bat != bag:
                    prefix = cur_word[:j] # prefix = ba
                    break
            # if the loop finishes without finding a mismatch
            # we still need to update the prefix, as the cur_word becomes our new prefix
            if len(cur_word) < len(prefix):
                prefix = cur_word
        return prefix 