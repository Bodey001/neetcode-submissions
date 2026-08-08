class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Given s, t: find the shortest substring of s containing every
        # character of t (including duplicates). Return "" if none exists.
        #
        # Insight: variable-size sliding window with two hash maps.
        # `need` = required counts from t (built once).
        # `have` = running counts of needed characters inside the current
        #          window [l, r].
        # Instead of comparing need/have char-by-char on every step, track
        # `formed`: the number of *distinct* characters whose count in
        # `have` has just reached (not exceeded) their required count in
        # `need`. The window is valid exactly when formed == required
        # (required = number of distinct chars in t, not len(t)).
        #
        # Expand r to grow the window until valid, then shrink from l
        # while it stays valid, recording the smallest valid window seen.
        #
        # Time: O(n + m), Space: O(k) -- n = len(s), m = len(t),
        # k = number of unique characters involved.

        need = {} 
        have = {}

        formed = 0

        min_length = ""

        # initialise the needed characters in need hash map.
        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0) + 1

        required = len(need)  # distinct characters needed, not len(t)


        # run through the array 
        l=0
        for r in range(len(s)):

            if s[r] in need:
                have[s[r]] = have.get(s[r], 0) + 1
                formed += 1 if have[s[r]] == need[s[r]] else 0

            while formed == required:
                if min_length == "":
                    min_length = s[l:r+1]
                else:
                    min_length = min_length if len(min_length) < r - l + 1 else s[l:r+1]

                if s[l] in need: 
                    have[s[l]] = have.get(s[l]) - 1
                    if have[s[l]] < need[s[l]]:
                        formed -= 1
                
                l+=1

        return min_length