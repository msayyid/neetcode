from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        # the idea is to encode using the length of a string in a list
        # with a symbol, which we do not add to the actual word when decoding
        # i will use length + # + str
        # full_string = ""
        return "".join(f"{len(s)}#{s}" for s in strs)
        # for s in strs:


        #     full_string += str(len(s))
        #     "#".join(s)
        #     # full_string += "#"
        #     # full_string += s
        # return full_string



    def decode(self, s: str) -> List[str]:
        result = []
        # when decoding, we extract the numbers up to #
        # typecast it, and run this number of times to jump and to build the string
        ptr = 0
        start = 0
        while ptr < len(s):
            if s[ptr] == "#":
                number_rep = int(s[start:ptr])
                # temp_str = 
                result.append(s[ptr+1:ptr+number_rep+1])
                ptr += number_rep + 1
                start = ptr
            else: 
                ptr += 1
        return result
        



# Encode/Decode Strings
# Idea: encode each string as len(s)#s. The # acts as a delimiter and the length tells the 
# decoder exactly how many characters to grab, avoiding ambiguity with any character including # itself.

# Decode: extract digits up to #, cast to int, jump pointer by that amount and slice. 

# Pointer jumping avoids O(N²) — we never re-scan characters.
# Mistake: += string concatenation is O(M) per operation because Python strings are 
# immutable — each += copies the whole string. Use "".join(...) instead, which pre-allocates memory. 
# Same Big O but much faster in practice.

# join syntax: "separator".join(iterable) — separator goes outside, items go inside. 
# For no separator: "".join(f"{len(s)}#{s}" for s in strs)
# Time: O(N + M) — N = number of strings, M = total characters. M alone isn't enough 
# because N can exceed M (e.g. 100 empty strings).
# Space: O(M) — result and full_string both scale with total characters. ptr, start, number_rep are O(1).