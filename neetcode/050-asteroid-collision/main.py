from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0: # if left moving a is bigger, then our top is destroyed
                    stack.pop()
                elif diff > 0:
                    a = 0 # our current a is destroyed because our top was bigger
                else: # if diff == 0, both are destroyed
                    stack.pop()
                    a = 0

            if a: # if a is not destroyed (a was bigger or a didnt go to whiel and didn't change) - i need a better wording in here
                stack.append(a)
        return stack
    


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff > 0:
                    a = 0
                elif diff < 0:
                    stack.pop()
                else:
                    a = 0
                    stack.pop()
                
            if a:
                stack.append(a)
        return stack
    

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # a collision is only possible when:
            # previous asteroid moves right (+) and current moves left (-)
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff > 0:
                    # stack top is bigger, so a is gone
                    a = 0
                elif diff < 0:
                    # a is bigger, top of stack is gone
                    stack.pop()
                else:
                    # both are destroyed
                    a = 0
                    stack.pop()
            # if current asteroid survives all possible collisions, keep it
            if a:
                stack.append(a)
        return stack