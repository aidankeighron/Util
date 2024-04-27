from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right

def is_sum_tree(root: Node) -> bool:
    if not root.left and not root.right:
        return True
    left = sum(root.left) if root.left else 0
    right = sum(root.right) if root.right else 0
    return all((root.value == left+right, 
                is_sum_tree(root.left) if root.left else True, 
                is_sum_tree(root.right) if root.right else True))

root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)

print(is_sum_tree(root))