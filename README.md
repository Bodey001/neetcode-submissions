# NeetCode Submissions

My worked solutions to the NeetCode 150 roadmap, synced from [neetcode.io](https://neetcode.io) as I go.

**48 problems · 70 submissions · Python (69) and JavaScript (1)**

Working through the roadmap in order, so the coverage below is a snapshot of how far I've
gotten rather than a finished set. Arrays & Hashing through Linked List are done; Trees is
in progress (6 problems so far); everything after is not started yet.

## How to read this repo

Two things are worth knowing before you browse.

**The comments are the point.** Most solutions carry a block comment above the code
explaining the invariant the algorithm relies on, not just what the lines do. See
[trapping-rain-water](Data%20Structures%20%26%20Algorithms/trapping-rain-water/submission-0.py)
for why the shorter running max is always the safe side to resolve, or
[merge-two-sorted-linked-lists](Data%20Structures%20%26%20Algorithms/merge-two-sorted-linked-lists/submission-0.py)
for why the losing list's pointer stays put. I write these for myself, to check that I
actually understand a solution rather than having memorized its shape.

**Multiple files means multiple attempts.** Twelve problems here have more than one
submission. Usually the later file is a rework after I found a better approach, and
reading them in order shows the change:

| Problem | Attempts | What changed |
|---|---|---|
| [search-2d-matrix](Data%20Structures%20%26%20Algorithms/search-2d-matrix/) | 4 | Linear row scan then binary search within the row → one binary search over the flattened `m*n` index space, with `divmod` mapping back to `(row, col)` |
| [products-of-array-discluding-self](Data%20Structures%20%26%20Algorithms/products-of-array-discluding-self/) | 3 | O(n²) rebuild of the whole output array per element → prefix pass plus suffix pass in O(n) time, O(1) auxiliary space |
| [binary-search](Data%20Structures%20%26%20Algorithms/binary-search/) | 3 | Boundary and midpoint handling tightened across attempts |
| [two-integer-sum](Data%20Structures%20%26%20Algorithms/two-integer-sum/) | 2 | Storing the complement instead of the value, dropping one lookup per iteration |

Not every re-submission is an improvement; some are just a resubmit. And the file numbers
come from NeetCode's own submission index, so a folder that starts at `submission-2` or
`submission-5` means the earlier attempts were made before I connected GitHub sync.

## Coverage

### Arrays & Hashing (8 problems, 13 submissions)
`duplicate-integer` ×2 · `is-anagram` · `two-integer-sum` ×2 · `anagram-groups` ·
`top-k-elements-in-list` · `string-encode-and-decode` ·
`products-of-array-discluding-self` ×3 · `valid-sudoku` ×2

### Two Pointers (5 problems, 7 submissions)
`is-palindrome` · `two-integer-sum-ii` ×2 · `three-integer-sum` ×2 ·
`max-water-container` · `trapping-rain-water`

### Sliding Window (5 problems, 7 submissions)
`buy-and-sell-crypto` · `longest-substring-without-duplicates` · `permutation-string` ·
`minimum-window-with-characters` ×2 · `sliding-window-maximum` ×2

### Stack (6 problems, 6 submissions)
`validate-parentheses` · `minimum-stack` · `evaluate-reverse-polish-notation` ·
`daily-temperatures` · `car-fleet` · `largest-rectangle-in-histogram`

### Binary Search (7 problems, 15 submissions)
`binary-search` ×3 · `search-2d-matrix` ×4 · `eating-bananas` ·
`find-minimum-in-rotated-sorted-array` ×2 · `find-target-in-rotated-sorted-array` ·
`time-based-key-value-store` · `median-of-two-sorted-arrays` ×3

### Linked List (11 problems, 16 submissions)
`reverse-a-linked-list` · `merge-two-sorted-linked-lists` ×3 ·
`linked-list-cycle-detection` ×2 · `reorder-linked-list` ·
`remove-node-from-end-of-linked-list` · `copy-linked-list-with-random-pointer` ·
`add-two-numbers` · `find-duplicate-integer` ×2 · `lru-cache` ·
`merge-k-sorted-linked-lists` ×2 · `reverse-nodes-in-k-group`

### Trees (6 problems, 6 submissions)
`invert-a-binary-tree` · `depth-of-binary-tree` · `binary-tree-diameter` ·
`balanced-binary-tree` · `same-binary-tree` · `subtree-of-a-binary-tree`

## Layout

```
Data Structures & Algorithms/
  <problem-slug>/
    submission-0.py    ← attempt, numbered by NeetCode submission index
    submission-1.py
```

Solutions are written against NeetCode's editor harness, so they assume its `Solution`
class scaffold and its already-imported typing names (`List`, `Optional`). They aren't
standalone scripts and there is no test runner here; to run one, paste it back into the
problem page or supply your own harness.

## Timeline

Started 2026-05-01. Two working stretches so far: 1–26 May covering Arrays & Hashing,
Two Pointers and Stack, then 5 August onward covering Sliding Window, Binary Search,
Linked List, and now Trees. Commit dates are real submission dates, so `git log` doubles
as a record of the pace.

---

Synced automatically via NeetCode's GitHub integration. Files here are pushed by that
integration, so edits made directly in this repo can be overwritten on the next sync.
