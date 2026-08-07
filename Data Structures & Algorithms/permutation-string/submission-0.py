class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Problem: Given s1 and s2 (lowercase letters only), determine whether
        # any substring of s2 is a permutation (anagram) of s1 — i.e. some
        # window of s2 has exactly the same letter counts as s1, in any order.
        #
        # Core insight: since order doesn't matter, this reduces to a
        # FIXED-SIZE sliding window over s2 (window length = len(s1)).
        # At each window we just need to know: do its 26 letter counts
        # exactly match s1's 26 letter counts?
        #
        # Instead of re-comparing all 26 counts at every step (O(26) per
        # step), we maintain a running integer `matches` = the number of
        # the 26 letters whose counts currently agree between s1 and the
        # window (most agree trivially at 0 vs 0). The window is a valid
        # permutation exactly when matches == 26.
        #
        # Each time the window slides, exactly one character leaves (left)
        # and one enters (right). For each of those single-count changes we:
        #   1. check equality BEFORE the change -> if equal, we're about to
        #      break it, so matches -= 1
        #   2. apply the +1/-1 to s2_count
        #   3. check equality AFTER the change -> if now equal, we just
        #      formed a match, so matches += 1
        # This keeps every step O(1), so the whole scan is O(n) total.
        #
        # Complexity: O(n) time, where n = max(len(s1), len(s2)) — each
        # character enters/leaves the window once, O(1) work each time.
        # O(1) space — two fixed 26-length arrays regardless of input size.

        s1_count = [0 for _ in range(26)]
        s2_count = [0 for _ in range(26)]

        if (len(s1) > len(s2)):
            return False

        fixed_window = len(s1) - 1
        base = ord("a")
        matches = 0

        # initialise: build counts for s1 and the first window of s2,
        # then count how many of the 26 letters already agree
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - base] += 1
            s2_count[ord(s2[i]) - base] += 1

        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0

        for r in range(fixed_window + 1, len(s2)):
            l = r - fixed_window

            if matches == 26:
                break

            # removing (l - 1): the character sliding out of the window
            count_index = ord(s2[l-1]) - base
            matches -= 1 if s1_count[count_index] == s2_count[count_index] else 0
            s2_count[count_index] -= 1
            matches += 1 if s1_count[count_index] == s2_count[count_index] else 0

            # adding (r): the character sliding into the window
            count_index = ord(s2[r]) - base
            matches -= 1 if s1_count[count_index] == s2_count[count_index] else 0
            s2_count[count_index] += 1
            matches += 1 if s1_count[count_index] == s2_count[count_index] else 0

        return matches == 26