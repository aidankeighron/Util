from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def binary_tree_to_linked_list(root: Node) -> None:
    def flatten(node):
        if node is None:
            return
        flatten(node.left)
        right = node.right
        node.right = node.left
        node.left = None
        cur = node
        while cur.right:
            cur = cur.right
        
        cur.right = right
        flatten(right)
    flatten(root)

root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.right = Node(6)

binary_tree_to_linked_list(root)
print(root)