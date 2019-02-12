"""
17. Reverse Integer

Question:
Reverse digits of an integer. For example: x = 123, return 321.
Example Questions Candidate Might Ask:
Q: What about negative integers?
A: For input x = –123, you should return –321.
Q: What if the integer’s last digit is 0? For example, x = 10, 100, …
A: Ignore the leading 0 digits of the reversed integer. 10 and 100 are both reversed as 1.
Q: What if the reversed integer overflows? For example, input x = 1000000003.
A: In this case, your function should return 0.
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = 0
        y = abs(x)
        while y > 0:
            reverse = reverse * 10 + y % 10
            y = y // 10
        ans = -reverse if x < 0 else reverse
        if reverse >= (2**31 -1) or reverse <= (-2**31):
            return 0
        return ans