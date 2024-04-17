from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def mirror_binary_tree(root: Node) -> Node:
    def mirror(node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        mirror(node.left)
        mirror(node.right)
    mirror(root)
    return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.left.left = Node(6)
root.left.right = Node(7)
root.left.left.left = Node(6)
root.left.left.left = Node(8)
root.left.left.right = Node(9)

print(mirror_binary_tree(root))
