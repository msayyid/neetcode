from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        my_string = ""
        if strs:
            for i in range(len(strs)):
                my_string += str(len(strs[i]))
                my_string += "#"
                my_string += strs[i]
            return my_string
        return my_string

    def decode(self, s: str) -> List[str]:
        my_list = []
        temp_str = ""
        # num_rep = ""
        ptr = 0
        start = 0
        if s:
            while ptr <= len(s)-1:
                if s[ptr] == "#":
                    num_rep = int(s[start:ptr])
                    print(num_rep)
                    temp_str = s[ptr+1:ptr+num_rep+1]
                    my_list.append(temp_str)
                    ptr += num_rep + 1
                    start = ptr

                    print(ptr)
                else: 
                    ptr += 1
            return my_list

        return my_list


