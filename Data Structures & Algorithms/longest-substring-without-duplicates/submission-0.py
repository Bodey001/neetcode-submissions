class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Problem: find the length of the longest substring of s that contains
        # no repeating characters.
        #
        # Approach: sliding window with two pointers, l (left) and r (right),
        # plus a set that tracks which characters are currently inside the
        # window [l, r]. We expand the window by moving r forward one step at
        # a time. If s[r] is already in the set, the window currently contains
        # a duplicate, so we shrink from the left -- removing s[l] from the
        # set and advancing l -- repeating only until that specific duplicate
        # is gone (not clearing the whole window, since characters between the
        # old duplicate and l may still be valid to keep). Once the window is
        # guaranteed duplicate-free, we add s[r] and update the best length
        # seen so far using r - l + 1.
        if len(s) == 0:
            return 0

        seen = set()
        max_substring = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_substring = max(max_substring, r - l + 1)

        return max_substring