
class SinglyLinkedListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def compare(llist1: SinglyLinkedListNode, llist2: SinglyLinkedListNode):
    tempListHead1 = llist1
    tempListHead2 = llist2
    if tempListHead1 == None and tempListHead2 == None and tempListHead1.val == tempListHead2.val:
  
        tempNext1 = tempListHead1.next
        tempNext2 = tempListHead2.next
        if tempNext1 == tempNext2:
            return 1
        else:
            return 0

    return

