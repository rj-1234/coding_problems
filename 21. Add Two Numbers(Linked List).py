"""
21. Add Two Numbers

Question:
You are given two linked lists representing two non-negative numbers. The digits are
stored in reverse order and each of their nodes contains a single digit. Add the two
numbers and return it as a linked list.
Input: (2  4  3) + (5  6  4)
Output: 7  0  8
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = n = ListNode(0) # dummy keeps track of head and n keeps track of values appended to the linked list
        carry = 0

        p, q = l1, l2 #because we don't want to modify the numbers
        
        while(p or q):
            x = p.val if p else 0
            y = q.val if q else 0
            digit = x + y + carry
            carry = digit / 10
            n.next = ListNode(digit % 10)
            n = n.next
            if p: 
                p = p.next
            if q:
                q = q.next
        
        if carry:
            n.next = ListNode(carry)
            
        return dummy.next