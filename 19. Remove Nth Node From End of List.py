
"""
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""

"""
ALGO - use 'n' to separate your fast and slow pointers by appropriate distance and then simple point the slow pointer to its next.next at the end

Edge case - [1], 1
Solution - if not fast:
		   	return head.next
		   	# i.e if fast becomes none(and fast.net doesn't exist) it imples we've gone ahead so return head.next as thats the only possibility here.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        i = 0
        
        while i < n:
            fast = fast.next
            i += 1
            
        if not fast:
            return head.next
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head