"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

"""
https://www.youtube.com/watch?v=LxwiwlUDOk4		
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        
        return self.helper("", n, 0)
    
    def helper(self, cur, open_available, unclosed):
    	# base case when all available open parents have been used
        if open_available == 0:						
            return [cur + ")" * unclosed]
        # when there are no unclosed parent present
        elif (unclosed == 0):
            return self.helper(cur + "(", open_available - 1, unclosed + 1)
        # when there are both i.e available parents > 0 and some parents are still unclosed
        return self.helper(cur + "(", open_available - 1, unclosed + 1) + self.helper(cur + ")", open_available, unclosed - 1)