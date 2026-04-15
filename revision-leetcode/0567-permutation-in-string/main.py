class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if len(s2) < k:
            return False
        count1 = [0] * 26
        for c in s1:
            count1[ord(c) - ord("a")] += 1
        
        count2 = [0] * 26
        for c in s2[:k]:
            count2[ord(c) - ord("a")] += 1

        if count1 == count2:
            return True
        
        for i in range(k, len(s2)):
            count2[ord(s2[i]) - ord("a")] += 1
            count2[ord(s2[i - k]) - ord("a")] -= 1
            if count1 == count2:
                return True
        return False

# On time O1 space


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1, count2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord("a")] += 1
            count2[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)): # we start from len(s1) because we already have the fist window
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord("a") # we have the current index to add
            count2[index] += 1 # Increase the count of the new character entering the window
            if count1[index] == count2[index]: # if now they are equal (after we have incremented our count2, our window)
                matches += 1
            elif count1[index] + 1 == count2[index]: # if they were equal before and we broke it now
                matches -= 1

            # elif count1[index] == count2[index] - 1:
            #     matches -= 1  # question : would this work as well? yes works


            index = ord(s2[l]) - ord("a")
            count2[index] -= 1
            if count1[index] == count2[index]:
                matches += 1
            elif count1[index] - 1 == count2[index]:
                matches -= 1 # same question goes in here too, would it work if we did count1[index] == count2[index] + 1?
            l += 1

        return matches == 26
        