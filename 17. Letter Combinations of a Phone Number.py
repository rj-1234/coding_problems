"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

"""
ALGO - lets take for eg - 23
empty list = result
for each digit in digits i.e 2 and 3 in 23
	current list = cur
	for each character mapped to 2 in dictionary(a list or tuple can also be used to save space) i.e. a b c in abc
		for i in result(starts with 0)
			cur.append(i + character)
		
"""

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapped_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        
        res = ['']
        
        for d in digits:
            cur = []
            print("current list : ")
            print(cur)
            for chars in mapped_digit[d]:
                print("chars : "+chars)
                for c in res:
                    cur.append(c + chars)
                    print("current list appended : ")
                    print (cur)
            res = cur
        
        return res if digits else []
       
"""
OUTPUT for 23

current list : 
[]
chars : a
current list appended : 
['a']
chars : b
current list appended : 
['a', 'b']
chars : c
current list appended : 
['a', 'b', 'c']
current list : 
[]
chars : d
current list appended : 
['ad']
current list appended : 
['ad', 'bd']
current list appended : 
['ad', 'bd', 'cd']
chars : e
current list appended : 
['ad', 'bd', 'cd', 'ae']
current list appended : 
['ad', 'bd', 'cd', 'ae', 'be']
current list appended : 
['ad', 'bd', 'cd', 'ae', 'be', 'ce']
chars : f
current list appended : 
['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af']
current list appended : 
['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf']
current list appended : 
['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
"""     