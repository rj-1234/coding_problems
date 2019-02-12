"""
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


"""
ALGO - Divid and Conquer
	three basic cases, 
		1 list has no elements // simple
		2 list has 1 element   // simple
		3 list has 2 		   // return sorted linked list from 2 sorted linked lists
		4 list has more than 2 elements 	// divide k lists from between (length of lists) and then call mergeKLists on both halves
"""
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = len(lists)
        
        if not lists or l == 0:
            return None
        
        elif l == 1:
            return lists[0]
        
        elif l == 2:
            return self.merge2lists(lists[0], lists[1])
        
        else:
            mid = l/2
            return self.mergeKLists([self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])])
        
        
    def merge2lists(self, l1, l2):
        dummy = current = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
                current = current.next
            else:
                current.next = l2
                l2 = l2.next
                current = current.next
            
        if l1:
            current.next = l1
        
        if l2:
            current.next = l2
            
        return dummy.next