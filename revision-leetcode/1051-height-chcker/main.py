from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = 0
        # expected = sorted(heights) # O(NlogN)
        count = [0] * 100
        expected = [0] * len(heights)
        for h in heights:
            count[h - 1] += 1
        # print(count)

        i = 0
        for key in range(100):
            for _ in range(count[key]):
                expected[i] = key + 1
                i += 1
        print(expected)
        
        
        j = 0
        i = 0
        for i in range(len(heights)): # O(N)
            if heights[i] != expected[i]:
                counter += 1
        print(counter)
        return counter
    

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        mismatch = 0
        count = [0] * 100
        for h in heights:
            count[h - 1] += 1

        print(count)

        expected = []
        for i in range(0, 100):
            for _ in range(count[i]):
                expected.append(i + 1)

        print(expected)

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch += 1

        return mismatch



class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        mismatch = 0
        count = [0] * 100
        for h in heights:
            count[h - 1] += 1

        expected = []
        j = 0
        for i in range(0, 100):
            for _ in range(count[i]):
                if heights[j] != i + 1:
                    mismatch += 1
                j += 1

        return mismatch

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 100

        # step 1, create count
        for h in heights:
            count[h - 1] += 1

        mismatch = 0
        original_index = 0

        # step 2, create the sorted order one value at a time
        for expected_height in range(100):
            
            # if expected height appeared multiple times,
            # use it multiple times
            while count[expected_height] > 0:

                # compare original value with the expected sorted value
                if heights[original_index] != expected_height + 1:
                    mismatch += 1

                # move to the next original position
                original_index += 1

                # we used one copy of this height
                count[expected_height] -= 1

        return mismatch