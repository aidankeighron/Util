from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def is_sorted(root):
    if root.left and (root.value < root.left.value or not is_sorted(root.left)):
        return False
    if root.right and (root.value > root.right.value or not is_sorted(root.right)):
        return False
    return True

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(7)

print(is_sorted(root))