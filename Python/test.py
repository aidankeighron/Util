from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def binary_tree_sum(tree: Node) -> int:
    def dfs(node):
        if node is None:
            return 0
        return node.value + dfs(node.left) + dfs(node.right)
    return dfs(tree)

tree1 = Node(10)
tree1.left = Node(5)
tree1.right = Node(-2)

print(binary_tree_sum(tree1))