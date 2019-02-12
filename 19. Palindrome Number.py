"""
19. Palindrome Number

Question:
Determine whether an integer is a palindrome. Do this without extra space.
Example Questions Candidate Might Ask:
Q: Does negative integer such as –1 qualify as a palindrome?
A: For the purpose of discussion here, we define negative integers as non-palindrome.
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = str(x)
        i = 0
        j = len(y) - 1
        while i < j:
            if y[i] == y[j]:
                i += 1
                j -= 1
            else:
                return False
        return True