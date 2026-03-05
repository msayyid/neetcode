**Encode & Decode Strings**

*The idea:* Encode each string as `length#string` (e.g. `"Hello"` → `"5#Hello"`). This avoids any delimiter ambiguity because we never *search* for a boundary inside the string — we just jump exactly `length` characters forward.

*Why my first approach failed:* Using `|` as a delimiter breaks when `|` appears inside a string. Even a word like `"DELIMITER"` could appear. Any character-search-based approach is fundamentally fragile.

*Why `#` after the length is safe:* `#` is only used to find where the **number ends**, not where the string ends. Numbers never contain `#`, so this boundary is always reliable.

*Decode approach:* Used two pointers — `ptr` to scan forward and `start` to track where the current length number begins. When hitting `#`, slice `s[start:ptr]` for the number, then grab exactly `num_rep` characters after it. Critical: update `start = ptr` **after** moving `ptr`, not before.

*Mistakes made:* Slicing from index 0 every time instead of tracking `start`. Setting `start = ptr + 1` before updating `ptr` (wrong order). While condition `ptr <= len(s)` causes index error — must be `ptr <= len(s)-1` or equivalently `ptr < len(s)` (cleaner). The `-1` is because strings are 0-indexed, so the last valid index is `len(s)-1`.

*On slicing cost:* Slices are not O(1) but they don't make the solution O(N²) either. Because `ptr` jumps forward by exactly `num_rep` after each slice, no character is ever visited twice. The total work across all slices adds up to O(N).

*Complexities:* Time **O(N)**, Space **O(N)** — N being total characters across all strings. `temp_str` is O(1) since max string length is bounded at 200.

*Is this optimal?* Yes — since every character must be visited at least once to encode and decode correctly, O(N) time is the best possible. You cannot do better.