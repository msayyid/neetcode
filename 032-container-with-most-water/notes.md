## 📝 Container With Most Water

### Problem
Given an array of heights, find two bars that together hold the most water. Area = `min(left_height, right_height) * distance_between_them`.

### My approach journey
- Started with **brute force** — tried every pair `(i, j)`, calculated area, tracked max. Worked correctly. O(n²) time, O(1) space.
- Thought two pointers needed a sorted array — **this was wrong**. Two pointers don't always need sorting; it depends on whether there's a logical reason to eliminate one side.

### Two Pointer Idea
Start with the widest container possible (`l=0, r=end`). At each step, the area is limited by the **shorter bar**. Moving the taller pointer inward can only hurt (width shrinks, height stays bounded by the same or shorter bar). Moving the **shorter pointer** at least gives a *chance* of improvement. So always move the shorter one inward.

### Pseudocode
```
l = 0, r = last index
max_area = 0

while l < r:
    area = min(height[l], height[r]) * (r - l)
    update max_area
    if height[l] < height[r]:
        move l right
    else:
        move r left

return max_area
```

### Complexities
| | Brute Force | Two Pointer |
|---|---|---|
| Time | O(n²) | O(n) |
| Space | O(1) | O(1) |

### Key mistake / misconception
Two pointers do **not** require a sorted array. They require a logical reason to eliminate one pointer — here, the shorter bar is always the bottleneck.

