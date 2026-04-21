class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        count_t = dict()
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        window = {}
        have = 0
        need = len(count_t)

        min_length = float("inf")
        result = [-1, -1]
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < min_length:
                    result = [l, r]
                    min_length = r - l + 1
                
                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1

                l += 1
        l, r = result
        return s[l : r + 1] if min_length != float("inf") else ""
            



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count_t = dict()
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        window = dict()
        have = 0 # # number of unique characters whose required frequency is satisfied
        need = len(count_t) # number of unique characters we must satisfy

        min_length = float("inf")
        result = [-1, -1] # to keep track of shortest valid window boundaries
        l = 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1 # add current character to the window and update its frequency
            
            # if this character is required and we just reached its required frequency
            # then one more character is now satisfied
            if s[r] in count_t and window[s[r]] == count_t[s[r]]: 
                have += 1 

            # shrink the window
            # window is valid (all required characters satisfied)
            # try to shrink it to find a smaller valid window
            while have == need:
                # now we know that we have the elements in window that are in count_t
                # and now we need to check if we can get shorter window
                if r - l + 1 < min_length: # # update result if current valid window is smaller
                    # update the result list
                    result = [l, r]
                    min_length = r - l + 1

                # remove leftmost character from window
                window[s[l]] -= 1

                # check whether the shrinking decrements an element of the valid windw4
                # if removing this character breaks its required frequency,
                # then the window is no longer valid, so decrease 'have'        

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1 # have is decrement if our shrinking has affected the elements which are common in t and s
                
                # move left pointer to shrink window
                l += 1
        l, r = result
        return s[l : r + 1] if min_length != float("inf") else ""