class MyHashSet:

    def __init__(self):
        self.my_set = [False] * 1000001
        

    def add(self, key: int) -> None:
        self.my_set[key] = True

    def remove(self, key: int) -> None:
        self.my_set[key] = False
        

    def contains(self, key: int) -> bool:
        return self.my_set[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Design HashSet — Notes
# The idea:
# A hashset gives constant time lookup by using a hash function to map a value to a specific place (index) in memory (an array).
# This problem's trick:
# Because keys are bounded between 0 and 1,000,000, the key itself IS the index — no real hashing needed. 

# So we just allocate a boolean array of size 1,000,001 initialized to False.
# Operations:

# add(key) → set self.my_set[key] = True
# remove(key) → set self.my_set[key] = False
# contains(key) → return self.my_set[key]

# Mistakes I made:

# Forgot to use self. when initializing my_set inside __init__, making it a local variable inaccessible to other methods
# Was storing key instead of True in add — we only need to mark presence, not store the value

# Complexities:

# Time: O(1) for all operations
# Space: O(1,000,001) → essentially O(n) where n is the constraint size — always allocated regardless of how many keys are stored

# Real world limitation:
# This only works because keys are bounded integers. A real hashset would need an actual hash function and collision handling (e.g. chaining with linked lists).