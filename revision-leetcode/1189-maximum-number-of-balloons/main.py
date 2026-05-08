class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        for c in text:
            count[c] = count.get(c, 0) + 1

        b = count.get("b", 0)
        a = count.get("a", 0)
        l = count.get("l", 0) // 2 # how many pairs of l s do i have since only 2 ls can make up one balloon
        o = count.get("o", 0) // 2
        n = count.get("n", 0) 
        return min(b, a, l, o, n)