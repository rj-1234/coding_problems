
"""
13. Longest Palindromic Substring

Question:
Given a string S, find the longest palindromic substring in S. You may assume that the
maximum length of S is 1000, and there exists one unique longest palindromic substring.

Hint:
First, make sure you understand what a palindrome means. A palindrome is a string
which reads the same in both directions. For example, “aba” is a palindome, “abc” is not.

A common mistake:
Some people will be tempted to come up with a quick solution, which is unfortunately
flawed (however can be corrected easily):
Reverse S and become S’. Find the longest common substring between S and S’,
which must also be the longest palindromic substring.
This seemed to work, let’s see some examples below.
For example, S = “caba”, S’ = “abac”.
The longest common substring between S and S’ is “aba”, which is the answer.
Let’s try another example: S = “abacdfgdcaba”, S’ = “abacdgfdcaba”.
The longest common substring between S and S’ is “abacd”. Clearly, this is not a valid
palindrome.
We could see that the longest common substring method fails when there exists a
reversed copy of a non-palindromic substring in some other part of S. To rectify this,
each time we find a longest common substring candidate, we check if the substring’s
indices are the same as the reversed substring’s original indices. If it is, then we attempt
to update the longest palindrome found so far; if not, we skip this and find the next
candidate.

"""

"""
ALGO :

for each character start from the middle and go out until the string is not a palindrome : isplaindrome() does this
record and compare from previous largest palindrome substring : res stores this
return the largest at the end. : res
"""
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            # for odd cases such as a, aba, ababa
            l = self.ispalindrome(s, i, i)
            # print("odd : "+l)
            if len(l) > len(res):
                res = l
            
            #for even cases such as aa, abba, abbaabba
            l = self.ispalindrome(s, i, i+1)
            # print("even : "+l)
            if len(l) > len(res):
                res = l
        return res
                
    def ispalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # print(str(l)+" : "+str(r))
            # print(s[l], s[r])
            l -= 1
            r += 1
        return s[l+1:r]
