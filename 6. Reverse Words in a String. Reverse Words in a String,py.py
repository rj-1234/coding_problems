"""
6. Reverse Words in a String

Question:
Given an input string s, reverse the string word by word.
For example, given s = "the sky is blue", return "blue is sky the".
Example Questions Candidate Might Ask:
Q: What constitutes a word?
A: A sequence of non-space characters constitutes a word.
Q: Does tab or newline character count as space characters?
A: Assume the input does not contain any tabs or newline characters.
Q: Could the input string contain leading or trailing spaces?
A: Yes. However, your reversed string should not contain leading or trailing spaces.
Q: How about multiple spaces between two words?
A: Reduce them to a single space in the reversed string.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.strip().split()[::-1])
        


# rough work
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        print(" ".join(s.strip().split()[::-1]))
        # print(words)
        # for word in words:
        #     word = word[::-1]
        #     print(word+" ")

s = Solution()
s.reverseWords("the    sky is blue   ")