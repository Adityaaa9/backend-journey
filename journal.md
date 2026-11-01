## Block 2 — Python fundamentals

Wrote playground.py: types, mutability, loops, functions, collections, is/==
Gotcha that surprised me: <which of the 5>
Mutable vs immutable: list/dict/set are mutable; str/tuple/int are not

## Block 3 — Two pointers

Patterns: converging (reverse, palindrome) + slow/fast (remove duplicates)
All 3: O(n) time, O(1) space
Bug I hit: <e.g. forgot left<right guard in palindrome skip loop>
Reuse later: move-zeroes, cycle detection, sliding window

## Block 4 — Task Tracker CLI v0

Built tracker.py: add/list/done/delete, in-memory, sys.argv parsing
Design: dict per task {id,title,done}; next_id never reused; parse_id for int safety
Known limits: in-memory only (resets each run), no concurrency, no tests yet
Refactor due Day 2: wrap in TaskStore class, add functions with type hints
