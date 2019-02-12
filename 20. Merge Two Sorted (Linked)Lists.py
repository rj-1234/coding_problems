"""
20. Merge Two Sorted Lists

Question:
Merge two sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two lists.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def length(self, l):
        current = l
        length = 0
        while current.next != None:
            current = current.next
            length += 1
        return length + 1
    
    def append(self,val, l):
        new = ListNode(val)
        current = l
        while current.next != None:
            current = current.next
        current.next = new
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = n = ListNode(0) # n keeps track of head and dummy keeps track of values appended to the linked list
        while l1 or l2:
            if l1 and l2:
                if (l1.val <= l2.val):
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
                continue
            if l1:
                dummy.next = l1
                l1 = l1.next
                dummy = dummy.next
                continue
            if l2:
                dummy.next = l2
                l2 = l2.next
                dummy = dummy.next
                continue

        return n.next