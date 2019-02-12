"""
18. Plus One

Question:
Given a number represented as an array of digits, plus one to the number.
Example Questions Candidate Might Ask:
Q: Could the number be negative?
A: No. Assume it is a non-negative number.
Q: How are the digits ordered in the list? For example, is the number 12 represented by [1,2] or
[2,1]?
A: The digits are stored such that the most significant digit is at the head of the list.
Q: Could the number contain leading zeros, such as [0,0,1]?
A: No
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1 
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits