from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# In-order Traversal
def in_order(root):
    if root:
        in_order(root.left)
        print(root.value, end=" ")
        in_order(root.right)

# Pre-order Traversal
def pre_order(root):
    if root:
        print(root.value, end=" ")
        pre_order(root.left)
        pre_order(root.right)

# Post-order Traversal
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.value, end=" ")

# Level-order Traversal (BFS)
def level_order(root):
    if not root:
        return

    queue = deque([root])  # Use a deque as a queue for level-order traversal

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        # Add the left and right children to the queue if they exist
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example Tree
root = Node(1)

#level 1
root.left = Node(2)
root.right = Node(3)

# level 2
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# level 3
root.left.left.right = Node(7)
root.right.right.left = Node(8)

print("In-order:")
in_order(root)  # Output: 4 2 5 1 3

print("\nPre-order:")
pre_order(root)  # Output: 1 2 4 5 3

print("\nPost-order:")
post_order(root)  # Output: 4 5 2 3 1

print("\nLevel-order:")
level_order(root)  # Output: 1 2 3 4 5
