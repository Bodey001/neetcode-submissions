import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        PROBLEM: Valid Palindrome
        
        Given a string `s`, return true if it is a palindrome, or false otherwise.
        A string is a palindrome if, after converting all uppercase letters into 
        lowercase letters and removing all non-alphanumeric characters, it reads 
        the same forward and backward.
        
        SOLUTION STRATEGY: Two Pointers (In-Place)
        
        We place one pointer at the start (left) and one at the end (right).
        We move them toward the center. If either pointer lands on a non-alphanumeric 
        character, we skip it. Once both pointers are on valid characters, we compare 
        them (ignoring case). If they match, we move both inward.
        
        Time Complexity: O(n) - We traverse the string at most once.
        Space Complexity: O(1) - We do this entirely in-place using pointers.
        """
        
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True