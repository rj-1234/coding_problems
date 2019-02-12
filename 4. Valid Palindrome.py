"""
4. Valid Palindrome

Question:
Given a string, determine if it is a palindrome, considering only alphanumeric characters
and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
Example Questions Candidate Might Ask:
Q: What about an empty string? Is it a valid palindrome?
A: For the purpose of this problem, we define empty string as valid palindrome.
"""

import re

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        x = s.lower()
        x = re.sub('[^a-z0-9]+' , "", x)
        j = len(x) - 1
        print (x)
        while i <= j:
            for k in range(len(x)):
                if x[i] == x[j]:
                    i += 1
                    j -= 1
                else:
                    return False
        
        return True