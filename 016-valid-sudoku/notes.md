> **Valid Sudoku** — checked rows, columns, and 3x3 boxes for duplicates using sets.
>
> **First Solution:**
> - Used a single `set` for row and column, resetting them after each `i` iteration
> - For columns, used `board[j][i]` swap trick — swapping indices traverses column-wise in the same loop, no extra loop needed
> - For boxes, used `(i//3, j//3)` as a dictionary key to uniquely identify each of 9 boxes
> - Used `dict.get(key, set())` to safely retrieve a box's set, then saved it back with `boxes[loc] = check_set`
> - Handling row, column, and box independently with their own `if` checks — `continue` couldn't work because `board[i][j]` and `board[j][i]` are two different cells
>
> **Cleaner Solution:**
> - Used `defaultdict(set)` for rows, columns, and boxes — each key maps to a set of numbers seen so far
> - For rows key is `i`, columns key is `j`, boxes key is `(i//3, j//3)`
> - Single `continue` at the top for dots works now because we only ever look at one cell `board[i][j]`
> - `defaultdict` auto-creates an empty set on first access — no need for `.get()` or saving back, and no need to reset sets manually
>
> **Mistakes made:**
> - Initially `row` set was never reset between rows causing wrong results
> - Used `is not "."` instead of `!= "."` — `is` checks identity not value, always use `!=` for string comparison
> - Used `.add()` return value to reassign — `.add()` returns `None`, never do `x = set.add()`
>
> **Time:** O(81) = O(1) — fixed board size
> **Space:** O(81) = O(1) — fixed number of keys and set entries