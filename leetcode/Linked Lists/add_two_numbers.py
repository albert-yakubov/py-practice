# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
# initialize head of linked list:
class LinkedList(object):
    def __init__(self):
        self.head = None


class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        start = ListNode(0)
        # modifying l2
        l2_prev = None
        start.next = l2
        # check for lenght, missmatch and check if there is anything to carry over:
        while(l1 or l2) or carry != 0:
            # utilize linked list sizes
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
                # then link the prev pointer to the next:
                l2_prev.next = l2
            total = l1.val + l2.val + carry
            # skip zero values:
            modulo = total % 10 
            l2.val = modulo
            carry = int((total-modulo)/10)
            l2_prev = l2
            l1 = l1.next
            l2 = l2.next
        
        
        
        
        
        return start.next