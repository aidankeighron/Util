from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def merge_two_binary_trees(root: Node, other: Node) -> Node:
    if root is None:
        return other
    if other is None:
        return root

    root.value = root.value + other.value
    root.left = merge_two_binary_trees(root.left, other.left)
    root.right = merge_two_binary_trees(root.right, other.right)
    return root

tree1 = Node(5)
tree1.left = Node(6)
tree1.right = Node(7)
tree1.left.left = Node(2)
tree2 = Node(4)
tree2.left = Node(5)
tree2.right = Node(8)
tree2.left.right = Node(1)
tree2.right.right = Node(4)
merged_tree = merge_two_binary_trees(tree1, tree2)
print(merged_tree)