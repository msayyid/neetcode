from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","...."
        ,"..",".---","-.-",".-..","--","-.","---",".--."
        ,"--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        my_set = set()
        for word in words:
            new_conc = ""
            for w in word:
                new_conc += alphabet[ord(w) - ord("a")]
            if new_conc not in my_set:
                my_set.add(new_conc)
        
        return len(my_set)