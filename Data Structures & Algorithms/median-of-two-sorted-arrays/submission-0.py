class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        =======================================================================
        SOLUTION STRATEGY: BINARY SEARCH ON THE PARTITION
        =======================================================================
        If the merged array existed, it would split into a left half and a
        right half at the median. Let half = (m + n + 1) // 2 be the size of
        the left half (the "+1" makes odd and even totals behave uniformly).

        That split point in the merged array corresponds to some index i in
        nums1 and index j in nums2, where i + j = half. Guessing i fully
        determines j = half - i, so instead of searching over both arrays,
        we binary search over i alone — searching over the SMALLER array
        keeps the search range (and therefore the log factor) as small as
        possible.

        For a candidate i (and derived j), define the four values sitting at
        the edges of the proposed left/right split:

            Aleft  = nums1[i-1]   (or -inf if i == 0: nothing taken from nums1)
            Aright = nums1[i]     (or +inf if i == m: nothing left in nums1)
            Bleft  = nums2[j-1]   (or -inf if j == 0)
            Bright = nums2[j]     (or +inf if j == n)

        The partition is valid exactly when:

            Aleft <= Bright   AND   Bleft <= Aright

        Because each array is individually sorted, checking just these four
        boundary values is enough to guarantee every element in the combined
        left partition is <= every element in the combined right partition —
        we don't need to compare every pair.

        - If Bleft > Aright: we've taken too little from nums1's left side,
          so we need a bigger i -> move low up.
        - If Aleft > Bright: we've taken too much from nums1's left side,
          so we need a smaller i -> move high down.

        As i increases, Aleft only increases and Bleft only decreases, so
        these failure conditions move monotonically — which is exactly what
        makes binary search valid here.

        Once a valid partition is found:
        - If (m + n) is odd, the left partition has exactly one more element
          than the right, so the median is max(Aleft, Bleft).
        - If (m + n) is even, the median is the average of the largest
          element on the left and the smallest element on the right:
          (max(Aleft, Bleft) + min(Aright, Bright)) / 2.

        COMPLEXITY:
        - Time Complexity: O(log(min(m, n))). Binary search runs over the
          smaller array's index range [0, m].
        - Space Complexity: O(1). Only a constant number of pointers/values
          are tracked; no extra data structures are built.
        """

        # Ensure nums1 is the smaller array so the binary search range is minimal
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2

        # iterate through the smaller array (nums1)
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = half - i

            Aleft = float("-inf") if i == 0 else nums1[i-1]
            Aright = float("inf") if i == m else nums1[i]
            Bleft = float("-inf") if j == 0 else nums2[j-1]
            Bright = float("inf") if j == n else nums2[j]

            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            elif Aleft > Bright:
                high = i - 1
            else:
                low = i + 1