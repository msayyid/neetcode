from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = dict()
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        print(counter)

        for val in counter.values():
            if val > 1:
                return True

        return False
    

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = dict()
        for n in nums:
            if n in counter:
                return True
            counter[n] = counter.get(n, 0) + 1
        return False
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = set()
        for n in nums:
            if n in counter:
                return True
            counter.add(n)
        return False
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)