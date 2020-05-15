# --- Directions
# Return the 'middle' node of a linked list.
# If the list has an even number of elements, return
# the node at the end of the first half of the list.
# *Do not* use a counter variable, *do not* retrieve
# the size of the list, and only iterate
# through the list one time.

class Node:
  def __init__(self, data, next=None, prev=None):
    self.data = data;
    self.next = next;
    self.prev = prev;
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  def insertLast(self, data):
    node = Node(data)
    if self.tail:
      node.prev = self.tail
      self.tail = node
      self.tail.prev.next = node
    else:
      self.head = node
      self.tail = node

l = LinkedList();
l.insertLast('1')
l.insertLast('2')
l.insertLast('3')
l.insertLast('4')
l.insertLast('5')
l.insertLast('6')
# l.insertLast('7')

# assume singly linked
# need 1 pointer to interate through entire list (incrementing 1 node) - slow
# need 2nd pointer to stop at the middle node (incrementing 2 nodes)- fast
# when pointer 2 is at the end of the list return pointer 1
# if .next.next is null return pointer 1 (list is even)

def midpoint(ll):
  p_slow = ll.head
  p_fast = ll.head
  while p_fast.next is not None:
    print(p_slow.data, p_fast.data)
    if p_fast.next.next is None:
      print(p_slow.data)
      return p_slow
    else:
      p_slow = p_slow.next
      p_fast = p_fast.next.next

  print(p_slow.data)
  return p_slow.data


midpoint(l)

# This solution has a run time complexity of O(log n)
# Because: The number of operations performed is less than the number of inputs.