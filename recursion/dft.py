# Depth first triversal is used to search a tree or a graph

# it goes from back to fromt


# class represents individual node in the binary tree
class Node:
    def __init__(self, val):
        self.left= None
        self.right = None
        self.val = val
        
def orderPrint(node):
    if node:
        # recurse left
        orderPrint(node.left)
        print(node.val)
        orderPrint(node.right)
        
node= Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.lef = Node(4)
node.right.right = Node(5)
print(orderPrint(node))