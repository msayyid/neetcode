class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_word = dict()
        word_to_pattern = dict()
        s = s.split()
        if len(s) != len(pattern):
            return False

        for i in range(len(s)):
            if pattern[i] not in pattern_to_word:
                pattern_to_word[pattern[i]] = s[i]
            else:
                if pattern_to_word[pattern[i]] != s[i]:
                    return False
            if s[i] not in word_to_pattern:
                word_to_pattern[s[i]] = pattern[i]
            else:
                if word_to_pattern[s[i]] != pattern[i]:
                    return False

        return True
    

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_word = dict()
        word_to_pattern = dict()
        s = s.split()
        if len(s) != len(pattern):
            return False

        for i in range(len(s)):
            if pattern[i] in pattern_to_word and pattern_to_word[pattern[i]] != s[i]:
                return False
            pattern_to_word[pattern[i]] = s[i]

            if s[i] in word_to_pattern and word_to_pattern[s[i]] != pattern[i]:
                return False
            word_to_pattern[s[i]] = pattern[i]
            

        return True