# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        # while there a nodes in both lists 
        # list the lowest head node 
        # then increment that list
        # then link two lists
        
        # strat with new dummy head for new list
        prev = dummy = ListNode(None)
        
        # link prev to the lowest node
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        # then link the linked list with the rest of the nodes
        prev.next = l1 or l2
        return dummy.next
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        