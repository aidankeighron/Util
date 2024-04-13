from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def dimeter_of_binary_tree(root: Node) -> int:
    def depth(node):
        if not node:
            return 0
        return max(depth(node.left), depth(node.right)) + 1
    res = 0
    if root.left:
        res += depth(root.left)
    if root.right:
        res += depth(root.right)
    return res + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(dimeter_of_binary_tree(root))
print(dimeter_of_binary_tree(root.left))
print(dimeter_of_binary_tree(root.right))