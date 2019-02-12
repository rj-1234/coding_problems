"""
22. Swap Nodes in Pairs

Question:
Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1  2  3  4, you should return the list as 2  1  4  3.
Your algorithm should use only constant space. You may not modify the values in the
list, only nodes itself can be changed.
Example Questions Candidate Might Ask:
Q: What if the number of nodes in the linked list has only odd number of nodes?
A: The last node should not be swapped.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# https://www.youtube.com/watch?v=HuBxD8pWpJ0
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # print(head.val)
        dummy = curr = ListNode(0)
        dummy.next = head
        
        while head and head.next:
            p = head.next.next
            curr.next = head.next
            curr.next.next = head
            head.next = p
            curr = head
            head = p
        
        return dummy.next